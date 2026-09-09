#!/usr/bin/env python3
"""Run a simulated App Creator interview against the app-idea skill.

Two `claude -p` sessions talk to each other through this script:
  - the "agent" session runs the skill and interviews the App Creator
  - the "ac" session role-plays the App Creator from a persona file

Usage:
  python3 run-interview.py --persona personas/hr-onboarding-tracker.md \
      --skill ../app-idea --out iteration-1/hr-onboarding-tracker --model claude-sonnet-5

Outputs in --out:
  transcript.md   human-readable transcript
  turns.jsonl     one JSON object per CLI call (raw result, session ids, cost, duration)
  brief/          copy of every .md the agent wrote in its project dir
The agent's working directory is OUTSIDE this repo (see --project-dir). The script refuses to run
if that directory sits inside another git work tree, because the skill will branch and commit there.
"""
import argparse, json, os, pathlib, subprocess, sys, time

AGENT_HARNESS = """You are running the App Creator Framework skill at {skill}/SKILL.md. The user invoked it with /app-idea.
Read {skill}/SKILL.md now and follow it exactly, including the reference files it names.
You are talking to the App Creator through a chat window. Every reply you write goes straight to them, so write only what you would say to them. Do not narrate tool use or address anyone else.
Your working directory is {project}. {repo_note}
When the skill's Finishing section is satisfied and you have told the App Creator the closing items, end that final message with the exact text [INTERVIEW COMPLETE] on its own line."""

def run_claude(prompt, cwd, model, resume=None, system_prompt=None, append_system=None,
               allowed_tools=None, disallowed_tools=None, no_tools=False, add_dirs=(), timeout=900):
    cmd = ["claude", "-p", prompt, "--model", model, "--output-format", "json"]
    if resume:
        cmd += ["--resume", resume]
    if system_prompt:
        cmd += ["--system-prompt", system_prompt]
    if append_system:
        cmd += ["--append-system-prompt", append_system]
    if allowed_tools:
        cmd += ["--allowedTools", *allowed_tools]
    if disallowed_tools:
        cmd += ["--disallowedTools", *disallowed_tools]
    if no_tools:
        cmd += ["--tools", ""]
    for d in add_dirs:
        cmd += ["--add-dir", d]
    t0 = time.time()
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    dur = time.time() - t0
    if proc.returncode != 0:
        raise RuntimeError(f"claude exited {proc.returncode}\nSTDOUT:\n{proc.stdout[-2000:]}\nSTDERR:\n{proc.stderr[-2000:]}")
    data = json.loads(proc.stdout)
    data["_duration_s"] = round(dur, 1)
    return data

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--persona", required=True)
    ap.add_argument("--skill", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="claude-sonnet-5")
    ap.add_argument("--max-agent-turns", type=int, default=50)
    ap.add_argument("--project-dir", default=None,
                    help="Agent working dir. Must be OUTSIDE this framework repo. Defaults to $CLAUDE_JOB_DIR/tmp/<out-name>/project or /tmp.")
    ap.add_argument("--git-init", action="store_true",
                    help="Make the project dir its own git repo (no remote) so the skill's in-repo path is exercised safely.")
    ap.add_argument("--opener", default="Hi, I want to build a dashboard that shows me where every new hire is in their onboarding. Right now it's a nightmare spreadsheet.")
    args = ap.parse_args()

    skill = str(pathlib.Path(args.skill).resolve())
    out = pathlib.Path(args.out).resolve(); out.mkdir(parents=True, exist_ok=True)
    if args.project_dir:
        project = pathlib.Path(args.project_dir).resolve()
    else:
        base = pathlib.Path(os.environ.get("CLAUDE_JOB_DIR", "/tmp")) / "tmp" / "app-idea-runs" / out.name
        project = base / "project"
    project.mkdir(parents=True, exist_ok=True)
    # Refuse to run with the project dir inside a git work tree we don't own: the skill will branch/commit/push there.
    chk = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=str(project), capture_output=True, text=True)
    if chk.returncode == 0 and pathlib.Path(chk.stdout.strip()) != project:
        sys.exit(f"Refusing: project dir {project} is inside git repo {chk.stdout.strip()}. Use --project-dir outside any repo.")
    if args.git_init and chk.returncode != 0:
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=str(project), check=True)
        # Throwaway identity, no commit signing: keeps the test repo from using the developer's key or name.
        for k, v in (("commit.gpgsign", "false"), ("user.name", "ACF Test Agent"), ("user.email", "acf-test@example.invalid")):
            subprocess.run(["git", "config", "--local", k, v], cwd=str(project), check=True)
        subprocess.run(["git", "commit", "-q", "--allow-empty", "-m", "init"], cwd=str(project), check=True)
    ac_dir = out / "ac"; ac_dir.mkdir(exist_ok=True)
    persona = pathlib.Path(args.persona).read_text()
    transcript = out / "transcript.md"
    turns = out / "turns.jsonl"
    transcript.write_text(f"# Interview transcript\n\nPersona: `{args.persona}`  \nModel: `{args.model}`  \nSkill: `{skill}`\n\n")

    def log(role, text, meta):
        with transcript.open("a") as f:
            f.write(f"### {role}\n\n{text.strip()}\n\n---\n\n")
        with turns.open("a") as f:
            f.write(json.dumps({"role": role, "text": text, **{k: v for k, v in meta.items() if k != 'result'}}) + "\n")
        print(f"[{role}] {text.strip()[:160].replace(chr(10),' ')} ...", flush=True)

    agent_sid = None; ac_sid = None
    ac_msg = args.opener
    log("App Creator", ac_msg, {"turn": 0})

    for turn in range(1, args.max_agent_turns + 1):
        prompt = ac_msg if agent_sid else f"[The App Creator invoked /app-idea and wrote:]\n\n{ac_msg}"
        r = run_claude(prompt, cwd=str(project), model=args.model, resume=agent_sid,
                       append_system=AGENT_HARNESS.format(skill=skill, project=project,
                           repo_note=("It is a local git repository with no remote and no pull request tooling; if the skill calls for a pull request, commit on a branch and stop there."
                                      if args.git_init else "Write the brief as a file here. There is no repository and no download mechanism in this test; telling the App Creator the file name is enough.")),
                       allowed_tools=["Read", "Write", "Edit", "Glob", "Grep", "Bash(ls:*)", "Bash(pwd)", "Bash(mkdir:*)"]
                                     + (["Bash(git status:*)", "Bash(git rev-parse:*)", "Bash(git branch:*)", "Bash(git checkout:*)",
                                         "Bash(git switch:*)", "Bash(git add:*)", "Bash(git commit:*)", "Bash(git log:*)", "Bash(git diff:*)"] if args.git_init else []),
                       disallowed_tools=["Bash(git push:*)", "Bash(git remote:*)", "Bash(git fetch:*)", "Bash(git pull:*)", "Bash(gh:*)"]
                                        + ([] if args.git_init else ["Bash(git:*)"]),
                       add_dirs=[skill])
        agent_sid = r.get("session_id", agent_sid)
        agent_msg = r.get("result", "")
        log(f"Agent (turn {turn})", agent_msg, r)
        if "[INTERVIEW COMPLETE]" in agent_msg:
            print("Agent signalled completion.", flush=True); break

        nudge = ""
        if turn == 35: nudge = "\n\n(You have a meeting in about five minutes.)"
        if turn >= 45: nudge = "\n\n(You really have to leave now.)"
        r2 = run_claude(agent_msg + nudge, cwd=str(ac_dir), model=args.model, resume=ac_sid,
                        system_prompt=persona, no_tools=True)
        ac_sid = r2.get("session_id", ac_sid)
        ac_msg = r2.get("result", "")
        log("App Creator", ac_msg, r2)
        if "[AC LEAVES]" in ac_msg:
            print("App Creator left.", flush=True); break
    else:
        print("Hit max agent turns.", flush=True)

    briefs = [b for b in project.rglob("*.md") if ".git" not in b.parts]
    import shutil
    for b in briefs:
        dest = out / "brief" / b.relative_to(project); dest.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(b, dest)
    summary = {"agent_session": agent_sid, "ac_session": ac_sid, "turns": turn, "project_dir": str(project), "briefs": [str(b) for b in briefs]}
    (out / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()

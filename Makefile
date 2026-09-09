# Developer tasks for the App Creator Framework repo.

WORKSPACE := skills/app-creator/app-idea-workspace
PERSONA   ?= hr-onboarding-tracker
ITERATION ?= 1
MODEL     ?= claude-sonnet-5

.PHONY: help test-app-idea

help:
	@echo "make test-app-idea [PERSONA=hr-onboarding-tracker] [ITERATION=1] [MODEL=claude-sonnet-5]"
	@echo "  Run a simulated App Creator interview against skills/app-creator/app-idea."
	@echo "  Two 'claude -p' sessions talk to each other; the agent side has no git access."
	@echo "  Output: $(WORKSPACE)/iteration-N/<persona>/{transcript.md,turns.jsonl,brief/}"

test-app-idea:
	cd $(WORKSPACE) && python3 run-interview.py \
		--persona personas/$(PERSONA).md \
		--skill ../app-idea \
		--out iteration-$(ITERATION)/$(PERSONA) \
		--model $(MODEL)

.PHONY = pip_compile pip_sync
pip_compile:
	pip-compile

pip_sync:
	pip-sync

.PHONY = run
run:
	uvicorn app.main:app --reload

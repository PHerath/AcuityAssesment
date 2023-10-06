SHELL := /bin/bash
.ONESHELL:

.PHONY: run
run:
	( \
       source venv/bin/activate; \
       pip3 install -r requirements.txt; \
       uvicorn app.main:app --reload; \
    )

init:
	virtualenv -p python3.10 venv
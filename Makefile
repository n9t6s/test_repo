SHELL := /bin/bash

venv:
	python3.8 -m venv venv

.ONESHELL:
.install-reqs:
	source venv/bin/activate
	@python --version
	python -m pip install -r requirements.txt

init: venv .install-reqs
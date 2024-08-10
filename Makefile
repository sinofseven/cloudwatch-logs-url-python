SHELL = /usr/bin/env bash -xeuo pipefail

format: \
	fmt-isort \
	fmt-black

lint: \
	lint-isort \
	lint-black \
	lint-flake8

fmt-isort:
	poetry run isort aws_cloudwatch_logs_url/ tests/

fmt-black:
	poetry run black aws_cloudwatch_logs_url/ tests/

lint-isort:
	poetry run isort --check aws_cloudwatch_logs_url/ tests/

lint-black:
	poetry run black --check aws_cloudwatch_logs_url/ tests/

lint-flake8:
	poetry run flake8 aws_cloudwatch_logs_url/ tests/

test-unit:
	poetry run pytest -vv tests/unit

.PHONY: \
	format \
	lint \
	fmt-isort \
	fmt-black \
	lint-isort \
	lint-black \
	lint-flake8 \
	test-unit

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

gdiff:
	poetry run gendiff -h

test:
	poetry run pytest gendiff tests

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build

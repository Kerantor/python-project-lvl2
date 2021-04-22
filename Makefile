install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

gdiff:
	poetry run gendiff -h

package-install:
	python3 -m pip install --user dist/*.whl

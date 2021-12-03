install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build
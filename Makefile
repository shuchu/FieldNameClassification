format: 
	python -m isort *.py
	python -m black --target-version py39 *.py
lint:
	python -m mypy *.py
	python -m isort *.py
	python -m flake8 *.py
	python -m black --check *.py

test:
	python -m pytest ./tests

.PHONY: install analyze report test clean

install:
	pip install -e .
	pip install -r requirements.txt

analyze:
	python scripts/analyze.py

report:
	python scripts/report.py

test:
	pytest -q

clean:
	rm -rf __pycache__ src/agromarket/__pycache__ .pytest_cache

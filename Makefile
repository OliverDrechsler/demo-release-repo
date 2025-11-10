# Minimal Makefile to build Sphinx docs

.PHONY: html

html:
	@mkdir -p docs/_build
	python -m pip install --quiet -r requirements.txt || true
	python -m pip install --quiet sphinx sphinx-rtd-theme myst-parser || true
	sphinx-build -b html docs docs/_build/html

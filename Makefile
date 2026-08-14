.PHONY: seed collect generate validate test update serve

seed:
	python scripts/build_seed.py

generate:
	python -m hcr generate

validate:
	python -m hcr validate

collect:
	python -m hcr collect --since-days 120

update:
	python -m hcr update --since-days 120

test:
	python -m unittest discover -s tests -v

serve:
	python -m hcr serve --bind 0.0.0.0 --port 8765

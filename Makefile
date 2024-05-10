project_dir := .
src_dir := src

# Lint code
.PHONY: lint
lint:
	@poetry run ruff check $(project_dir) --fix
	@poetry run mypy $(src_dir)

# Format code
.PHONY: format
format:
	@poetry run black $(project_dir)
	@poetry run isort $(project_dir)

# Lint + format + stattic analyzer
.PHONY: prepare
prepare: format lint

.PHONY: migrate
migrate:
	@poetry run alembic upgrade head
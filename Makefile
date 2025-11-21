test:
	uv run pytest

test-coverage:
	uv run pytest --cov=brain_games --cov-report=xml:coverage.xml

lint:
	uv run ruff check brain_games

format:
	uv run ruff format brain_games

install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

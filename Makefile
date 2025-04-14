install:
	uv sync
brain-games:
	uv run brain-games
lint:
	ruff check brain_games
format:
	ruff format brain_games
	ruff format .
	ruff check --fix .

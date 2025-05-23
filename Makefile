venv-setup: ## Install project dependencies using Poetry
	@echo ">>> Setting up Python virtual environment and installing dependencies with Poetry..."
	poetry install --no-interaction

chromadb-up:
	@echo ">>> Starting ChromaDB service..."
	docker run -v ./chroma-data:/data -p 8000:8000 chromadb/chroma

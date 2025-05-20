# CrawlerOne

## Project setup

```bash
pyenv local 3.11.7
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pre-commit install
```

## Checks

### Run tests

```bash
pytest
```

### Pre-commit

```bash
git add .
pre-commit run --all-files
```

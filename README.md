# CrawlerOne

## Project setup

```bash
pyenv local 3.11.7
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pre-commit install        # pre-commit clean
```

## Checks

### Run tests

#### All tests

```bash
pytest
```

#### Unit / Integration tests

```bash
pytest unit
pytest integration
```

### Pre-commit

```bash
git add .
pre-commit run --all-files
```

## Run project

```bash
python -m crawler.main
```

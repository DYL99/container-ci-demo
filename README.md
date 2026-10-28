# CPS 310 Container & CI Demo

This small Python project is used to demonstrate containers and continuous integration.

## What the Program Does

The program:

- loads settings from `config.json`
- reads task data from `tasks.csv`
- calculates a simple task summary
- prints the results to the terminal

## Requirements

- Python 3.12 or newer
- Git

Install Python dependencies with:

```text
python -m pip install -r requirements.txt
```

## Create a Virtual Environment

### Windows

```text
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### macOS

```text
python3 -m venv .venv
source .venv/bin/activate
```

## Run the Program

### Windows

```text
python app.py
```

### macOS

```text
python3 app.py
```

## Run the Tests

### Windows

```text
python -m pytest -v
```

### macOS

```text
python3 -m pytest -v
```

## Run Local Verification

### Windows

```text
.\verify.ps1
```

### macOS

```text
chmod +x verify.sh
./verify.sh
```

## Class Demo

Docker and GitHub Actions files are intentionally not included yet.

During the live demo, we will add:

```text
Dockerfile
.dockerignore
.github/workflows/tests.yml
```

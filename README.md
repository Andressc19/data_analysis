# Project: StudentsPerformance — Quick Start Guide

## Description

This repository contains examples and quick steps to perform an Exploratory Data Analysis (EDA) on `datasets/StudentsPerformance.csv`.

It includes clear instructions to create and activate a virtual environment (`venv`) on both macOS and Windows, and how to install dependencies from `requirements.txt`.

## Prerequisites

* Python 3.8+ installed (available as `python` or `python3`).
* You are located at the project root directory (the folder that contains `requirements.txt` and `datasets/`).

---

## Create and activate a `venv`

Below are the commands to create and activate a virtual environment on macOS and Windows.

### macOS (zsh / Terminal)

```bash
# 1) Create the virtual environment
python3 -m venv .venv

# 2) Activate the environment (zsh)
source .venv/bin/activate

# 3) Verify the prompt now starts with (.venv)
```

### Windows — PowerShell

```powershell
# 1) Create the virtual environment
python -m venv .venv

# 2) Activate in PowerShell
.\.venv\Scripts\Activate.ps1

# Note: if PowerShell blocks script execution, run (as administrator or in your user scope):
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### Windows — CMD (Command Prompt)

```cmd
REM 1) Create the virtual environment
python -m venv .venv

REM 2) Activate in CMD
.venv\Scripts\activate.bat
```

### Deactivate the environment

```bash
deactivate
```

---

## Install dependencies

With the virtual environment activated (you should see `(.venv)` in the prompt), install the project dependencies:

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Folder structure
```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── constants.py
│   ├── datasets
│   │   ├── StudentsPerformance.csv
│   │   ├── StudentsPerformance_AVG.csv
│   │   ├── StudentsPerformance_LUNCH_AVG.csv
│   │   ├── StudentsPerformance_NORMALIZED.csv
│   │   ├── StudentsPerformance_PLE_AVG.csv
│   │   └── StudentsPerformance_TPC_AVG.csv
│   ├── diagrams
│   ├── graphs
│   │   ├── __init__.py
│   │   ├── course_distribution.py
│   │   ├── ethnicity_distribution.py
│   │   ├── gender_distribution.py
│   │   ├── lunch_distribution.py
│   │   └── parental_level_distribution.py
│   ├── measure
│   │   └── metrics.py
│   ├── utils.py
│   └── validations.py
├── main.py
├── requirements.txt
└── validations.py
```
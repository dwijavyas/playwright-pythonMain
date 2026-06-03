# 🧪 Playwright-Python Hybrid E2E UI + API Test Automation Framework

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language (3.11) |
| Playwright | UI Automation Framework |
| pytest | Test Runner |
| Debian | Operating System |
| Allure Reports | Test Reporting |
| HTML Reports | Reporting |
| Jenkins | CI/CD Pipeline |
| VS Code | IDE |
| MIT License | Open Source License |

---

## Overview

This is a hybrid automation framework combining **UI and API testing** using **Playwright with Python** and `pytest`. The project is designed to run on **Debian** using a `uv` virtual environment, and integrates with **Jenkins** for CI/CD pipelines. The framework supports:

- Full **End-to-End testing** for an eCommerce platform
- **UI automation** with Playwright
- **API testing** for placing orders via REST endpoints
- **Allure & HTML Reports** for test visualization
- **Page Object Model (POM)** structure
- **Network Interception** testing
- Uses **pytest fixtures** and reusable utilities
- Playwright Trace Viewer for visual debugging
- GitHub integrated with `.gitignore` best practices

---

## Tech Stack

| Layer         | Tool / Technology       | Description                                |
|--------------|--------------------------|--------------------------------------------|
| Language      | `Python 3.11+`           | Core scripting language                    |
| Framework     | `Playwright`             | E2E browser automation                     |
| Test Runner   | `pytest`                 | Test execution                             |
| Reports       | `Allure`, `pytest-html`  | Rich and clean test reports                |
| Versioning    | `git`, `GitHub`          | Source control                             |
| OS            | `Debian (Linux)`         | Project environment                        |
| CI/CD         | `Jenkins`                | Automation server for test pipelines       |
| Editor        | `Visual Studio Code`     | Development IDE                            |
| Environment   | `uv` (virtualenv)        | Lightweight virtual Python environment     |

---

## Project Features

- **Hybrid Testing**: Combines UI and API layers
- **Order Placement via API**: Simulated checkout using REST POST call
- **UI Verification**: Product selection, cart, and post-order validation
- **Playwright POM Architecture**: Maintains reusability & scalability
- **Network Interception Tests**: Validates API calls/responses in-browser
- **Environment-Specific Configuration**: Easily switch between environments
- **Allure Reporting Integration**
- **Runs on Jenkins Pipelines with parameterization**
- **Clean GitHub Repo** with `.gitignore`, `requirements.txt`, and `README.md`

---
## How to Run

pytest -s -n 3
pytest -m smoke
pytest -k web
pytest --html=reports/html-report/report.html --self-contained-html


# Project Name: emojihub-cli

## Overview
`emojihub-cli` is a Python CLI tool for exploring and finding emojis. It uses the public EmojiHub API to fetch emoji data. This project is for a class, emphasizing clean code, docstrings, comprehensive testing with `pytest`, and a CI/CD pipeline with GitHub Actions.

## API Integration
- **API:** EmojiHub
- **Base URL:** `https://emojihub.yurace.pro/api`
- **Auth:** None required.

## CLI Commands (using argparse)
The tool will be runnable via `python -m src.main [command]`.

1.  `random`: Fetches and displays a single random emoji.
    - **Endpoint:** `/random`
2.  `list-groups`: Fetches and lists all available emoji group names.
    - **Endpoint:** `/groups`
3.  `by-group <group_name>`: Fetches all emojis for a given group.
    - **Argument:** `group_name` (e.g., "face-positive")
    - **Endpoint:** `/all/group/{group_name}`
4.  `search <query>`: Searches for emojis by name.
    - **Argument:** `query` (e.g., "cat")
    - **Endpoint:** `/search?q={query}`

## Technical Stack
- Python 3.10+
- `argparse` for CLI
- `requests` for API calls
- `pytest` for testing
- `unittest.mock` for mocking API calls in tests
- GitHub Actions for CI/CD

## Code Organization
- `src/main.py`: CLI entry point, `argparse` setup, main logic.
- `src/api.py`: All functions that interact with the EmojiHub API.
- `tests/test_api.py`: `pytest` tests for `api.py` (all API calls MUST be mocked).
- `tests/test_main.py`: `pytest` tests for `main.py` (CLI logic, mocks `src.api` functions).

## Standards
- Follow PEP 8 guidelines.
- All functions and classes must have docstrings.
- Handle `requests` errors gracefully (e.g., `try...except`).
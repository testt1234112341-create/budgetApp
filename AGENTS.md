# AGENTS.md

## Project Overview

This repository is a Python CLI budget app project.
It uses CSV files as the source of truth for transactions and is built to support incremental, test-first development.

## Coding Rules

- Type hints are required for all functions and public interfaces.
- Keep each function to 50 lines or fewer.
- Prefer small, focused functions with clear names.

## TDD Rules

- Write tests before implementation.
- Do not add production code until the target behavior is covered by tests.
- When changing behavior, update or add tests first.

## Quality Rules

- Keep cyclomatic complexity at 10 or below.
- Prefer simple control flow and early returns where possible.

## QA Review Rules

- Before every commit, run quality review through the `qa_engineer` subagent.
- Use the review result to fix issues before committing.

## Test Commands

- `pytest`
- `radon cc`

## Commit Rules

- Commit once a single feature is complete.
- Push after each feature commit.
- Keep commits small and feature-focused.


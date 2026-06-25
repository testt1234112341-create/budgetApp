---
name: budget-cli
description: Use for this repository's Python CLI budget app work, including CSV transaction handling, TDD implementation, test maintenance, and quality checks guided by AGENTS.md.
---

# Budget CLI Skill

Use this skill for work in this repository.

## Core Rules

- Follow [AGENTS.md](/Users/elice47/Documents/budgetApp/AGENTS.md).
- Use TDD: tests first, implementation second.
- Keep functions small, typed, and easy to review.
- Keep cyclomatic complexity at 10 or below.

## Workflow

1. Read the relevant CSV sample or existing tests before changing behavior.
2. Write or update tests first.
3. Implement the smallest change that satisfies the tests.
4. Run `pytest`.
5. Run `radon cc` for complexity checks.
6. Before committing, have `qa_engineer` review the change.

## When To Use

- Adding or changing CSV loading logic
- Transaction calculations
- Filtering and summary features
- Test expansion and refactoring
- Quality checks before commit


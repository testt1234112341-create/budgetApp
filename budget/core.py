"""Core business logic for the CLI budget app."""

from __future__ import annotations

from typing import Any, Dict, List


Transaction = Dict[str, Any]


def add_transaction(transactions: List[Transaction], transaction: Transaction) -> List[Transaction]:
    """Return a new transaction list with one transaction appended."""
    pass


def get_balance(transactions: List[Transaction]) -> float:
    """Return the balance computed from all transaction amounts."""
    pass


def filter_by_category(transactions: List[Transaction], category: str) -> List[Transaction]:
    """Return transactions that match the given category."""
    pass


def load_transactions_from_csv(file_path: str) -> List[Transaction]:
    """Load transactions from a CSV file."""
    pass


def monthly_summary(transactions: List[Transaction]) -> Dict[str, Dict[str, int]]:
    """Return monthly income, expense, and net totals."""
    pass


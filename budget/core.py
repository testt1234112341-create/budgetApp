"""Core business logic for the CLI budget app."""

from __future__ import annotations

from typing import Any, Dict, List


Transaction = Dict[str, Any]


def add_transaction(transactions: List[Transaction], transaction: Transaction) -> List[Transaction]:
    """Return a new transaction list with one transaction appended."""
    return transactions + [transaction]


def get_balance(transactions: List[Transaction]) -> float:
    """Return the balance computed from all transaction amounts."""
    return float(sum(transaction["amount"] for transaction in transactions))


def filter_by_category(transactions: List[Transaction], category: str) -> List[Transaction]:
    """Return transactions that match the given category."""
    target_category = category.casefold()
    return [
        transaction
        for transaction in transactions
        if str(transaction["category"]).casefold() == target_category
    ]


def load_transactions_from_csv(file_path: str) -> List[Transaction]:
    """Load transactions from a CSV file."""
    pass


def monthly_summary(transactions: List[Transaction]) -> Dict[str, Dict[str, int]]:
    """Return monthly income, expense, and net totals."""
    pass

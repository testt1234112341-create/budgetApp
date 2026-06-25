"""Core business logic for the CLI budget app."""

from __future__ import annotations

import csv
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
    transactions: List[Transaction] = []
    with open(file_path, encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transaction: Transaction = {
                "date": row["date"],
                "type": row["type"],
                "category": row["category"],
                "description": row["description"],
                "amount": int(row["amount"]),
                "memo": row["memo"],
            }
            transactions.append(transaction)
    return transactions


def monthly_summary(transactions: List[Transaction]) -> Dict[str, Dict[str, int]]:
    """Return monthly income, expense, and net totals."""
    summary: Dict[str, Dict[str, int]] = {}
    for transaction in transactions:
        month = str(transaction["date"])[:7]
        amount = int(transaction["amount"])
        if month not in summary:
            summary[month] = {"income": 0, "expense": 0, "net": 0}
        if amount >= 0:
            summary[month]["income"] += amount
        else:
            summary[month]["expense"] += amount
        summary[month]["net"] += amount
    return summary

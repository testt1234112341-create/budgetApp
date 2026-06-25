"""Tests for budget core behavior."""

from budget.core import (
    add_transaction,
    filter_by_category,
    get_balance,
    load_transactions_from_csv,
    monthly_summary,
)


def test_add_transaction_increases_length() -> None:
    """Adding a transaction should increase the list length by one."""
    transactions = []
    transaction = {
        "date": "2026-01-05",
        "type": "지출",
        "category": "식비",
        "description": "점심식사",
        "amount": -12000,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert len(result) == 1


def test_add_transaction_preserves_negative_amount() -> None:
    """Negative amounts should be stored unchanged for expenses."""
    transactions = []
    transaction = {
        "date": "2026-01-05",
        "type": "지출",
        "category": "식비",
        "description": "점심식사",
        "amount": -12000,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert result[0]["amount"] == -12000


def test_add_transaction_preserves_positive_amount() -> None:
    """Positive amounts should be stored unchanged for income."""
    transactions = []
    transaction = {
        "date": "2026-01-07",
        "type": "수입",
        "category": "급여",
        "description": "월급",
        "amount": 3500000,
        "memo": "1월급여",
    }

    result = add_transaction(transactions, transaction)

    assert result[0]["amount"] == 3500000


def test_add_transaction_allows_empty_description() -> None:
    """Empty descriptions should be accepted as-is."""
    transactions = []
    transaction = {
        "date": "2026-01-28",
        "type": "기타수입",
        "category": "기타수입",
        "description": "",
        "amount": 25000,
        "memo": "중고마켓",
    }

    result = add_transaction(transactions, transaction)

    assert result[0]["description"] == ""


def test_get_balance_returns_zero_for_empty_list() -> None:
    """An empty transaction list should produce zero balance."""
    assert get_balance([]) == 0.0


def test_get_balance_sums_step2_sample_data() -> None:
    """Sample step2 transactions should sum to the expected balance."""
    transactions = [
        {
            "date": "2026-01-04",
            "type": "지출",
            "category": "여행",
            "description": "항공권",
            "amount": -979796,
            "memo": "메모_3",
        },
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "의료",
            "description": "한의원",
            "amount": -65990,
            "memo": "카드결제",
        },
        {
            "date": "2026-01-15",
            "type": "수입",
            "category": "기타수입",
            "description": "중고 판매",
            "amount": 135541,
            "memo": "",
        },
        {
            "date": "2026-02-01",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 4358625,
            "memo": "",
        },
    ]

    assert get_balance(transactions) == 3448380


def test_filter_by_category_matches_actual_category_names() -> None:
    """Filtering should return matching transactions from the sample data."""
    transactions = [
        {
            "date": "2026-01-10",
            "type": "지출",
            "category": "쇼핑",
            "description": "생활용품",
            "amount": -326526,
            "memo": "",
        },
        {
            "date": "2026-02-05",
            "type": "지출",
            "category": "쇼핑",
            "description": "옷 구입",
            "amount": -63587,
            "memo": "메모_5",
        },
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "의료",
            "description": "한의원",
            "amount": -65990,
            "memo": "카드결제",
        },
    ]

    result = filter_by_category(transactions, "쇼핑")

    assert len(result) == 2
    assert all(item["category"] == "쇼핑" for item in result)


def test_filter_by_category_is_case_insensitive() -> None:
    """Category matching should ignore case differences."""
    transactions = [
        {
            "date": "2026-01-15",
            "type": "지출",
            "category": "문화/여가",
            "description": "영화관",
            "amount": -64470,
            "memo": "현금",
        }
    ]

    result = filter_by_category(transactions, "문화/여가".lower())

    assert result == transactions


def test_filter_by_category_returns_empty_list_for_missing_category() -> None:
    """Missing categories should produce an empty list."""
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "의료",
            "description": "한의원",
            "amount": -65990,
            "memo": "카드결제",
        }
    ]

    assert filter_by_category(transactions, "식비") == []


def test_filter_by_category_returns_independent_list() -> None:
    """Returned results should not alias the original list."""
    transactions = [
        {
            "date": "2026-01-10",
            "type": "지출",
            "category": "쇼핑",
            "description": "생활용품",
            "amount": -326526,
            "memo": "",
        }
    ]

    result = filter_by_category(transactions, "쇼핑")
    result.append(
        {
            "date": "2026-02-05",
            "type": "지출",
            "category": "쇼핑",
            "description": "옷 구입",
            "amount": -63587,
            "memo": "메모_5",
        }
    )

    assert len(transactions) == 1
    assert len(result) == 2


def test_load_transactions_from_csv_reads_step1_sample() -> None:
    """CSV loading should parse the step1 sample file correctly."""
    result = load_transactions_from_csv("data/step1_transactions.csv")

    assert len(result) == 10
    assert result[0] == {
        "date": "2026-01-05",
        "type": "지출",
        "category": "식비",
        "description": "점심식사",
        "amount": -12000,
        "memo": "",
    }
    assert result[1]["amount"] == 3500000
    assert isinstance(result[1]["amount"], int)


def test_monthly_summary_groups_step3_sample_data() -> None:
    """Monthly summary should aggregate income, expense, and net totals."""
    transactions = load_transactions_from_csv("data/step3_transactions.csv")

    result = monthly_summary(transactions)

    assert result["2025-01"] == {
        "income": 405037,
        "expense": -2886860,
        "net": -2481823,
    }
    assert result["2025-12"] == {
        "income": 6867295,
        "expense": -3540137,
        "net": 3327158,
    }

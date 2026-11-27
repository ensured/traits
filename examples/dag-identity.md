---
description: "An Airflow DAG uses the same name for its file stem, DAG ID, and decorated function"
when: "Adding or renaming an Airflow DAG"
paths: dags/**
---

Define one DAG per file and call its decorated function at module scope.

## Why

The DAG ID shown in the scheduler identifies the source file directly.

## Pattern

```python
# dags/refresh_book_availability.py
@dag(
    dag_id="refresh_book_availability",
    schedule="@daily",
    start_date=datetime(2024, 1, 1, tzinfo=timezone.utc),
    catchup=False,
)
def refresh_book_availability() -> None:
    refresh_availability()


refresh_book_availability()
```

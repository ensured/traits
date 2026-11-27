---
description: "Scheduled catalog refresh DAGs set catchup=False"
when: "Adding or changing a schedule for a catalog refresh DAG"
paths: dags/**
---

Each run reads the latest available snapshot. Multiple catchup runs would
read the same snapshot again.

## Pattern

```python
@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1, tzinfo=timezone.utc),
    catchup=False,
)
def refresh_book_availability() -> None:
    refresh_availability()
```

## Exceptions

A refresh DAG that imports a distinct file for each data interval enables
catchup so the scheduler processes each missed interval.

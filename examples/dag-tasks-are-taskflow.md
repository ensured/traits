---
description: "Airflow DAGs express catalog transformations as TaskFlow functions"
when: "Adding a catalog transformation task"
paths: dags/**
---

Decorate the Python function with `@task` and call it from the DAG to pass
its result to the next task.

## Pattern

```python
@task
def normalise_isbns(isbns: list[str]) -> list[str]:
    return sorted({isbn.replace("-", "") for isbn in isbns})


def refresh_catalog() -> None:
    store_isbns(normalise_isbns(load_isbns()))
```

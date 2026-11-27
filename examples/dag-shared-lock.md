---
description: "Catalog maintenance DAGs bracket writes with lock setup and teardown tasks"
when: "Adding or rewiring an Airflow DAG that makes a bulk catalog change"
paths: dags/**
---

The acquisition and release tasks use the same lock key. The lock service
tracks the run that acquired the lock and checks ownership on release.

## Why

Bulk catalog rewrites share one resource. Tying teardown to setup lets Airflow
release the lock after a successful acquisition even when a work task fails.

## Pattern

```python
def rebuild_catalog_index() -> None:
    lock = AcquireLockSensor(task_id="acquire_lock", key="catalog")
    release = ReleaseLockOperator(task_id="release_lock", key="catalog")
    lock >> rebuild_index() >> release.as_teardown(setups=lock)
```

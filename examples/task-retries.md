---
description: "Airflow retry policies are declared on individual tasks"
when: "Configuring retries for an Airflow task"
paths: dags/**
---

Set `retries` and `retry_delay` on the task whose work can be repeated.
Choose the settings based on that task's failure modes.

## Pattern

```python
@task(retries=2, retry_delay=timedelta(minutes=3))
def load_isbns() -> list[str]:
    return read_isbn_feed()
```

---
description: "Tasks open MongoDB through an Airflow connection inside the task body"
when: "Writing an Airflow task that needs MongoDB"
paths: dags/**
---

Open the hook in a context manager so that the connection closes when the
task exits. Pass small values such as document IDs between tasks.

## Why

Parsing the DAG stays free of database connections, and workers own the
lifetime of the connections they use.

## Pattern

```python
@task
def count_books() -> int:
    with MongoHook(mongo_conn_id="catalog_mongo") as hook:
        return hook.get_collection("books").count_documents({})
```

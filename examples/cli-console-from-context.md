---
description: "CLI commands write through the output streams in the Click context"
when: "Writing CLI output"
paths: src/library_catalog/cli/commands/*.py
---

The application puts an object with `stdout` and `stderr` streams in the
Click context. Commands use `stdout` for results and `stderr` for diagnostics.

## Why

Pipelines can consume the result stream, and tests can supply their own streams.

## Pattern

```python
@books.command()
@click.pass_obj
def count_books(context: CatalogContext) -> None:
    click.echo(context.books.count(), file=context.stdout)
```

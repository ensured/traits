---
description: "CLI commands raise click.ClickException for failures a user can resolve"
when: "Handling an expected failure inside a CLI command"
paths: src/library_catalog/cli/commands/*.py
---

Catch the specific failure and give the user enough context to correct it.

## Pattern

```python
try:
    records = read_catalog_file(path)
except CatalogFormatError as error:
    raise click.ClickException(f"{path}: {error}") from error
```

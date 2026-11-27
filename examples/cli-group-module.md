---
description: "Each CLI command group lives in a module with the same name"
when: "Adding a command group to the CLI"
paths: src/library_catalog/cli/commands/*.py
---

Define a top-level Click group in `commands/<group>.py` and attach its
subcommands in the same module. The entry point imports each group for registration.

## Why

A command group shown by `--help` points to the module that owns its commands.

## Pattern

```python
# src/library_catalog/cli/commands/books.py
@click.group()
def books() -> None:
    """Work with the library catalog."""
```

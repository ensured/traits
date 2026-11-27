---
description: "Modules obtain a module-level logger with logging.getLogger(__name__)"
when: "Adding logging to a Python module"
paths: src/library_catalog/**
---

Assign the logger to `logger` below the imports. Configure handlers and log
levels at the application entry point.

## Why

The module name identifies the source of the message and lets operators
configure one subsystem at a time.

## Pattern

```python
import logging

logger = logging.getLogger(__name__)


def note_catalog_loaded(book_count: int) -> None:
    logger.info("Loaded %d books", book_count)
```

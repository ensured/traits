---
description: "CLI tests invoke commands through Click's CliRunner"
when: "Testing a CLI command"
paths: tests/cli/**
---

Pass dependencies through `obj` when the command needs context. Assert on the
exit code and the caller-facing output written to the supplied stream.

## Pattern

```python
def test_count_reports_number_of_books(catalog_context):
    result = CliRunner().invoke(count_books, obj=catalog_context)
    assert result.exit_code == 0
    assert catalog_context.stdout.getvalue() == "3\n"
```

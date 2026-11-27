# Traits

Traits document recurring code patterns as short Markdown files. Contributors
and coding agents use them to follow project conventions and review changes.

## Install

Use Git credentials with read access to `ensured/traits`. In Claude Code
2.1.275 or later, run this in a session.

```text
/plugin install traits --marketplace ensured/traits
```

For OpenCode, run this from the project root.

```sh
npx skills add ensured/traits --agent opencode --skill '*'
```

- [Install from a local checkout or ZIP](docs/install.md)
- [Write and review traits](docs/workflow.md)
- [Trait file format](skills/trait-index/SPEC.md)
- [Examples](examples/README.md)
- [Build a release](docs/releasing.md)

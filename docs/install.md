# Install Traits

## Claude Code

From a source checkout or the extracted plugin ZIP, register the marketplace
and install the plugin.

```sh
claude plugin marketplace add "$PWD"
claude plugin install traits@traits
```

Start Claude Code in the project where you want to use Traits. For a single
session, run `claude --plugin-dir /path/to/traits` from that project. Use the
path to the checkout or extracted plugin.

For a standalone install, extract the skills ZIP into your project's
`.claude/skills/`, or copy all six directories from `skills/` there. Invoke
standalone skills without the `traits:` prefix.

## Direct use

Any editor can read and edit trait files. To generate the index directly, run
this from the target project root with Bash and `awk` installed.

```sh
/path/to/traits/skills/trait-index/generate.sh
```

The generator creates `traits/README.md` and installs `traits/SPEC.md` on
first use. Pass `--check-spec` to verify compatibility before editing. An
unmarked spec uses format 1. If the format differs, use a matching Traits
release or migrate the project traits and spec together.

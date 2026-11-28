# Install Traits

## Claude Code

Register the GitHub marketplace and install the plugin. Your Git client needs
read access to `ensured/traits`.

```sh
claude plugin marketplace add ensured/traits
claude plugin install traits@traits
```

From a source checkout or the extracted plugin ZIP, register the local
marketplace with `claude plugin marketplace add "$PWD"`.

Start Claude Code in the project where you want to use Traits. For a single
session, run `claude --plugin-dir /path/to/traits` from that project. Use the
path to the checkout or extracted plugin.

For a standalone install, extract the skills ZIP into your project's
`.claude/skills/`, or copy the skill directories from `skills/` there. Invoke
standalone skills without the `traits:` prefix.

## OpenCode

From the project root, install the skills with the
[Skills CLI](https://github.com/vercel-labs/skills). It requires Node.js
22.20 or later.

```sh
npx skills add ensured/traits --agent opencode --skill '*'
```

You can also extract `traits-skills-<version>.zip` into `.opencode/skills/`.
Download the ZIP from [GitHub Releases](https://github.com/ensured/traits/releases),
or copy the skill directories from a source checkout's `skills/` directory.
Keep `generate.sh` and `SPEC.md` alongside `trait-index/SKILL.md`.

Ask OpenCode to use `trait-index` to initialize or refresh your project's
trait index. In OpenCode V2, you can invoke the skill with `@trait-index`.

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

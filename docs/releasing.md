# Build a release

Run this from a source checkout with Python 3.

```sh
python3 scripts/package.py
```

The complete release appears in `dist/traits-<version>/`. It contains the
plugin, standalone skills, and source ZIPs. The version comes from
`.claude-plugin/plugin.json`. Extract the source ZIP to rebuild from the same
inputs.

Review `scripts/release-files.txt` when adding or removing public files. The
packager reads only the listed files, then puts all three bundles in place
together. An identical rebuild succeeds. To build changed content at the same
version, choose a fresh destination with `--output DIRECTORY`.

If the build checkout contains private history, start the public repository
from the source ZIP with fresh Git history.

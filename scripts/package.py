"""Build a complete release from the listed public source files."""

import argparse
import errno
import json
import re
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = Path("scripts/release-files.txt")
GENERATOR = Path("skills/trait-index/generate.sh")
PLUGIN_MANIFEST = Path(".claude-plugin/plugin.json")
SOURCE_ONLY = {Path(".gitignore"), Path("scripts/package.py"), INVENTORY}
NOTICES = {Path("LICENSE"), Path("NOTICE")}
REQUIRED = SOURCE_ONLY | {
    GENERATOR,
    GENERATOR.with_name("SPEC.md"),
    PLUGIN_MANIFEST,
    Path(".claude-plugin/marketplace.json"),
    Path("README.md"),
}


def read_source(path):
    source = ROOT / path
    if source.resolve() != source or not source.is_file():
        raise ValueError(f"Expected a regular source file at {path}")
    return source.read_bytes()


def read_public_files():
    inventory = read_source(INVENTORY)
    files = {}
    for name in inventory.decode("utf-8").splitlines():
        if not name:
            continue
        path = Path(name)
        if (
            path.is_absolute()
            or any(part.lower() in ("..", ".git") for part in path.parts)
            or path.parts[:1] == ("dist",)
            or "\\" in name
            or ":" in name
            or path in files
        ):
            raise ValueError(f"Invalid release inventory path {name!r}")
        content = inventory if path == INVENTORY else read_source(path)
        mode = 0o100755 if path == GENERATOR else 0o100644
        files[path] = (content, mode)

    missing = REQUIRED - files.keys()
    if missing:
        names = ", ".join(str(path) for path in sorted(missing))
        raise ValueError(f"Missing release inputs {names}")
    return files


def write_zip(destination, entries):
    with ZipFile(destination, "w") as archive:
        for name, (content, mode) in sorted(entries.items()):
            info = ZipInfo(name.as_posix())
            info.create_system = 3
            info.external_attr = mode << 16
            archive.writestr(info, content, ZIP_DEFLATED)


def publish_release(staged, destination):
    if not destination.exists() and not destination.is_symlink():
        try:
            staged.rename(destination)
            return
        except OSError as error:
            if error.errno not in (errno.EEXIST, errno.ENOTEMPTY):
                raise

    if destination.is_dir() and not destination.is_symlink():
        staged_files = {path.name: path for path in staged.iterdir()}
        existing = {path.name for path in destination.iterdir()}
        if existing == staged_files.keys():
            for name, source in staged_files.items():
                current = destination / name
                if current.is_symlink() or not current.is_file():
                    break
                if current.read_bytes() != source.read_bytes():
                    break
            else:
                return

    raise ValueError(
        f"Release {destination} already exists with different contents. "
        "Use a different output directory or release version."
    )


def build_release(output):
    files = read_public_files()
    version = json.loads(files[PLUGIN_MANIFEST][0])["version"]
    if not isinstance(version, str) or not re.fullmatch(r"[0-9][0-9A-Za-z.+-]*", version):
        raise ValueError("Plugin version must be safe to use in a filename")

    plugin = {path: data for path, data in files.items() if path not in SOURCE_ONLY}
    skills = {
        path.relative_to("skills"): data
        for path, data in files.items()
        if path.parts[:1] == ("skills",)
    }
    skills.update({path: files[path] for path in NOTICES if path in files})
    source = {Path("traits") / path: data for path, data in files.items()}

    destination = output / f"traits-{version}"
    output.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=output, prefix=".traits-release-") as directory:
        staged = Path(directory) / destination.name
        staged.mkdir()
        write_zip(staged / f"traits-plugin-{version}.zip", plugin)
        write_zip(staged / f"traits-skills-{version}.zip", skills)
        write_zip(staged / f"traits-source-{version}.zip", source)
        publish_release(staged, destination)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        "--source-output",
        type=Path,
        metavar="DIRECTORY",
        default=ROOT / "dist",
        help="publish all three bundles in DIRECTORY/traits-VERSION (default: dist)",
    )
    args = parser.parse_args()
    try:
        destination = build_release(args.output)
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"{error}\n")
    print(destination)


if __name__ == "__main__":
    main()

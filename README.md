# BRTrains3

A clean-sheet BRBuild project for the next generation of BRTrains.

## Status

This repository is initialised with a minimal BRBuild project and temporary smoke-test vehicle. The smoke-test vehicle exists only to validate the build pipeline and should be replaced as real vehicle conversion begins.

## Build

```bash
# Use Python 3.10+; BRBuild uses modern type-annotation syntax.
uv venv --python 3.14 .venv
uv pip install --python .venv/bin/python pillow pyyaml nml
.venv/bin/python build.py --log
```

The project-local launcher is the simplest path:

```bash
.venv/bin/python build.py --log
```

It can also be built from the BRBuild checkout:

```bash
cd /path/to/BRBuild
.venv/bin/python ./Run.py BRTrains3 --log
```

`BRBuild.yaml` keeps `grf_folder: src/grf` explicit because the BRBuild project finder does not apply the same default as the project-local launcher.

The launcher expects BRBuild as a sibling checkout (`../BRBuild`). Override the location with `BRBUILD_DIR`:

```bash
BRBUILD_DIR=/path/to/BRBuild .venv/bin/python build.py
```

Generated build data is written by BRBuild outside this source tree according to its current configuration.

## Layout

- `BRBuild.yaml` — project manifest
- `build.py` — BRBuild launcher
- `src/grf/GRF.yaml` — GRF metadata and parameters
- `src/vehicles/` — vehicle candidates
- `src/templates/` — project-specific NML templates when needed
- `docs/BRTrains3/` — working conversion and reference notes (outside this repository)

The authoritative project/build schema is the current BRBuild implementation. OpenTTE is the closest current reference project; BRMetro is a secondary prototype/concept reference, not a 1:1 template.

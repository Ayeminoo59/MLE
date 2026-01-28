# MLE

This repo is my **ML Engineering (MLOps-heavy)** learning workspace.

## Setup (Conda)

Create and activate the project environment:

```bash
cd /Users/ayeminoo/Desktop/MLE
conda env create -f environment.yml
conda activate mle
```

## Common commands

```bash
make format
make lint
make test
```

## Repo structure

- `src/`: Python package code (reusable)
- `tests/`: pytest tests
- `notebooks/`: experiments (keep light; move final code into `src/`)
- `scripts/`: runnable scripts (ETL/train/eval/etc.)

## Notes

- Prefer `mle` env over `base`.
- Keep changes reproducible (commands in this README, runnable tests).
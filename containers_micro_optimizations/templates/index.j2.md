% Containers Micro-optimizations

Containers in question: `tuple`, `list`, `dict`, `set`, `frozenset`.

Python version:
```
$ python --version
{{ run('python --version') }}
```

## What empty container is the most memory efficient?
### Empty container sizes
```
$ python -m containers_micro_optimizations.space.empty
```
{{ run('python -m containers_micro_optimizations.space.empty') }}

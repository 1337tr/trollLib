# trolllib

A tiny PyPI library template. It exposes **one function**, and that function
**runs automatically at import**.

## Install

```bash
pip install trolllib
```

## Use

```python
import trolllib          # prints: Hello, world!
trolllib.greet("you")    # prints: Hello, you!
```

## Develop

```bash
pip install -e ".[dev]"
pytest
```

## Publish

```bash
python -m build
python -m twine upload dist/*
```
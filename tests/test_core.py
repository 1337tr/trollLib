import importlib

from trolllib.core import greet


def test_greet_returns_message(capsys):
    assert greet("tester") == "Hello, tester!"
    assert capsys.readouterr().out.strip() == "Hello, tester!"


def test_greet_runs_on_import(capsys):
    import trolllib

    importlib.reload(trolllib)
    assert "Hello, world!" in capsys.readouterr().out
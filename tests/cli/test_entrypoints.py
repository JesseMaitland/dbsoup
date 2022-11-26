from dbsoup.cli import actions
from typing import Callable
import inspect


def test_all_entrypoints() -> None:
    for name, func in inspect.getmembers(actions, inspect.isfunction):
        args = inspect.getfullargspec(func)
        assert isinstance(func, Callable)
        assert args[0][0] == "cmd"

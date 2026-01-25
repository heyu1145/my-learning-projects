import builtins
import sys


class _cout:
    def __lshift__(self, other):
        print(other, end='')
        return self

    def __str__(_self):
        return ''

    def __repr__(_self):
        return ''


class _cin:
    def __rshift__(self, other):
        value = input()
        if isinstance(other, list):
            other[0] = value
        return self

    def __str__(_self):
        return ''

    def __repr__(_self) -> str:
        return ''

    def __enter__(_self) -> str:
        return input()

    def __exit__(_self) -> None:
        pass


class _endl:
    def __str__(_self):
        sys.stdout.flush()
        return '\n'

    def __repr__(self) -> str:
        sys.stdout.flush()
        return '\n'


class std:
    endl = _endl()
    cout = _cout()
    cin = _cin()


__all__ = ["std"]
builtins.std = std  # type: ignore

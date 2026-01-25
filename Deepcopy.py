import random
from typing import TypeVar, cast
from mytime import timer
import copy

T = TypeVar("T")


def Deepcopy(a: T) -> T:
    if isinstance(a, dict):
        if a == {}:
            return a
        return cast(T, {k: Deepcopy(v) for k, v in a.items()})
    elif isinstance(a, list):
        if a == []:
            return a
        return cast(T, [Deepcopy(v) for v in a])
    elif isinstance(a, set):
        if a == set():
            return a
        return cast(T, {Deepcopy(v) for v in a})
    elif isinstance(a, tuple):
        if a == ():
            return a
        return cast(T, tuple(Deepcopy(v) for v in a))
    else:
        return a


def makelist(n=0):
    result = []
    for _ in range(random.randint(50, 100)):
        if random.random() < 0.15 and n <= 30:
            a = makelist(n + 1)
        else:
            a = random.randint(1, 10000)
        result.append(a)
    return result


@timer
def getlist():
    return makelist()


lista = getlist()


@timer()
def copya(a):
    return Deepcopy(a)


copy1 = copya(lista)
copy1[1] = []
print(lista is copy1, lista == copy1)


@timer()
def copyb(a):
    return copy.deepcopy(a)


copy2 = copyb(lista)
copy2[1] = []
print(lista is copy2, lista == copy2)

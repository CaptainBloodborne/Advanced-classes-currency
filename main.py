from __future__ import annotations
from typing import Type
import functools


@functools.total_ordering
class Currency:
    """
    1 EUR = 2 USD = 100 RUB

    1 EUR = 2 USD    ;  1 EUR = 100 RUB
    1 USD = 0.5 EUR  ;  1 USD = 50 RUB
    1 RUB = 0.02 USD ;  1 RUB = 0.01 EUR
    """

    def __init__(self, value: float = 0):
        self.value = float(value)

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        return f"{cls.__dict__['rates'][str(other_cls())]} {other_cls()} for 1 {cls()}"

    def to_currency(self, other_cls: Type[Currency]) -> Currency:
        return other_cls(
            self.value * self.__class__.__dict__['rates'][str(other_cls())])

    def __add__(self: Currency, other: Currency) -> Currency:
        return self.__class__(
            other.to_currency(self.__class__).value + self.value
        )

    def __gt__(self: Currency, other: Currency) -> bool:
        return self.to_currency(other.__class__).value > other.value

    def __le__(self, other):
        return self.to_currency(other.__class__).value < other.value

    def __eq__(self, other):
        return self.to_currency(other.__class__).value == other.value


class Euro(Currency):
    rates = {
        'USD': 2.0,
        'RUB': 100.0,
        'EUR': 1.0
    }

    def __repr__(self):
        if self.value:
            return f"{self.value} EUR"
        else:
            return "EUR"


class Dollar(Currency):
    rates = {
        'EUR': 0.5,
        'RUB': 50.0,
        'USD': 1.0
    }

    def __repr__(self):
        if self.value:
            return f"{self.value} USD"
        else:
            return "USD"


class Rubble(Currency):
    rates = {
        'USD': 0.02,
        'EUR': 0.01,
        'RUB': 1.0
    }

    def __repr__(self):
        if self.value:
            return f"{self.value } RUB"
        else:
            return "RUB"


# print(dir(Currency))
# Currency.__name__ = 'Cur'
# print(Currency.__name__)
# print(Rubble()
#       )
print(
        f"Euro.course(Rubble)   ==> {Euro.course(Rubble)}\n",
        f"Dollar.course(Rubble) ==> {Dollar.course(Rubble)}\n",
        f"Rubble.course(Euro)   ==> {Rubble.course(Euro)}\n",
)

print(f"e = {Euro(100)}")
e = Euro(100)
r = Rubble(1000)
d = Dollar(2)
ee = Euro(1)
dollar25 = Dollar(25)
ruble100 = Rubble(1000)

print(e.__class__.__dict__)
print(f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n")
print(e + r)
print(dollar25 + ruble100)
print(e < r)
print(ee >= d)
abc = dollar25 + ruble100 + e
print(type(abc))
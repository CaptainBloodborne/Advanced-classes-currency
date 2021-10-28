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
        'USD': 2,
        'RUB': 100,
        'EUR': 1
    }

    def __repr__(self):
        if self.value:
            return f"{self.value} EUR"
        else:
            return "EUR"


class Dollar(Currency):
    rates = {
        'EUR': 0.5,
        'RUB': 50,
        'USD': 1
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
        'RUB': 1
    }

    def __repr__(self):
        if self.value:
            return f"{self.value } RUB"
        else:
            return "RUB"

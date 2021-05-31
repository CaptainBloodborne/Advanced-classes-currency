class Currency:
    """
    1 EUR = 2 USD = 100 RUB

    1 EUR = 2 USD    ;  1 EUR = 100 RUB
    1 USD = 0.5 EUR  ;  1 USD = 50 RUB
    1 RUB = 0.02 USD ;  1 RUB = 0.01 EUR
    """

    def __init__(self, value: int):
        pass

    @classmethod
    def course(cls, other_cls):
        raise NotImplementedError

    def to_currency(self, other_cls):
        raise NotImplementedError


class Euro(Currency):
    pass


class Dollar(Currency):
    pass


class Rubble(Currency):
    pass

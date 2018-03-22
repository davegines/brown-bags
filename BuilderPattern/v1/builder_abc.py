import abc
from BuilderPattern.v1.product import Product


class Builder(metaclass=abc.ABCMeta):
    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def build_part_a(self):
        pass

    @abc.abstractmethod
    def build_part_b(self):
        pass

    @abc.abstractmethod
    def build_part_c(self):
        pass

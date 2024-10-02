"""
Provides an numerical class for attributes to have an numerical description
"""
from typing import Union
from .descriptive_base import DescriptiveAttributeBase


class DescriptiveNumericalAttribute(DescriptiveAttributeBase):
    """
    On setting, checks that the value is a Python numerical type of int or float
    """

    def __init__(
        self,
        name: str,
        minvalue: Union[int, float, None] = None,
        maxvalue: Union[int, float, None] = None,
    ):
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        super().__init__(name=name)

    def validate(self, value) -> None:
        """
        validation method to be called on __set__ attribute
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected {value!r} to be an int or float")
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f"Expected {value!r} to be at least {self.minvalue!r}")
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f"Expected {value!r} to be no more than {self.maxvalue!r}")

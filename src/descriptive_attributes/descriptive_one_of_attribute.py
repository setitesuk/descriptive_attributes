"""
Provides an numerical class for attributes to have an numerical description
"""
from typing import Any
from .descriptive_base import DescriptiveAttributeBase


class DescriptiveOneOfAttribute(DescriptiveAttributeBase):
    """
    On setting, checks that the value is a Python numerical type of int or float
    """

    def __init__(
        self,
        name: str,
        *options: Any,
    ):
        self.options = options
        super().__init__(name=name)

    def validate(self, value) -> None:
        """
        validation method to be called on __set__ attribute
        """
        if value not in self.options:
            raise ValueError(f"Expected {value!r} to be one of {self.options!r}")

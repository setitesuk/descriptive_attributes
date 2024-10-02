"""
Provides an numerical class for attributes to have an numerical description
"""
from typing import Union, Callable
from .descriptive_base import DescriptiveAttributeBase


class DescriptiveStringAttribute(DescriptiveAttributeBase):
    """
    On setting, checks that the value is a Python type of string
    Optionally checks length against optional min and max sizes, and against a predicate function
    i.e. for checking password complexities
    """

    def __init__(
        self,
        name: str,
        minsize: Union[int, None] = None,
        maxsize: Union[int, None] = None,
        predicate: Union[Callable, None] = None,
    ):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate
        super().__init__(name=name)

    def validate(self, value) -> None:
        """
        validation method to be called on __set__ attribute
        """
        if not isinstance(value, str):
            raise TypeError(f"Expected {value!r} to be an str")
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(
                f"Expected {value!r} to be no smaller than {self.minsize!r}"
            )
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                f"Expected {value!r} to be no bigger than {self.maxsize!r}"
            )
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(f"Expected {self.predicate} to be true for {value!r}")

"""
Provides a base class for generating classes for attributes to have descriptions
"""
from typing import Any
from abc import abstractmethod


class DescriptiveAttributeBase:
    """
    To be used as a base class for Attributes that
    need a description of their get, set and delete methods

    This works by storing the attribute in a private variable on the instance,
    and accessing by the attribute name

    args:
        name (str) : a name string for the attribute

    """

    def __set_name__(self, owner: Any, name: str) -> None:
        self.public_name = name
        self.private_name = f"_{name}"

    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError(f"{name} must be a string")
        self.name = name

    def __get__(self, instance: Any, owner: Any) -> Any:
        value = getattr(instance, self.private_name)
        return value

    def __set__(self, instance: Any, value: Any) -> None:
        self.validate(value)
        setattr(instance, self.private_name, value)

    def __delete__(self, instance: Any) -> None:
        delattr(instance, self.private_name)

    @abstractmethod
    def validate(self, value):
        """validation method to be called on all __set__ attribute"""
        pass

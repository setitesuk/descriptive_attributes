"""
Provides an immutable class for attributes to have an immutable description
"""
from typing import Any
from .descriptive_base import DescriptiveAttributeBase


class DescriptiveImmutableAttribute(DescriptiveAttributeBase):
    """
    Declares that the attribute is immutable once set, raising an AttributeError if it should be changed
    """

    def __set__(self, instance: Any, value: Any):
        try:
            value = getattr(instance, self.private_name)
        except AttributeError:
            # if we get an AttributeError, the value has not been set, and we allow this once
            setattr(instance, self.private_name, value)
            return

        # if we got a value, we raise an AttributeError, as it should not be modified
        raise AttributeError(f"{self.public_name}'s value cannot be altered")

    def __delete__(self, *args):
        raise AttributeError(f"{self.public_name} cannot be deleted")

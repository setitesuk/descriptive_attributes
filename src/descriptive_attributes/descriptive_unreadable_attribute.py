"""
Provides an unreadable class for attributes to have an unreadable description
"""
from .descriptive_base import DescriptiveAttributeBase


class DescriptiveUnreadableAttribute(DescriptiveAttributeBase):
    """
    Declares that the attribute is not readable via the attribute name once set,
    raising an AttributeError

    This is for values that should be set and then only used internally to the object,
    where they can access directly with obj._<name>
    """

    def __get__(self, *args):
        raise AttributeError(f"{self.public_name} is not readable")

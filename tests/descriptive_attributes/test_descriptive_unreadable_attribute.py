import pytest

from src.descriptive_attributes.descriptive_unreadable_attribute import DescriptiveUnreadableAttribute


class MockClass:
    my_attr = DescriptiveUnreadableAttribute("my_attr")

    def __init__(self, attr_val=None):
        if attr_val is not None:
            self.my_attr = attr_val


class TestDeclarativeUnreadableAttribute():
    def test_instantiation_with_attr_val(self):
        my_test_class = MockClass(attr_val="test_attr")
        with pytest.raises(AttributeError):
            my_test_class.my_attr
        # assert that the value is accessible via the private attr name
        assert my_test_class._my_attr == "test_attr"

    def test_change_attr_val(self):
        my_test_class = MockClass(attr_val="test_attr")
        my_test_class.my_attr = "new_test_attr"
        with pytest.raises(AttributeError):
            my_test_class.my_attr
        # assert that the value is accessible via the private attr name
        assert my_test_class._my_attr == "new_test_attr"

    def test_delete_attr(self):
        my_test_class = MockClass(attr_val="test_attr")
        delattr(my_test_class, "my_attr")
        # assert that the value has been removed
        assert getattr(my_test_class, "_my_attr", None) is None


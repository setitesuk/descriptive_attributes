import pytest

from src.descriptive_attributes.descriptive_immutable_attribute import DescriptiveImmutableAttribute


class MockClass:
    my_attr = DescriptiveImmutableAttribute("my_attr")

    def __init__(self, attr_val=None):
        if attr_val is not None:
            self.my_attr = attr_val


class TestDeclarativeImmutableAttribute():
    def test_instantiation_with_attr_val(self):
        my_test_class = MockClass(attr_val="test_attr")
        assert my_test_class.my_attr == "test_attr"

    def test_change_attr_val(self):
        my_test_class = MockClass(attr_val="test_attr")
        with pytest.raises(AttributeError):
            my_test_class.my_attr = "new_test_attr"
        assert my_test_class.my_attr == "test_attr"

    def test_delete_attr(self):
        my_test_class = MockClass(attr_val="test_attr")
        with pytest.raises(AttributeError):
            my_test_class.__delattr__("my_attr")
        assert my_test_class.my_attr == "test_attr"

    def test_instantiation_with_no_attr_val(self):
        my_test_class = MockClass()
        with pytest.raises(AttributeError):
            my_test_class.my_attr

    def test_add_attr_val(self):
        my_test_class = MockClass()
        my_test_class.my_attr = "added_test_attr"
        assert my_test_class.my_attr == "added_test_attr"
        with pytest.raises(AttributeError):
            my_test_class.my_attr = "changing_test_attr"
        assert my_test_class.my_attr == "added_test_attr"


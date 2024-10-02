import pytest

from src.descriptive_attributes.descriptive_one_of_attribute import DescriptiveOneOfAttribute


class MockClass:
    my_attr = DescriptiveOneOfAttribute("my_attr")

    def __init__(self, attr_val=None):
        if attr_val is not None:
            self.my_attr = attr_val

class MockWithValueOptionsClass(MockClass):
    my_attr = DescriptiveOneOfAttribute("my_attr", "foo", 1, 1.3)

class TestDeclarativeNumericalAttribute():
    def test_instantiation_with_attr_val_no_options_declared(self):
        with pytest.raises(ValueError):
            MockClass(attr_val=123)

    def test_instantiation_with_attr_val_no_options_declared_no_value(self):
        my_test_class = MockClass()
        assert getattr(my_test_class, "my_attr", None) is None

    def test_instantiation_with_attr_val_no_options_declared_no_value_cannot_be_added(self):
        my_test_class = MockClass()
        assert getattr(my_test_class, "my_attr", None) is None
        with pytest.raises(ValueError):
            my_test_class.my_attr = "foo"

    def test_instantiate_attr_val_with_options(self):
        my_test_class = MockWithValueOptionsClass(attr_val="foo")
        assert my_test_class.my_attr == "foo"

    def test_change_attr_val_with_options(self):
        my_test_class = MockWithValueOptionsClass(attr_val="foo")
        my_test_class.my_attr = 1
        assert my_test_class.my_attr == 1

    def test_change_attr_val_with_options_not_allowed_option(self):
        my_test_class = MockWithValueOptionsClass(attr_val="foo")
        with pytest.raises(ValueError):
            my_test_class.my_attr = 123

    def test_change_attr_val_with_options_when_no_value_originally_set_but_allowed_option_given(self):
        my_test_class = MockWithValueOptionsClass()
        my_test_class.my_attr = 1.3
        assert my_test_class.my_attr == 1.3

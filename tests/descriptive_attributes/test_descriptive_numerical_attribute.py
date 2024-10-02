import pytest

from src.descriptive_attributes.descriptive_numerical_attribute import DescriptiveNumericalAttribute


class MockClass:
    my_attr = DescriptiveNumericalAttribute("my_attr")

    def __init__(self, attr_val=None):
        if attr_val is not None:
            self.my_attr = attr_val

class MockWithValueRestrictionsClass(MockClass):
    my_attr = DescriptiveNumericalAttribute("my_attr", minvalue=5, maxvalue=10,)

class TestDeclarativeNumericalAttribute():
    def test_instantiation_with_attr_val(self):
        my_test_class = MockClass(attr_val=123)
        assert my_test_class.my_attr == 123

    def test_change_attr_val(self):
        my_test_class = MockClass(attr_val=123)
        my_test_class.my_attr = 12.3
        assert my_test_class.my_attr == 12.3


    def test_change_with_no_attr_val(self):
        my_test_class = MockClass()
        my_test_class.my_attr = 12.3
        assert my_test_class.my_attr == 12.3

    def test_instantiation_with_string_attr_val(self):
        with pytest.raises(TypeError):
            MockClass(attr_val="string")

    def test_change_to_string_attr_val(self):
        my_test_class = MockClass(attr_val=123)
        with pytest.raises(TypeError):
            my_test_class.my_attr = "string"
        # original should be left unchanged
        assert my_test_class.my_attr == 123

    def test_change_to_string_no_orig_attr_val(self):
        my_test_class = MockClass()
        with pytest.raises(TypeError):
            my_test_class.my_attr = "string"
        # original should be left unchanged
        assert getattr(my_test_class, "my_attr", None) is None

    def test_instantiation_with_too_big_attr_val(self):
        with pytest.raises(ValueError):
            MockWithValueRestrictionsClass(attr_val=123)

    def test_instantiation_with_too_small_attr_val(self):
        with pytest.raises(ValueError):
            MockWithValueRestrictionsClass(attr_val=1)

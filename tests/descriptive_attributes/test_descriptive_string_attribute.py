import pytest

from src.descriptive_attributes.descriptive_string_attribute import DescriptiveStringAttribute


class MockClass:
    my_attr = DescriptiveStringAttribute("my_attr")

    def __init__(self, attr_val=None):
        if attr_val is not None:
            self.my_attr = attr_val

class MockWithSizeRestrictionsClass(MockClass):
    my_attr = DescriptiveStringAttribute("my_attr", minsize=5, maxsize=10,)

def my_predicate(value):
    return len(value) > 0

class MockWithPredicateRestrictionsClass(MockClass):
    my_attr = DescriptiveStringAttribute("my_attr", predicate=my_predicate)


class TestDeclarativeStringAttribute():
    def test_instantiation_with_attr_val(self):
        my_test_class = MockClass(attr_val="my_val")
        assert my_test_class.my_attr == "my_val"

    def test_change_attr_val(self):
        my_test_class = MockClass(attr_val="my_val")
        my_test_class.my_attr = "my_new_val"
        assert my_test_class.my_attr == "my_new_val"


    def test_change_with_no_attr_val(self):
        my_test_class = MockClass()
        my_test_class.my_attr = "my_new_val"
        assert my_test_class.my_attr == "my_new_val"

    def test_instantiation_with_number_attr_val(self):
        with pytest.raises(TypeError):
            MockClass(attr_val=123)

    def test_change_to_string_attr_val(self):
        my_test_class = MockClass(attr_val="string")
        with pytest.raises(TypeError):
            my_test_class.my_attr = 123
        # original should be left unchanged
        assert my_test_class.my_attr == "string"

    def test_change_to_string_no_orig_attr_val(self):
        my_test_class = MockClass()
        with pytest.raises(TypeError):
            my_test_class.my_attr = 123
        # original should be left unchanged
        assert getattr(my_test_class, "my_attr", None) is None

    def test_instantiation_with_value_too_small_attr_val(self):
        with pytest.raises(ValueError):
            MockWithSizeRestrictionsClass(attr_val="val")

    def test_instantiation_with_value_too_big_attr_val(self):
        with pytest.raises(ValueError):
            MockWithSizeRestrictionsClass(attr_val="valvalvalval")

    def test_instantiation_attr_val_passes_predicate(self):
        my_test_class = MockWithPredicateRestrictionsClass(attr_val="predicate_passes")
        assert my_test_class.my_attr == "predicate_passes"

    def test_instantiation_attr_val_fails_predicate(self):
        with pytest.raises(ValueError):
            MockWithPredicateRestrictionsClass(attr_val="")

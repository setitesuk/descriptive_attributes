# Descriptive Attributes

To improve code maintainability, it is good to add descriptors to attributes to enforce what data is allowed into them.

Currently, there is no enforcement and an attribute on an object can contain any python type (and typing does not enforce this at runtime).

To resolve this, import one of these types of descriptors and assign the attribute an instantiation of the class.

On modification of the value in the object, the descriptive_attribute class will trigger and constrain as required

```python
from descriptive_attributes.descriptive_numerical_attribute import DescriptiveNumericalAttribute

class MyClass:
  number_attribute = DescriptiveNumericalAttribute()

my_number_class = MyClass(1)
print(my_number_class.number_attribute) # Output: 1

my_non_number_class = MyClass("foo") # Output: ValueError("Expected foo to be an int or float")
```
There are classes for

* immutable_attributes: once the value has been added, it cannot be changed or deleted
* unreadable_attributes: once the value is set, it cannot be read externally, the object has access via a private attribute
* numerical_attributes: must be an int or float. Optionally can have limits
* string_attributes: must be a string. Optionally, can have length limits, and a function to resolve to True
* one_of_attributes: provide a list of options that value must match one of

This can help ensure at run time that data is as expected. This also improves the security of the code, by enforcing rules.

More can be defined using descriptive_base.DescriptiveAttributeBase as a base class, and then overriding the __get__, __set__, __delete__ and validate functions.
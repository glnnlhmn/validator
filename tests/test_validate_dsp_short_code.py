# test_short_code.py
from dataclasses import dataclass

import pytest

from my_validator.exception import InvalidDSPShortCode, InvalidDataType
from my_validator.validate import AttributeDescriptor
from my_validator.validate import validate_short_code


@dataclass()
class MyClass:
    short_code: str = AttributeDescriptor(validate_short_code)


def test_create_dsp():
    dsp = MyClass("Test")
    assert dsp.short_code == "Test"


def test_change_dsp_short_code():
    dsp = MyClass("Test")
    dsp.short_code = "MODE"
    assert dsp.short_code == "MODE"


def test_change_dsp_short_code_to_non_str():
    dsp = MyClass("Test")
    with pytest.raises(InvalidDataType, match='value must be a string'):
        dsp.short_code = 1


def test_change_dsp_short_code_to_short_str():
    dsp = MyClass("Test")
    with pytest.raises(InvalidDSPShortCode, match='length did not equal 4'):
        dsp.short_code = "ssn"


def test_change_dsp_short_code_to_long_str():
    dsp = MyClass("Test")
    with pytest.raises(InvalidDSPShortCode, match='length did not equal 4'):
        dsp.short_code = "shade"


def test_set_empty_dsp():
    dsp = MyClass("Test")
    dsp.short_code = ""
    assert dsp.short_code == ""


def test_create_empty_dsp():
    dsp = MyClass()
    assert isinstance(dsp.short_code, AttributeDescriptor)


def test_set_none_dsp():
    dsp = MyClass("Test")
    dsp.short_code = None
    assert dsp.short_code is None

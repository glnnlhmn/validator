# test_short_code.py
from dataclasses import dataclass

from my_validator.exception import InvalidDSPShortCode, InvalidDataType
from my_validator.validate import AttributeDescriptor
from my_validator.validate import validate_short_code


@dataclass()
class DSP:
    short_code: str = AttributeDescriptor(validate_short_code)


def test_create_dsp():
    dsp = DSP("Test")
    assert dsp.short_code == "Test"


def test_change_dsp_short_code():
    dsp = DSP("Test")
    dsp.short_code = "MODE"
    assert dsp.short_code == "MODE"


def test_change_dsp_short_code_to_non_str():
    dsp = DSP("Test")
    try:
        dsp.short_code = 1
    except InvalidDataType:
        assert True, f"Non string: Error handled"
    except:
        assert False, f"Non string: Unexpected error not handled"
    else:
        assert False, f"Non string: Error not raised"


def test_change_dsp_short_code_to_short_str():
    dsp = DSP("Test")
    try:
        dsp.short_code = "SUM"
    except InvalidDSPShortCode:
        assert True, f"String to short: Error handled"
    except:
        assert False, f"String to short: Unexpected error not handled"
    else:
        assert False, f"String to short: Error not raised"


def test_change_dsp_short_code_to_long_str():
    dsp = DSP("Test")
    try:
        dsp.short_code = "SHADE"
    except InvalidDSPShortCode:
        assert True, f"String to long: Error handled"
    except:
        assert False, f"String to long: Unexpected error not handled"
    else:
        assert False, f"String to long: Error not raised"


# def test_set_empty_dsp():
#     dsp = DSP("Test")
#     dsp.short_code = ""
#     assert dsp.short_code is None
#
#
# def test_create_empty_dsp():
#     dsp = DSP()
#     assert dsp.short_code is None

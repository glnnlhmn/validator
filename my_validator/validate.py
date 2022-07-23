# file:  validate.py

from my_validator.exception import InvalidDataType, InvalidDSPShortCode, NonPositiveInteger


class AttributeDescriptor:
    def __init__(self, validator=None):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if not instance: return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator:
            if not self.validator(value):
                raise ValueError(f"Invalid {self.name}: {value}")
        instance.__dict__[self.name] = value


def validate_short_code(short_code: str) -> str:
    if short_code is None:
        return None
    elif isinstance(short_code, str):
        if len(short_code) == 4:
            return short_code
        raise InvalidDSPShortCode("Length of DSP short code did not equal 4")
    else:
        raise InvalidDataType("DSP short code value must ba a string")


def validate_short_code(short_code: str) -> str:
    if short_code == '':
        return ''
    elif isinstance(short_code, str):
        if len(short_code) == 4:
            return short_code
        raise InvalidDSPShortCode("Length of DSP short code did not equal 4")
    else:
        raise InvalidDataType("DSP short code value must ba a string")


def validate_id(test_id: int) -> int:
    if isinstance(test_id, int):
        if test_id <= 0:
            raise NonPositiveInteger('Value must be greater than zero')
        else:
            return test_id
    else:
        raise InvalidDataType("id must be an integer")

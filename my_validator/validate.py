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
        """
        If the validator is not None, then call the validator function with the value, and if the validator function returns
        False, raise a ValueError exception

        :param instance: The instance of the class that the descriptor is being accessed from
        :param value: The value that is being assigned to the attribute
        """
        if self.validator:
            if not self.validator(value):
                raise ValueError(f"Invalid {self.name}: {value}")
        instance.__dict__[self.name] = value


def validate_short_code(short_code: str) -> bool:
    """
    This function validates that the short code is a string, and that it is 4 characters long,
    the length is zero, or is none.

    :param short_code: The short code of the DSP
    :type short_code: str
    :return: A boolean value
    """
    if isinstance(short_code, AttributeDescriptor) or\
            short_code == '' or short_code is None:
        return True
    elif isinstance(short_code, str):
        if len(short_code) == 4:
            return True
        raise InvalidDSPShortCode("Length of DSP short code length did not equal 4")
    else:
        raise InvalidDataType("DSP short code value must be a string")


def validate_id(test_id: int) -> int:
    if isinstance(test_id, int):
        if test_id <= 0:
            raise NonPositiveInteger('Value must be greater than zero')
        else:
            return test_id
    else:
        raise InvalidDataType("id must be an integer")

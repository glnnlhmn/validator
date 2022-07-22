# file:  descriptors.py
#  Ref: https://stackoverflow.com/questions/54488765/validating-input-when-mutating-a-dataclass ??

# from dataclasses import dataclass
from validator.exception import InvalidDataType, InvalidDSPShortCode


def validate_code_len(code: str) -> bool:
    #  print("<<   validate_code_len")
    if len(code) != 4:
        raise InvalidDSPShortCode("Length of DSP short code did not equal 4")
        return False
    return True


def validate_code_type(code: str) -> bool:
    #  print(F"<<  validate_code_type:: {type(code)}")
    if not isinstance(code, str):
        raise InvalidDataType("DSP short code value must ba a string")
        return False


class AttributeDescriptor:
    def __init__(self, type, validators=()):
        self.type = type
        self.validators = validators

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if not instance: return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError(f"{self.name!r} values must be of type {self.type!r}")
#       print("    SETTING ")
        all_valid = True
        for validator in self.validators:
            all_valid = all_valid and  validator(value)
        if all_valid:
            instance.__dict__[self.name] = value



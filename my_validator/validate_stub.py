from dataclasses import dataclass

from my_validator.validate import AttributeDescriptor, validate_short_code


@dataclass
class DSP:
    short_code: str = AttributeDescriptor(validate_short_code)


dsp = DSP("TTTT")

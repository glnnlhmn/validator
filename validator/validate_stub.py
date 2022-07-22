from dataclasses import dataclass

from validator.validate import AttributeDescriptor, validate_code_len, validate_code_type


@dataclass
class DSP:
    short_code: str = AttributeDescriptor(str, [validate_code_type])


dsp = DSP(2)
print(dsp.short_code)

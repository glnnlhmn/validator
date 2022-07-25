from dataclasses import dataclass

from my_validator.validate import AttributeDescriptor, validate_short_code


@dataclass
class DSP:
    short_code: str = AttributeDescriptor(validate_short_code)

    def __post_init__(self):
        if isinstance(self.short_code, AttributeDescriptor):
            self.short_code = None


dsp = DSP("aska")

print(f'DSP Short code: {dsp.short_code}')
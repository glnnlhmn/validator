from dataclasses import dataclass, is_dataclass, asdict, field

from my_validator.validate import AttributeDescriptor, validate_short_code


"""
Default values for all @dataclass parameters
@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, 
           kw_only=False, slots=False
"""


@dataclass(order=True)
class DSP:
    short_code: str = field(default=AttributeDescriptor(validate_short_code), repr=True)
    """
    I want to change to make this 
    
        short_code: str = AttributeDescriptor(validate_short_code)
        
    so I could use the field method and set parameters other then the default value
    
        short_code: str = field(default=AttributeDescriptor(validate_short_code), repr=True)
      
    """
    # time_stamp: datetime

    def __post_init__(self):
        if isinstance(self.short_code, AttributeDescriptor):
            self.short_code = None


def is_dataclass_instance(obj):
    return is_dataclass(obj) and not isinstance(obj, type)


dsp_str = 'gsdp'
dsp = DSP(dsp_str)

"""
Printing some stuff out just to see what we have
"""

print(f'Is dsp object a data class: {is_dataclass_instance(dsp)}')
print(f'Is dsp_str object a data class: {is_dataclass_instance(dsp_str)}\n')
print(f'DSP Short code: {dsp.short_code}\n')
print(f'Return object as a dictionary: {asdict(dsp)}\n')
print(f'print dsp repr: {repr(dsp)}\n')
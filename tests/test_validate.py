from validator.validate_stub import DSP
# import sys


def test_create_valid_dsp():
    # print(sys._getframe().f_code.co_name)
    dsp = DSP("Test")
    # print(f"    {dsp}  address={id(dsp)}")

#   pprint(dir(dsp))


def test_change_dsp_short_code():
    # print(sys._getframe().f_code.co_name)
    dsp = DSP("Test")
    # print(f"    ORG: {dsp}  address={id(dsp)}")
    dsp.short_code = "MODE"
    # print(f"    MOD: {dsp}  address={id(dsp)}")


def test_change_dsp_short_code_to_non_str():
    # print(sys._getframe().f_code.co_name)
    dsp = DSP("Test")
    # print(f"    {dsp} address={id(dsp)}")
    # print("      try:  dsp.short_code = 1")
    try:
        dsp.short_code = 1
    except Exception as e:
        # print(F"  Exception: {e.args}")
        return False


def test_change_dsp_short_code_to_short_str():
    # print(sys._getframe().f_code.co_name)
    dsp = DSP("Test")
    # print(f"    {dsp} address={id(dsp)}")
    # print("     try: dsp.short_code = SUM")
    try:
        dsp.short_code = "SUM"
    except Exception as e:
        # print(F"  Exception: {e.args}")
        return False

# OUTPUT:
#     try: dsp.short_code = SUM
#          SETTING
#          validate_code_len
#          Exception: ("'int' object is not callable",)  ?? Why?


def test_change_dsp_short_code_to_long_str():
    # print(sys._getframe().f_code.co_name)
    dsp = DSP("Test")
    # print(f"    {dsp} address={id(dsp)}")
    # print("     try  dsp.short_code = SHADE")
    try:
        dsp.short_code = "SHADE"
    except Exception as e:
        # print(F"  Exception: {e.args}")
        return False


def test_set_empty_dsp():
    # print(sys._getframe().f_code.co_name)
    dsp = DSP("Test")
    # print(f"    {dsp} address={id(dsp)}")
    # print("   try dsp.short_code = None")
    try:
        dsp.short_code = None
    except Exception as e:
        # print(F"  Exception: {e.args}")
        return False


def test_create_empty_dsp():
    # print(sys._getframe().f_code.co_name)
    # print(" try with empty code  dsp = DSP()")
    try:
        dsp = DSP()
    except Exception as e:
        # print(F"  Exception: {e.args}")
        return False


# test_create_valid_dsp()
# print('--------------------------\n')
# test_change_dsp_short_code()
# print('--------------------------\n')
# test_change_dsp_short_code_to_non_str()
# print('--------------------------\n')
# test_change_dsp_short_code_to_short_str()
# print('--------------------------\n')
# test_change_dsp_short_code_to_long_str()
# print('--------------------------\n')
# test_set_empty_dsp()
# print('--------------------------\n')
# test_create_empty_dsp()
# print('--------------------------\n')

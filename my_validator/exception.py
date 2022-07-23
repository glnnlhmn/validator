# exception.py
class Error(Exception):
    pass


class InvalidEmployeeStatus(Error):
    pass


class InvalidEmployeeStatusType(Error):
    pass


class InvalidDataType(Error):
    pass


class InvalidDSPShortCode(Error):
    pass


class InputStringToLong(Error):
    pass


class NonPositiveInteger(Error):
    pass

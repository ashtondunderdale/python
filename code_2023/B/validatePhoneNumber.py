import re

def validatePhoneNumber(phone_number):
    """validates a given phone number"""

    # pattern for the phone number
    pattern = r"^0?\d{5} \d{6}$"

    # checks if pattern = match
    if re.fullmatch(pattern, phone_number):
        return True
    return False

print(validatePhoneNumber("07482 847384"))
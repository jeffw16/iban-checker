#! /usr/bin/python3

# IBAN Checker

# Naive IBAN checker
# Modulo 97 operation naively
def naiveIbanChecker(iban: str) -> bool:
    iban = ''.join(iban.split()) # strip spaces
    iban_len = len(iban)
    if iban_len < 15 or iban_len > 34:
        # Invalid length, return false
        return False
    iban_arr = [ch for ch in (iban[4:] + iban[:4])]
    letters = [chr(x) for x in range(65, 65+26)]
    letter_mapping = {ch : ord(ch) - 55 for ch in letters}
    num_str = ''.join([str(letter_mapping[x]) if x in letter_mapping else x for x in iban_arr])
    return int(num_str) % 97 == 1

assert naiveIbanChecker('GB82 WEST 1234 5698 7654 32') == True
assert naiveIbanChecker('GB98 MIDL 0700 9312 3456 78') == True
assert naiveIbanChecker('DE91 1000 0000 0123 4567 89') == True
assert naiveIbanChecker('DE91 1000 0000 0123 4567 82') == False
assert naiveIbanChecker('DE91 1000 0000 0123 4567 49') == False

# Optimal IBAN checker
# Piecewise calculation of modulo 97
def fastIbanChecker(iban: str) -> bool:
    iban = ''.join(iban.split()) # strip spaces
    iban_len = len(iban)
    if iban_len < 15 or iban_len > 34:
        # Invalid length, return false
        return False
    iban_arr = [ch for ch in (iban[4:] + iban[:4])]
    letters = [chr(x) for x in range(65, 65+26)]
    letter_mapping = {ch : ord(ch) - 55 for ch in letters}
    num_str = ''.join([str(letter_mapping[x]) if x in letter_mapping else x for x in iban_arr])
    nine = num_str[:9]
    mod_result = -1
    num_str = num_str[9:]
    while len(nine) > 2:
        mod_result = int(nine) % 97
        nine = ('0' + str(mod_result) if mod_result < 10 else str(mod_result)) + num_str[:7]
        num_str = num_str[7:]
    return mod_result == 1

assert fastIbanChecker('GB82 WEST 1234 5698 7654 32') == True
assert fastIbanChecker('GB98 MIDL 0700 9312 3456 78') == True
assert fastIbanChecker('DE91 1000 0000 0123 4567 89') == True
assert fastIbanChecker('DE91 1000 0000 0123 4567 82') == False
assert fastIbanChecker('DE91 1000 0000 0123 4567 49') == False

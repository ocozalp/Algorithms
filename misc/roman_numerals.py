digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
digits_rev = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
              10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}


def roman_to_decimal(roman_number):
    total_value = 0
    max_digit = 0

    for c in reversed(roman_number):
        digit_value = digits[c]
        if digit_value >= max_digit:
            max_digit = digit_value
            total_value += digit_value
        else:
            total_value -= digit_value

    return total_value


def decimal_to_roman(decimal_number):
    result = ''
    for value in digits_rev:
        while decimal_number >= value:
            result += digits_rev[value]
            decimal_number -= value

    return result
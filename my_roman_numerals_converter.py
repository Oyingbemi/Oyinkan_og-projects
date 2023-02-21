def my_roman_numerals_converter(z):
    numbers = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    roman  = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    roman_numerals = ''
    while z != 0:
        if numbers[i] <= z:
           roman_numerals += roman[i]
           z = z - numbers[i]
        else:
            i -= 1 # i = i - 1
  
    return roman_numerals

# print(my_roman_numerals_converter(14))
# print(my_roman_numerals_converter(79))
# print(my_roman_numerals_converter(845))

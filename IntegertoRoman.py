# github repository- Lavanya-B

class Romans:

    def int_to_roman(self, num):
        integers = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        romans = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // integers[i]):
                roman_num += romans[i]
                num -= integers[i]
            i += 1
        return roman_num


def main():
    number = Romans()
    integer = int(input('Enter an integer number: '))
    result = number.int_to_roman(integer)
    return result


if __name__ == '__main__':
    print(main())
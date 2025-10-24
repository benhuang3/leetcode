class Solution:
    def intToRoman(self, num: int) -> str:
        roman_tuples = [ 
            (1000, "M"),
            (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
            (90, "XC"), (50, "L"), (40, "XL"), (10, "X"),
            (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        letters = []
        total = 0
        index = 0

        while total != num:
            if (total + roman_tuples[index][0] <= num):
                total += roman_tuples[index][0]
                letters.append(roman_tuples[index][1])
            else:
                index += 1
        return "".join(letters)


        
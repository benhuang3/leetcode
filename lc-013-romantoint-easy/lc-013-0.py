class Solution:
    def romanToInt(self, s: str) -> int:
        rti_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        combo_dict = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}

        i = 0
        res = 0

        while i < len(s):
            win = s[i:i+2]
            if win in combo_dict:
                res += combo_dict.get(win)
                i += 1
            else:
                res += rti_dict.get(win[0])
            i += 1

        return res


        
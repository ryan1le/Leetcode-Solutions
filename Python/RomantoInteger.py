class Solution(object):
    def romanToInt(self, s):
        result = 0;
        doubleroman = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        singleroman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for x in doubleroman:
            if (x in s):
                result += doubleroman[x]
                s = s.replace(x, "")
        for x in s:
            if (x in singleroman):
                result += singleroman[x]
        return result
        

                
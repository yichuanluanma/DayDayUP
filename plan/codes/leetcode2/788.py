# 旋转数字
class Solution:
    def rotatedDigits(self, N: int) -> int:
        mapping = {"0":"0", "1":"1","2":"5","5":"2","6":"9","8":"8","9":"6"}
        count = 0
        for i in range(1, N+1):
            tmp = ""
            flag = True
            for s in str(i):
                if s not in mapping.keys():
                    flag = False
                    break
                else:
                    tmp += mapping[s]
            if not flag:
                continue
            if tmp != str(i):
                count += 1
        return count
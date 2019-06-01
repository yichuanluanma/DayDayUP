# 字母大小写全排列

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [S]
        for i in range(len(S)):
            if S[i].isalpha():
                for st in res[:]:
                    l = list(st)
                    if S[i].islower():
                        l[i] = S[i].upper()
                        res.append(''.join(l))
                    else:
                        l[i] = S[i].lower()
                        res.append(''.join(l))
        return res
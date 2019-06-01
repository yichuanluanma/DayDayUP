# 最常见的单词
import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = re.split(r"""[!?',;. ]""", paragraph.lower())
        d = Counter(p)
        del d['']
        for i in banned:
            del d[i]
        return max(d,key=lambda x:d[x])
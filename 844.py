class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = ''
        for i in range(len(s)):
            if s[i] != '#':
                a += s[i]
            else:
                a = a[:-1]

        b = ''
        for i in range(len(t)):
            if t[i] != '#':
                b += t[i]
            else:
                b = b[:-1]

        return a == b  
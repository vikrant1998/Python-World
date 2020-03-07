class Solution(object):
    def isMatch(self, s, p):
        if not p:
            return not s

        s1, p1 = 0, 0
        track_s, track_p = 0, -1

        while s1 < len(s):
            if p1 < len(p) and (s[s1] == p[p1] or p[p1] == '?'):
                s1 += 1
                p1 += 1
            elif p1 < len(p) and (p[p1] == '*'):
                track_s = s1
                track_p = p1
                p1 += 1
            elif track_p >= 0:
                s1 = track_s + 1
                track_s += 1
                p1 = track_p
            else:
                return False

        while p1 < len(p) and p[p1] == '*': p1 += 1
        return p1 == len(p)

if __name__ == "__main__":
    s = "adceb"
    p = "*a*b"

    S = Solution()
    print(S.isMatch(s, p))
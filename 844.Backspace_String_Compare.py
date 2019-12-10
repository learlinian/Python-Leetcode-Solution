class Solution(object):
    def backspaceCompare(self, S, T):
        # modify S
        while '#' in S:
            index = S.index('#')
            if index > 0:
                S = S[:index-1] + S[index:]  # delete the item before '#'
            S = S.replace('#', '', 1)        # delete '#'

        # modify T
        while '#' in T:
            index = T.index('#')
            if index > 0:
                T = T[:index-1] + T[index:]
            T = T.replace('#', '', 1)
        if S == T:
            return True
        return False


if __name__ == '__main__':
    S = "oi###mupo##rszty#s#xu###bxx##dqc#gdjz"
    T = "oi###mu#ueo##pk#o##rsztu#y#s#xu###bxx##dqc#gz#djz"
    print(Solution().backspaceCompare(S, T))

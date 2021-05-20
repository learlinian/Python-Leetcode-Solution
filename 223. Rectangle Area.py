# too boring for this question.. Just ignore
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)

        if E > C or G < A or F > D or H < B:
            return area1 + area2

        colliding_x = 0
        if A <= E <= C:
            if G > C:
                colliding_x = C - E
            else:
                colliding_x = G - E
        elif A <= G <= C:
            if E < A:
                colliding_x = G - A
            else:
                colliding_x = G - E
        elif E <= A and G >= C:
            colliding_x = C - A
        elif E >= A and G <= C:
            colliding_x = G - E

        colliding_y = 0
        if B <= H <= D:
            if F < B:
                colliding_y = H - B
            else:
                colliding_y = H - F
        elif B <= F <= D:
            if H > D:
                colliding_y = D - F
            else:
                colliding_y = H - F

        return area1 + area2 - colliding_x * colliding_y


if __name__ == '__main__':
    print(Solution().computeArea(-2,-2,2,2,-3, -3,3,1))

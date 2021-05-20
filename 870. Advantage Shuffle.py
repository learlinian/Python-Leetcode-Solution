class Solution(object):
    def advantageCount(self, A, B):
        A_sort = sorted(A)
        B_sort = sorted(B)
        mapping = {}
        b_index = 0
        def save(key, val):
            if key in mapping.keys():
                mapping[key].append(val)
            else:
                mapping[key] = [val]
        for a_index in range(len(A)):
            if A_sort[a_index] <= B_sort[b_index]:
                save(B_sort[b_index - a_index - 1], A_sort[a_index])
                continue
            save(B_sort[b_index], A_sort[a_index])
            b_index += 1
        result = []
        for v in B:
            result.append(mapping[v][-1])
            _ = mapping[v].pop()
        return result

if __name__ == '__main__':
    A = [2, 0, 4, 1, 2]
    B = [1, 3, 0, 0, 2]
    print(Solution().advantageCount(A, B))
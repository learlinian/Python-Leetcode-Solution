# class Solution(object):
#     def minNumberOfFrogs(self, croakOfFrogs):
#         result = 0
#         seq = ['k', 'a', 'o', 'r', 'c']
#         croak_list = []
#         croak_list[:0] = croakOfFrogs
#         while croak_list:
#             start_len = len(croak_list)
#             i = len(croak_list) - 1
#             seq_i = 0
#             while i >= 0:
#                 if croak_list[i] == seq[seq_i]:
#                     del croak_list[i]
#                     if seq_i < 4:
#                         seq_i += 1
#                     else:
#                         seq_i = 0
#                 i -= 1
#             result += 1
#             if start_len == len(croak_list) or seq_i != 0:
#                 return -1
#             if not croak_list:
#                 break
#         return result

class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        mapping = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        record = [0] * 5
        result = 0
        for v in croakOfFrogs:
            record[mapping[v]] += 1
            if mapping[v] > 0 and record[mapping[v]] > max(record[:mapping[v]]):
                return -1
            if v == 'c' and record[0] - record[4] > result:
                result += 1
        if record[0] * 5 != sum(record):
            return -1
        return result


if __name__ == '__main__':
    croakOfFrogs = "cccrorakrcoakorakoak"
    print(Solution().minNumberOfFrogs(croakOfFrogs))

class Solution(object):
    def splitIntoFibonacci(self, S):
        max_num = len(S) // 3 + 1

        for first_len in range(1, max_num+1):
            first_num = int(S[:first_len])
            for second_len in range(1, max_num+1):
                second_num = int(S[first_len:first_len+second_len])
                fib = [first_num, second_num]
                accumulated_len = first_len + second_len
                while len(''.join([str(i) for i in fib])) < len(S):
                    print(fib, first_len, second_len)
                    next_len = len(str(first_num+second_num))
                    next_int = int(S[accumulated_len:accumulated_len+next_len])
                    print('next_int: ' + str(next_int))
                    if next_int != first_num + second_num or next_int > 2 ** 31 - 1:
                        break
                    fib.append(next_int)
                    if len(''.join([str(i) for i in fib])) == len(S):
                        return fib
                    first_num = second_num
                    second_num = next_int
                    accumulated_len += next_len
            if first_num == 0:
                break
        return []


if __name__ == '__main__':
    # s = "0123456579"
    # s = "011235813"
    # s = '112358130'
    # s = '17522'
    # s = '0123'
    s = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
    print(Solution().splitIntoFibonacci(s))
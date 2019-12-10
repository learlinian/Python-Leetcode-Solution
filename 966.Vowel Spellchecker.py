class Solution(object):
    def spellchecker(self, wordlist, queries):
        # make vowel character '*'
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c for c in word)

        words_perfect = set(wordlist)
        words_cap = {}  # word without capital character
        words_vow = {}  # word without vowel

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        # match query to the corresponding value
        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        s = []
        for query in queries:
            s.append(solve(query))

        return s


if __name__ == '__main__':
    wordlist = ["KiTe", "kite", "hare", "Hare"]
    queries = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
    print(Solution().spellchecker(wordlist, queries))

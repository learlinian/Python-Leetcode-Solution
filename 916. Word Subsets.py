class Solution:
    def wordSubsets(self, words1, words2):
        chars = {}
        for word in words2:
            temp_char = {}
            for c in word:
                try:
                    temp_char[c] += 1
                except:
                    temp_char[c] = 1
            for key in temp_char:
                try:
                    if chars[key] < temp_char[key]:
                        chars[key] = temp_char[key]
                except:
                    chars[key] = temp_char[key]

        result = []
        for word in words1:
            found = True
            for c in chars:
                if word.count(c) < chars[c]:
                    found = False
                    break
            if found:
                result.append(word)

        return result
def Solution(words):
    characters = set()
    for word in words:
        characters.update(word)

    characters = list(characters)
    records = []
    for i in range(len(words)-1):
        for j in range(min(len(words[i]), len(words[i+1]))):
            if words[i][j] == words[i+1][j]:
                continue
            records.append([words[i][j], words[i+1][j]])
            break

    last_character = []
    while last_character != characters:
        last_character = characters.copy()

        for record in records:
            first_index = characters.index(record[0])
            second_index = characters.index(record[1])
            if first_index > second_index:
                characters[first_index], characters[second_index] = characters[second_index], characters[first_index]

    return characters


if __name__ == '__main__':
    words = ["baa", "abcd", "abca", "cab", "cad"]
    print(Solution(words))

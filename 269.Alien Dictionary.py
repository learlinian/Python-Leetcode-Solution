def Solution(words):
    records = []
    for i in range(len(words)-1):
        for j in range(min(len(words[i]), len(words[i+1]))):
            if words[i][j] == words[i+1][j]:
                continue
            records.append([words[i][j], words[i+1][j]])
            break

    # invalid words
    if not records:
        return []

    characters = set()
    for word in words:
        characters.update(word)
    # characters = list(characters)
    
    # Bubble sorting -- time complexity: O(n^2)
    # last_character = []
    # while last_character != characters:
    #     last_character = characters.copy()
    #
    #     for record in records:
    #         first_index = characters.index(record[0])
    #         second_index = characters.index(record[1])
    #         if first_index > second_index:
    #             characters[first_index], characters[second_index] = characters[second_index], characters[first_index]

    # Topological sort -- time complexity: O(n^2)
    overlapped_char = set(i[0] for i in records)  # all characters appear in the words
    missing_key = (characters - overlapped_char).pop()
    all_char = len(characters)
    characters = [missing_key]

    while len(characters) < all_char:
        for record in records:
            if record[1] == characters[0]:
                characters = [record[0]] + characters

    return characters


if __name__ == '__main__':
    words = ["wrt","wrf","er","ett","rftt"]
    print(Solution(words))

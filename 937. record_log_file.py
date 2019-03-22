class Solution:
    def reorderLogFiles(self, List):
        output = [List[0]]      # initialize output with the first item in the input list
        last_length = 1         # reference to determine place to insert input list

        for item in List[1:]:
            temp = item.partition(' ')[2]   # filter our the identifier
            if temp[0].isdigit():           # if it is digit, then append directly and add 1 to last_length
                output.append(item)
                last_length += 1
            else:
                for i in range(len(output)):
                    if output[i].partition(' ')[2][0].isdigit():    # append if the reference string is already a digit
                        output.insert(i, item)
                    else:
                        # if the content of 2 strings are the same, then compare their identifiers
                        if temp == output[i].partition(' ')[2]:
                            min_length = min(len(item.partition(' ')[0]), len(output[i].partition(' ')[0]))
                            # if the identifiers are the same, then only insert if header;s length is shorter than 
                            # reference string 
                            if len(item.partition(' ')[0]) < len(output[i].partition(' ')[0]) and item.partition(' ')[0][:min_length] == output[i].partition(' ')[0][:min_length]:
                                output.insert(i, item)
                            else:
                                for j in range(min(len(item.partition(' ')[0]), len(output[i].partition(' ')[0]))):
                                    if item[j] < output[i][j]:
                                        output.insert(i, item)
                                        break
                                    if item[j] > output[i][j]:
                                        break
                        # if the content of the 2 strings are not the same
                        else:
                            output_temp = output[i].partition(' ')[2]
                            min_length = min(len(temp), len(output_temp))
                            if temp[:min_length] == output_temp[:min_length] and len(temp) < len(output_temp):
                                output.insert(i, item)
                            else:
                                for j in range(min(len(temp), len(output_temp))):
                                    if temp[j] < output_temp[j]:
                                        output.insert(i, item)
                                        break
                                    if temp[j] > output_temp[j]:
                                        break
                    # print('output: ' + str(output) + ' last_length: ' + str(last_length))
                    if len(output) == last_length + 1:
                        last_length += 1
                        break
                    # if the reference string is already the last one in output but there is still no reference string found
                    if i == len(output) - 1:
                        output.append(item)
                        last_length += 1
        return output


if __name__ == '__main__':
    s = ["j je", "b fjt", "7 zbr", "m le", "o 33"]
    print(Solution().reorderLogFiles(s))

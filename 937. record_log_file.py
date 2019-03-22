class Solution:
    def reorderLogFiles(self, List):
        output = [List[0]]
        last_length = 1

        for item in List[1:]:
            temp = item.partition(' ')[2]
            if temp[0].isdigit():
                output.append(item)
                last_length += 1
            else:
                for i in range(len(output)):
                    if output[i].partition(' ')[2][0].isdigit():
                        output.insert(i, item)
                    else:
                        if temp == output[i].partition(' ')[2]:
                            min_length = min(len(item.partition(' ')[0]), len(output[i].partition(' ')[0]))
                            if len(item.partition(' ')[0]) < len(output[i].partition(' ')[0]) and item.partition(' ')[0][:min_length] == output[i].partition(' ')[0][:min_length]:
                                output.insert(i, item)
                            else:
                                for j in range(min(len(item.partition(' ')[0]), len(output[i].partition(' ')[0]))):
                                    if item[j] < output[i][j]:
                                        output.insert(i, item)
                                        break
                                    if item[j] > output[i][j]:
                                        break
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
                    if i == len(output) - 1:
                        output.append(item)
                        last_length += 1
        return output

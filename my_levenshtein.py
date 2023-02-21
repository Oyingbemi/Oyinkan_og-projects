def my_levenshtein(string_1, string_2):
    if len(string_1) != len(string_2):
        return -1
    else:
        distance = 0
        for i in range(len(string_1)):
            if string_1[i] != string_2[i]:
                distance += 1
        return distance


# print(my_leveshtein("GGACTGA","GGACTGA"))
# print(my_leveshtein("ACCAGGG","ACTATGG"))
# print(my_leveshtein("GGACGGATTCTG","AGG"))
# print(my_leveshtein("",""))

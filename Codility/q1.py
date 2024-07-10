def solutions(S):
    temp_set = set()
    for element in S:
        if element in temp_set:
            return element
        else:
            temp_set.add(element)
    return ""


test_case = solutions("cdc")
print(test_case)

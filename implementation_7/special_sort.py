def SpecialSort(association_list):
    """
    takes in an association list and sorts it by values and if two values are the same, sort by key
    """
    return sorted(association_list, key=lambda x: [x[1], x[0]])


association_list = [[2, 2], [1, 10], [5, 4], [1, 4]]
print(SpecialSort(association_list))

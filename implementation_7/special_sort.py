def SpecialSort(association_list):
    """
    takes in an association list and sorts it by values and if two values are the same, sort by key
    Time Complexity: O(n*log(n))
    Space Complexity: O(1)
    """
    association_list.sort(key=lambda x: [x[1], x[0]])
    return association_list


association_list = [[2, 2], [1, 10], [5, 4], [1, 4]]
print(SpecialSort(association_list))

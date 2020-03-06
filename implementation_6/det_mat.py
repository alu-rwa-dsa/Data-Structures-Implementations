import math


def detMat(m):
    """
    detMat function takes in a n*n matrix and return the value of its determinant
    TimeComplexity: O(n^2)
    SpaceComplexity: O(n))
    """
    ans = 0
    # base case for the 1 * 1 matrix
    if len(m) == 1:
        return m[0]
    # base case when m is a 2*2 matrix
    if len(m) == 2:
        # return the determinant of a 2*2 matrix
        return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
    else:
        # loop through the elements of the first row
        for i in range(len(m)):
            # new_m holds all the values for the determinant of m[i]
            new_m = []
            for j in range(1, len(m)):
                new_m.append(m[j][0:i] + m[j][i + 1:])
            ans += math.pow(-1, i) * m[0][i] * detMat(new_m)
    return ans



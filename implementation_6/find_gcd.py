def gcd(a, b):
    """
    gcd takes in two numbers a, b and returns the greatest common divisor
    TimeComplexity: O(b/2)
    SpaceComplexity: O(1)
    """
    # base case when a = 0 or b = 0
    if (a == 0) or (b == 0):
        # return the max value between a and b
        return max(a, b)
    # call the gcd give a = b and b = a % b
    return gcd(b, a % b)


# def gcd_2(a, b):
#     if a == b:
#         return a
#     elif a > b:
#         return gcd_2(a - b, b)
#     else:
#         return gcd_2(a, b - a)

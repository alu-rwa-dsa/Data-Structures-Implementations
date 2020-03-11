def conver_to_string(n):
    string = "0123456789"
    if n < 10:
        return string[n]
    else:
        return conver_to_string(n // 10) + string[n % 10]


f = conver_to_string(12345)
print(f, type(f))

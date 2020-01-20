# import the need library to calc the time and space complexity and plot it
from matplotlib import pyplot
from time import perf_counter
from memory_profiler import memory_usage
import random


# sort an array in ascending Order
def sort_arr(arr):
    return arr.sort()


# get the max value from an array of integers
def max_arr(arr):
    return max(arr)


# transform letters of a string to lower case
def lower_case(word):
    return word.lower()


def plotTime(f, minArg, maxArg):
    """
    Run timer and plot time complexity
    """
    len_input = []
    t = []
    for i in range(minArg, maxArg):
        if f == lower_case:
            # string of capital As of length i
            l_input = "A" * i
        else:
            # randomize an array of length i with values from 0 to 100
            l_input = random.sample(range(100), i)
        # time start point
        start = perf_counter()
        # calling the function
        f(l_input)
        # time end point
        end = perf_counter()
        # appending the len of the input and time it took to run
        len_input.append(i)
        t.append((end - start) / 1000)
    return len_input, t


# def plotSpace():
#     """
#     Run memory_space test and plot space complexity
#     """
#     input_len = []
#     space = []
#     for i in range(1,100):
#         l_input = random.sample(range(100), i)
#         mem = profile.Profile(sort_arr(l_input))
#         print(mem)
#         input_len.append(i)
#         space.append(mem)
#
#     pyplot.plot(input_len, space, 'o')
#     pyplot.xlabel("List length")
#     pyplot.ylabel("Space in MB")
#     pyplot.show()


def size_million(f):
    """
    estimating the time if the input length is 1,000,000
    """
    if f == lower_case:
        l_input = "A" * 1000000
    else:
        l_input = random.sample(range(1000000), 1000000)
    start = perf_counter()
    f(l_input)
    end = perf_counter()
    return end - start


def main():
    # task 2; plot the time and space it takes a function to run an input of len 1: 100
    print('Analyzing Algorithms...')
    # calling the plotTime function and give it a function name, min, max values
    len_input, t = plotTime(sort_arr, 1, 100)
    # plot the output
    pyplot.plot(len_input, t, 'o')
    # title of the plot
    pyplot.title("Time Complexity of sort fun")
    # naming x axis
    pyplot.xlabel("List length")
    # naming y axis
    pyplot.ylabel("Time in (ms)")
    pyplot.show()

    len_input, t = plotTime(max_arr, 1, 100)
    pyplot.plot(len_input, t, 'o')
    pyplot.title("Time Complexity of max fun")
    pyplot.xlabel("List length")
    pyplot.ylabel("Time in (ms)")
    pyplot.show()

    len_input, t = plotTime(lower_case, 1, 100)
    pyplot.plot(len_input, t, 'o')
    pyplot.title("Time Complexity of Lower_case fun")
    pyplot.xlabel("List length")
    pyplot.ylabel("Time in (ms)")
    pyplot.show()

    # task 3; estimating the time it will take to execute input of length million
    print("Time to sort an array of length million= {} sec".format(size_million(sort_arr)))
    print("Time to find max number of an array of length million= {} sec".format(size_million(max_arr)))
    print("Time to lower a string length million= {} sec".format(size_million(lower_case)))


if __name__ == '__main__':
    main()

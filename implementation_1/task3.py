# Calc and plot space complexity of the sort, lower, max python functions
from matplotlib import pyplot
from memory_profiler import memory_usage
import random

# sort an array in ascending Order
def sort_arr():
    return l_input.sort()


# get the max value from an array of integers
def max_arr():
    return max(l_input)


# transform letters of a string to lower case
def lower_case():
    return l_input.lower()


def plotSpace(f, minArg, maxArg):
    """
    Run memory_space test and plot space complexity
    """
    global l_input
    input_ind = []
    space = []
    for i in range(minArg, maxArg):
        if f == lower_case:
            l_input = "A" * i
        else:
            l_input = random.sample(range(100), i)
        mem = memory_usage(f)
        input_ind.append(i)
        space.append(mem[-1])

    return input_ind, space


def main():
    # task 3; plot space it takes for a given function to execute given input of len 1: 100
    print('Analyzing Algorithms...')
    # calling the plotSpace function and give it a function name, min, max values
    len_input, t = plotSpace(sort_arr, 1, 100)
    # plot the output
    pyplot.plot(len_input, t, 'o')
    # title of the plot
    pyplot.title("Space Complexity of sort fun")
    # naming x axis
    pyplot.xlabel("List length")
    # naming y axis
    pyplot.ylabel("Space in (MB)")
    pyplot.show()

    len_input, t = plotSpace(max_arr, 1, 100)
    pyplot.plot(len_input, t, 'o')
    pyplot.title("Space Complexity of max fun")
    pyplot.xlabel("List length")
    pyplot.ylabel("Space in (MB)")
    pyplot.show()

    len_input, t = plotSpace(lower_case, 1, 100)
    pyplot.plot(len_input, t, 'o')
    pyplot.title("Space Complexity of Lower_case fun")
    pyplot.xlabel("List length")
    pyplot.ylabel("Space in (MB)")
    pyplot.show()


if __name__ == '__main__':
    main()

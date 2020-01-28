# just define main at the top and then call it

def main():
    caugh(3)
    printAhmed()

def caugh(n):
    for i in range(n):
        print(i)


def printAhmed():
    print("Ahmed Meshref")


if __name__ == "__main__":
    main()
def odd_even(a):
    if a % 2 == 0:
        print(str(a) + " is odd")
    else:
        print(str(a) + " is even")


if __name__ == '__main__':
    for x in range(10):
        odd_even(x)

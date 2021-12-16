
def print_fibo(limit):
    first = 1
    second = 1
    print(first, end = " ")
    print(second, end = " ")
    for i in range(limit):
        third = first + second
        print(third, end = " ")
        first = second
        second = third

if __name__ == "__main__":
    limit = 10
    print("fibonacci series is as ")
    print_fibo(limit)
    print()


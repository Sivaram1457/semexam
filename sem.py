n = int(input("enter the input"))

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    first = 1
    second = 2

    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third

    print(second)

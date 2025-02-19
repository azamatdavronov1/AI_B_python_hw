def factor(n):
    divider = 1
    while divider <= n:
        if n % divider == 0:
            print(divider, " is a factor of ", n)
        else:
            pass
        divider += 1


integer  = int(input("Enter a positive integer: "))
factor(integer)
n=int(input("Enter any number = "))
if(n==1):
        print(n,"is not a Prime Number")
else:
    for i in range(2, n):

        if n % i == 0:
            print(n, "is not a Prime Number")
            break
    else:
        print(n, "is a prime number")
n = int(input("Enter a number: "))
for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not a prime number") 
        break
if i == n - 1:
    print(f"{n} is a prime number")
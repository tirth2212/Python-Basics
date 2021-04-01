n = int(input("Enter Number of terms: "))
count = 0
i, j = 0, 1
if n <= 0:
    print("Enter a positive integer!!")
elif n == 1:
    print(j)
else:
    print("Here is the fibonacci series!")
    while count <= n:
        print(i)
        k = i + j
        i = j
        j = k
        count += 1

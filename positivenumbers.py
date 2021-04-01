list1 = []
n = int(input("Enter numbers of elements you want to enter in the list: "))
for i in range(0, n):
    element = int(input("Enter the elements: "))
    list1.append(element)
for m in list1:
    if m > 0:
        print(m)

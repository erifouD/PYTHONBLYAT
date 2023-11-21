TArray = [0, 4, 5, 6, 7, 3, 1, 4, 6, 7, 8, 1, 3, 4, 5, 6, 2, 4, 5]
b = int(input("Enter array manually?\n0 - no\n1 - yes\n"))
if(bool(b)):
    TArray.clear()
    Num = int(input("Enter array size: "))
    for i in range(Num):
        TArray.append(int(input(f"Enter  {i + 1} item of array: ")))

AlreadyChecked = []
for i in range(min(TArray), max(TArray)):
    if(not TArray.count(i) or i in AlreadyChecked): continue
    print("Value:", i, end = ", Indexes: ")
    for j in range(len(TArray)):
        if(TArray[j] == i):
            print(j, end = " ")
    print()
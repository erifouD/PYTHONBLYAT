#FIRST TASK================================
TArray = [0, 4, 5, 6, 7, 3, 1, 4, 6, 7, 8, 1, 3, 4, 5, 6, 2, 4, 5]
b = int(input("Enter array manually?\n0 - no\n1 - yes\n"))
if(b):
    TArray.clear()
    Num = int(input("Enter array size: "))
    for i in range(Num): TArray.append(int(input(f"Enter  {i + 1} item of array: ")))
Checked = []
for i in TArray:
    if((i in Checked) or TArray.count(i) < 2): continue
    Checked.append(i)
    print("Value:", i, end = ", Indexes: ")
    for j in range(len(TArray)): 
        if(TArray[j] == i): print(j, end = " ")
    print()

#SECOND TASK==============================
print()
TArray = [18, 5, 12, 21, 1, 3, 6, 9]
b = int(input("Enter array manually?\n0 - no\n1 - yes\n"))
if(b):
    TArray.clear()
    for i in range(8): TArray.append(int(input(f"Enter  {i + 1} item of array: ")))
for i in range(len(TArray)):
    if(TArray[i] < 15): TArray[i] *= 2
print(TArray)

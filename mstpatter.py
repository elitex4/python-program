a = int(input("Enter the number of rows you want in your pattern: "))

for i in range(1,a+1):
    for j in range(1,i+1):
        print(i*j, end=" ")
    print("\n")
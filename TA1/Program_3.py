print("Program 3A:")
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end="")
    print()
    
print(" ")
print("Program 3b:")

i = 1
while i <= 7:
    j = 0
    while j < i:
        if i % 2 != 0 or i == 6: 
            print(i, end='')
        j += 1
    if i % 2 != 0 or i == 6:
        print()
    i += 1




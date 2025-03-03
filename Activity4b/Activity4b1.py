A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'i', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'j', 'k'}

eInAnB = A & B
print("a. Elements in A and B:", eInAnB)

bNotInArC = B - (A | C)
print("b. Elements in B but not in A or C:", bNotInArC)
print("i. h, i, j, k:", {'h', 'i', 'j', 'k'})
print("ii. c, d, f:", {'c', 'd', 'f'})
print("iii. b, c, h:", {'b', 'c', 'h'})
print("iv. d, f:", {'d', 'f'})
print("v. c:", {'c'})
print("vi. l, m, o:", {'l', 'm', 'o'})

# Pascle Triangle

# c = (c * (row - column)) // column


n = 5
a = []
for i in range(1, n+1):

    c = 1
    b = []
    for j in range(1, i+1):

        #print(" ", c, end=" ")
        b.append(c)
        c = c*(i-j) // j

    # print()
    a.append(b)
print(a)

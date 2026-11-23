matrix=[
    [0,0,5],
    [0,0,0],
    [2,0,0]
]
print("sparse matrix:")
for row in matrix:
    print(row)
print("non-zero elements:")
for i in range(3):
    for j in range(3):
        if matrix[i][j] !=0:
            print(i,j,matrix[i][j])    
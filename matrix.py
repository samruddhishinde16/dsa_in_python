matrix=[
    [0,0,3],
    [0,0,0],
    [5,0,0]
]
zero=0
non_zero=0
for row in matrix:
    for element in row:
        if element==0:
            zero +=1
        else:
            non_zero +=1
print("zero elements=",zero)  
print("non-zero elements=",non_zero)  
if zero > non_zero:
    print("matrix is a spare matrix")
else:
    print("matrix is not a spare matrix")       

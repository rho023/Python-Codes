mat1=[
   [1,2,3],
   [4,5,6],
   [7,8,9]
]
mat2=[
    [10,11],
    [12,13],
    [14,15]
]
print(''' Matrix 1:     Matrix 2:
  [1,2,3]       [10,11]
  [4,5,6]       [12,13]
  [7,8,9]       [14,15]
     ''')
n=int(input("Enter the number of rows in first matrix: "))
m=int(input("Enter the number column in second matrix: "))
mat=[
    [0,0],
    [0,0],
    [0,0]
]
for i in range(n):
    for j in range(m):
         sum=0
         for k in range(n):
            sum=sum+int(mat1[i][k])*int(mat2[k][j])
         mat[i][j]=sum
print("The multiplied matrix is as follows:")
for row in mat:
    print(row)
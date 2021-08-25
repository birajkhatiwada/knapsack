import numpy as np

vals = [0,2,2,4,5,3]
wts = [0,3,1,3,4,2]
capacity = 7

#creating the table
width, height = capacity + 1, len(vals)
table = [[0 for i in range(width)] for j in range(height)]

#populate the table 
for row in range(height):
    for column in range(width):
        if(wts[row]<= column):
            # print(row, column)
            table[row][column] = max(vals[row]+table[row-1][column-wts[row]], table[row-1][column])

        else:
            table[row][column] = table[row-1][column]
    

#to print the table like table
list_as_array = np.array(table)
print(list_as_array)



#bactracking and finding the optimal path
row, column = height-1, capacity
arr=[]

while row != 0 and column != 0:
    print(table[row][column])
    if(table[row][column]!=table[row-1][column]):
        arr.append(row)
        column = column-wts[row]
    row = row-1

print(arr)
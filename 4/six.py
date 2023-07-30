rows = 4
cols = 3
result = [[col + rows*row for col in range(1, cols+1)] for row in range(rows)]
print(result)
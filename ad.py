def transpose(X):
  result = [[0,0,0],
         [0,0,0]]

  # iterate through rows
  for i in range(len(X)+1):
     # iterate through columns
     for j in range(len(X[0])+1):
         result[j][i] = X[i][j]

  for r in result:
     print(r)

#max-sum.py

def find_max(grid, n): #assuming nxn grid
    #initialize L, R, A, each with n rows, with n columns, each with initial value -inf
    L = [[float('inf') for j in range(n)] for i in range(n)]
    R = [[float('inf') for j in range(n)] for i in range(n)]
    A = [[float('inf') for j in range(n)] for i in range(n)]

    #initialize first row (you can only go right)
    A[0][0] = grid[0][0]
    for j in range(1,n):
        A[0][j] = A[0][j-1] + grid[0][j]

    #Iterate through rows 1->n-1
    #First compute L and R for the given row using the following recurrenes
    #L[i][j] = max(A[i-1][j], L[i][j-1]) + grid[i][j]
    #R[i][j] = max(A[i-1][j], R[i][j+1]) + grid[i][j]      
    #Then compute A using the following recurrence
    #A[i][j] = max(A[i-1][j], L[i][j-1] R[i][j+1]) + grid[i][j]
    for i in range(1, n):
        #Compute L for current row
        L[i][0] = A[i-1][0] + grid[i][0] #Case 1: On left edge of grid
        for j in range(1,n): #Case 2: Anywhere else
            L[i][j] = max(A[i-1][j], L[i][j-1]) + grid[i][j]

        #Compute R for current Row
        R[i][n-1] = A[i-1][n-1] + grid[i][n-1] #Case 1: On right edge of grid
        for j in range(n-2, 0, -1): #Case 2: Anywhere else, traverse from right to left
            R[i][j] = max(A[i-1][j], R[i][j+1]) + grid[i][j]

        #Compute A for current Row using L and R
        #3 Cases, left edge, right edge, anywhere else
        A[i][0] = max(A[i-1][0], R[i][1]) + grid[i][0] #Case 1: left edge, no left side
        A[i][n-1] = max(A[i-1][n-1], L[i][n-2]) + grid[i][n-1] #Case 2: right edge, no right side
        for j in range(1,n-1): #Case 3: Anywhere else
            A[i][j] = max(A[i-1][j], L[i][j-1], R[i][j+1]) + grid[i][j]

    print("A = " + str(A))

    return A[n-1][n-1] #return solution in bottom right index

if __name__ == "__main__":
    grid1 = [[3, 5, 7],
            [-4, 15, 4],
            [4, 3, 1]]
    #solution should be 3+5+7+4+15+3+1=38
    print("The maximum of grid1 is: " + str(find_max(grid1, 3)))

    grid2 = [[1, 2, 3, 4],
             [4, 3, 2, -5],
             [-1, -1, -1, -1],
             [10, 5, -27, 3]]
    #solution should be 1+2+3+2+3+4++(-1)+(-1)+(-1)+(-1)+3 = 14
    print("The maximum of grid2 is: " + str(find_max(grid2, 4)))
    
            
        
        

    

    
        
        
    
    

import numpy as np

def gauss_elimination(a_matrix,b_matrix):
    
    #Adding some contingencies to prrevent future problems
    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("Error: Square matrix not given!")
        return
        
    if b_matrix[1]> 1 or b_matrix.shape[0] != a_matrix.shape[0]:
        print("Error: Constant vector incorrectly sized")
        return
    
    #Initialization of necessary variables
    n=len(b_matrix)
    m=n-1
    i=0
    j=i-1
    x=np.zeros(n)
    new_line='\n'
    
    #Create our augmented matrix through NumPy's Concatenate feature
    augmented_matrix=np.concatenate((a_matrix,b_matrix),axis=1,dtype=float)
    print(f"The initial augmented matrix is:{new_line}{augmented_matrix}")
    print("Solving for hte upper-triangular matrix")
    
    #Applying Gauss Elimination
    while i<n:
        if augmented_matrix[i][i] ==0.0:
            print("Divide by zero error") 
            return                           #Fail-safe to eliminate divide by zero error!
        
        for j in range(i+1,n):
            scaling_factor=augmented_matrix[j][i]/augmented_matrix[i][i]
            augmented_matrix[j]=augmented_matrix[j]-(scaling_factor * augmented_matrix[i])
            print(augmented_matrix)           #Not needed, but nice to visualize the process
            
        i=i+1
        
    # Backwards Substitution
    x[m]=augmented_matrix[m][n]/augmented_matrix[m][m]
    
    for k in range(n-2,-1,-1):
        
        x[k]=augmented_matrix[k][n]
        
        for j in range(k+1,n):
            x[k]=x[k]/augmented_matrix[k][k]
            
    #Displaying Solution
    print(f"The following x-vector matrix solves the above augmented matrix:")
    
    for answer in range(n):
        print(f"x{answer} is {x[answer]} ")
        

'''variable_matrix=np.array([[1,1,3], [0,1,3],[-1,3,0]])
constant_matrix=np.array([[1],[0.2],[5]])'''                    #checking for incorrect size of b_matrix
variable_matrix=np.array([[1,1], [0,1]])                        # #checking for 2*2 size matrix
constant_matrix=np.array([[1],[0.2]])

'''variable_matrix=np.array([[1,1], [0,1],[-1,3,0]])
constant_matrix=np.array([[1],[0.2],[5]])'''                     #checking for 3*3 size matrix

gauss_elimination(variable_matrix,constant_matrix)

 
       
        
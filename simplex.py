import numpy as np
from fractions import Fraction

'''Input format:
m n
A(row-wise)
b(single line)
c(single line)
y/n 
B(if y, else ignore this line)
z

For the LP
max c^Tx + z
s.t. Ax=b, x>=0 
(and basis B if provided)
'''


def restrict(A,B):
    #restricts A to the columns in B
    new=[]
    for i in A:
        new.append([i[j] for j in (B-1)])
    return np.array(new)

def restrict_vector(c,B):
    #restricts c to the columns in B
    return np.array([c[i] for i in (B-1)])
    

m,n=map(int, input().split())

A=[]
for i in range(m):
    A.append(list(map(float, input().split(" "))))
A=np.array(A)

b=list(map(float, input().split(" ")))
b=np.array(b).T

c=list(map(float, input().split(" ")))
c=np.array(c).T

maybe = input()
if maybe=="y":
    B=list(map(int, input().split(" ")))
    B=np.array(B)
else:
    B=np.array([i for i in range(1,n+1)])

z=float(input())



def canonical_form(A,b,c,z,B):
    A_B = restrict(A,B)
    A_B_inv = np.linalg.inv(A_B)
    A_B_inv_T = np.transpose(A_B_inv)

    A_bar = A_B_inv @ A
    b_bar = A_B_inv @ b

    y= A_B_inv_T @ restrict_vector(c,B)
    c_bar = c.T - y.T @ A
    z_bar = z + y.T @ b 
    print("Current basis: B=",B)
    print(f"A_B_inv = \n{A_B_inv+Fraction()}")
    print("\nCurrent canonical form is:")
    print(f"max {c_bar+Fraction()}x + {z_bar+Fraction()}" )
    print("s.t. ")
    print(f"{A_bar+Fraction()}x = {b_bar+Fraction()}^T")
    print("x >= 0\n")
    return A_bar,b_bar,c_bar,y,z_bar
    
def simplex(A,b,c,z,B,m,n):
    iter=1
    while True:
        print(f"Iteration {iter}:")
        A,b,c,y,z = canonical_form(A,b,c,z,B)
        if np.all(c <= 0):
            print("\nOptimal solution found:")
            x=np.zeros(n)
            x[B-1]=b
            print("Certificate: y^T= ",y.T+Fraction())
            print("Objective value =", z+Fraction())
            return x,B #the optimal solution
        else:
            k=0
            for i in range(len(c)):  
                if c[i]>0:
                    k=i
                    break
            for i in range(m):
                if A[i][k]>0:
                    break
            else:
                x=np.zeros(n)
                x[B-1]=b
                d=np.zeros(n)
                j=0
                for i in B-1:
                    d[i]=-A[j][k] if A[j][k]!=0.0 else 0.0
                    j+=1
                d[k]=1
                print(f"Certificate: use x_{k+1}=t and use x(t)={x}^T + t{d}^T to prove unboundedness")
                return "Unbounded",B
            
            t,i = min([(b[i]/A[i][k],i) for i in range(m) if A[i][k]>0])
            l=B[i]
            B=np.sort(np.array([j if j!=l else (k+1) for j in B]))
            iter+=1

def phase_1(A,b):
    c_new=np.zeros(n+m)
    c_new[n:]=-1
    
    B=np.array([i for i in range(n+1,n+m+1)])
    
    I_m = np.identity(m)
    
    A_new=np.concatenate((A,I_m),axis=1)
        
    print("Original LP is:")
    print(f"max {c+Fraction()}x + {z+Fraction()}" )
    print("s.t.")
    print(f"{A+Fraction()}x = {b+Fraction()}^T")
    print("x >= 0")
    print("\n")
    
    print("Auxilary LP is:")
    print(f"max {c_new+Fraction()}x + {0+Fraction()}" )
    print("s.t.")
    print(f"{A_new+Fraction()}x = {b+Fraction()}^T")
    print("x >= 0")
    print("\n")
    
    print("Phase I:\n")
    
    result = simplex(A_new,b,c_new,0,B,m,m+n)
    for i in result[1]:
        if i>n:
            print("\nPhase I failed. LP is infeasible.")
            return "Infeasible",B
    else:
        print(f"\nPhase 1 completed sucessfully. Basis B = {result[1]}\n\nPhase II:\n")
        phase_2_result=simplex(A,b,c,z,result[1],m,n)
        return phase_2_result
        


if maybe=="n":
    result = phase_1(A,b)
    print(f"Final result: x={result[0]}, B={result[1]}")
else:
    print("Original LP is:")
    print(f"max {c+Fraction()}x + {z+Fraction()}" )
    print("s.t.")
    print(f"{A+Fraction()}x = {b+Fraction()}^T")
    print("x >= 0")
    print("\n")
    result=simplex(A,b,c,z,B,m,n)
    print(f"Final result: x={result[0]}, B={result[1]}")

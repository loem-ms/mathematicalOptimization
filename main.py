import numpy as np

def selectNindex(x,n_variable,x_N):
  pos_exist = 0
  for i in range(n_variable):
    if x[i]>0:
      pos_exist = 1
      return i,x_N[i]
    else:
      continue
  return -1

def selectBindex(x,y,n_constrain,x_B):
  res = x/y
  print(res)
  min_index = 0
  for i in range(n_constrain):
    if (res[i]<res[min_index]):
      min_index = i
    else:
      continue

  return min_index,x_B[min_index]

def updateC(b,n,n_constrain,n_variable,c):
  cTB = np.zeros(n_constrain)
  cTN = np.zeros(n_variable)
  for idx,i in enumerate(b-1):
    cTB[idx] = c[i]
  for idx,i in enumerate(n-1):
    cTN[idx] = c[i]
  return cTB,cTN
  
def updateBN(b,n,n_constrain,n_variable,A):
  B = np.zeros((n_constrain,n_constrain))
  N = np.zeros((n_variable,n_constrain))
  AT = np.transpose(A)
  
  for idx,i in enumerate(b-1):
    B[idx] = AT[i]
  for idx,i in enumerate(n-1):
    N[idx] = AT[i]
  return np.transpose(B),np.transpose(N)

def nextStep(B,N,b,cB,cN,n_constrain):
  Binv = np.linalg.inv(B)
  nb = np.dot(Binv,b)
  nN = np.dot(Binv,N)
  nB = np.identity(n_constrain)
  ncN = (cN-np.dot(np.dot(cB,Binv),N))
  Z = np.dot(cB,np.dot(Binv,b))
  return nB,nN,nb,ncN,Z,(nb>=0)

def checkMoving(c_N,n_variable):
  pos_var = 0
  for i in range(n_variable):
    if c_N[i]>0:
      pos_var += 1
    else:
      pos_var += 0
  if pos_var > 0:
    return True
  else:
    return False

def getValue(idx,nb,allX,n_constrain,n_variable):
  r_idx = list(allX).index(idx)
  if (r_idx <= n_constrain-1):
    return nb[r_idx]
  else:
    return 0

def solve(n_variable,n_constrain,x_B,x_N,b,c,A):
  x = True
  i = 0
  c_B,c_N = updateC(x_B,x_N,n_constrain,n_variable,c)
  B,N = updateBN(x_B,x_N,n_constrain,n_variable,A)
  idx_n,x_n_idx = selectNindex(c_N,n_variable,x_N)
  while x and (i<10):
    i += 1
    idx_b,x_b_idx = selectBindex(b,N[:,idx_n],n_constrain,x_B)
    #print("choose non-base :#",idx_n, " at x",x_n_idx)
    #print("choose base     :#",idx_b, " at x",x_b_idx)
    print("Pivote: x",x_n_idx," & x",x_b_idx)
    x_B[idx_b] = x_n_idx
    x_N[idx_n] = x_b_idx
    print("x_B : ",x_B)
    print("x_N : ",x_N)
    #print("updating C ...")
    c_B,c_N = updateC(x_B,x_N,n_constrain,n_variable,c)
    #print("c_B:",c_B)
    #print("c_N:",c_N)
    #print("finished!")
    #print("updating B,N ...")
    B,N = updateBN(x_B,x_N,n_constrain,n_variable,A)
    #print("B:")
    #print(B)
    #print("N:")
    #print(N)
    #print("finished!")
    #print("new tableaus ...")
    nB,nN,nb,nc_N,Z,feasible=nextStep(B,N,b,c_B,c_N,n_constrain)
    print("#",i,"##################")
    print(feasible)
    if feasible.all():
      print("Feasible")
    else:
      print("infeasible")
      break
    print("b    : ",nb)
    print("N    : ")
    print(nN)
    print("Z    : ",Z)
    print("c_N  : ",nc_N)

    print("########################")
    x = checkMoving(nc_N,n_variable)
    if x:
      idx_n,x_n_idx = selectNindex(nc_N,n_variable,x_N)
      print("Next>>")


  #-------- ANSWER -----------
  allX = np.concatenate((x_B,x_N))
  print("Optimum Feasible Solution: ")
  for i in range(n_variable+n_constrain):
    print("x",(i+1),"=",getValue(i+1,nb,allX,n_constrain,n_variable),end='|')
  print("\nOptimum Objective Value:")
  print(Z)
 
def main():
  #第５回 問題２（a）
  n_variable = 2
  n_constrain = 2

  x_B = np.array([3,4])
  x_N = np.array([1,2])
  b = np.array([154,112])
  c = np.array([4,5,0,0])
  A = np.array([[14,11,1,0],[7,16,0,1]])
  solve(n_variable,n_constrain,x_B,x_N,b,c,A)

if __name__ == "__main__":
    main()
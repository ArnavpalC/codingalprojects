def fu1(n,m):
    return n*m

def fu2(n,m):
    mul=0
    for i  in range(1,n+1):
        mul += m
    return mul


#def fu3(n,m):
 #   sum=0
  #     for j in range(1,i+1):
   #         sum += 1
    #return sum



print(fu1(80140,10012))
print(fu2(8123400,10032))

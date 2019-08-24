#program takes few numbers has a input from user and prints top two elements 
exp=list(map(int, input().split())) 

exp.sort(reverse=True)         

j=0
k=0              

for i in range(1,len(exp)):     
    if exp[j]==exp[i]:
        k+=1

print(exp[j],exp[k+1])         
     

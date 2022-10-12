x=int(input())
arr=[0]*x
for i in range(x):
    arr[i]=int(input())
l,c=1,1
for i in range(x):
    if l < arr[i]: 
    	c+=1
    	l = arr[i]
print(c)  
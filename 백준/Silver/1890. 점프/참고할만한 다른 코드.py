n,*a=map(int,open(0).read().split())
b=[1]+[0]*n*n
for i in range(n):
 for j in range(n):
  k=i*n+j;d=a[k];e=b[k]
  if(d>0)*(e>0):
   if i+d<n:b[k+d*n]+=e
   if j+d<n:b[k+d]+=e
print(b[-2])
##https://www.acmicpc.net/source/54839290

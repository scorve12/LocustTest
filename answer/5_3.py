n = int(input())
chk2=[0,1,2]
chk3=[0,1,2,4,5]
dp2=[1 if i in chk2 else 0 for i in range(4)]
dp3=[1 if i in chk3 else 0 for i in range(9)]

for i in range(n-1):
  a2=dp2
  a3=dp3
  dp2=[0 for x in range(4)]
  dp3=[0 for x in range(9)]
  
  for j in chk2:
    for k in chk2:
      if j&~k==j:
        dp2[j]+=a2[k]
        dp2[j]%=1000000007
        
  for j in chk3:
    for k in chk3:
      if j&~k==j:
        dp3[j]+=a3[k]
        dp3[j]%=1000000007
        
print(sum(dp2)*sum(dp2)*sum(dp3)%1000000007)

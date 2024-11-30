prime=True
n=int(input("enter the limit"))

for i in range(2,n):
    prime = True
    for j in range(2,i):
      if i%j==0:
         prime=False
    if prime:
        print(i)




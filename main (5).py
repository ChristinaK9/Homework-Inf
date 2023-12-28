a = ()
n = 378
for i in range(2, n+1):
    k = 0
    for b in range(1, i+1):
        k += 1
    if k == 2:
      a = k + i
print (a)      
    


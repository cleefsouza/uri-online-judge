o = str(input())
x = []
for i in range(12):
    y = []
    for j in range(12):
        v = float(input())
        y.append(v)
    y = y[::-1]
    x.append(y)

if(o=="S"):
    s = []
    z = 0
    for i in range(12):        
        if(i<6):
            fim, ini = i, 0
        else:
            fim, ini = 11-i, 0
            
        s.append(x[i][ini:fim])
        z += sum(s[i])
        
    print("{:.1f}".format(z))
    
elif(o=="M"):
    s = []
    z = 0
    m = 0
    for i in range(12):        
        if(i<6):
            fim, ini = i, 0
        else:
            fim, ini = 11-i, 0
            
        s.append(x[i][ini:fim])
        z += sum(s[i])
        m +=len(s[i])
    print("{:.1f}".format(z/m))

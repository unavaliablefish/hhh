
a = input("")
def sp(a):
    r = []
    x=0
    for i in range(len(a)):
        if a[i].isdigit():
            x=x*10+int(a[i])
        else:
            r.append(str(x))
            r.append(a[i])
            x=0
    return r
print(sp(a))

)
    def total(r):
    x=0
    output = []
    for i in range(len(r)):
        if r[i] == '*' or r[i] == '-' or r[i] == '+':
            x=1
    if x==0:
        output.append(r[0])
    
    for i in range(len(r)):
        if r[i] == '*' or r[i] == '-' or r[i] == '+':
            for j in total(r[:i]):
                for k in total(r[i+1:]):
                    print(j,k)
                    n = str(eval(j+r[i]+k))
                    output.append(n)
    return output

                        
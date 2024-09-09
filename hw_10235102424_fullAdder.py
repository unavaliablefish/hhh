Carry3=0
a0=1
a1=1 
b0=1
b1=1
Carry2=a0&b0
Sum1=(a1^b1)^(Carry2)
Carry1=a1&b1
Sum2=a0^b0
Carry3=Carry1&Carry2
print('carry=', Carry3)
print('sum1=',Sum1)
print('sum2=',Sum2)


Carry3=0
a0=1
a1=0
b0=0
b1=1
Carry2=a0&b0
Sum1=(a1^b1)^(Carry2)
Carry1=a1&b1
Sum2=a0^b0
Carry3=Carry1&Carry2
print('carry=', Carry3)
print('sum1=',Sum1)
print('sum2=',Sum2)
num1=45
num2=46
print(num1 + num2)

x=-1 
y=1.11
z=1+5j
print(x,y,z)


#type conversion

c=int(y)
print(c)
d=float(x)
print(c,d)
#e=float(z).............TypeError: float() argument must be a string or a real number, not 'complex'
# print(z)
p='Python';e=3.10
e1=str(e)
print(p+' '+e1)

p1='python is easy'
# p2=float(p1)..............ValueError: could not convert string to float: 'python is easy'
# print(p2)

s='1018'
ps=float(s)
print(ps)
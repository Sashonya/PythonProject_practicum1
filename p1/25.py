a = input()
probel = a.find(" ")
x = int(a[:probel])
n = a[probel+1:]
probel2= n.find(" ")
y = int(n[:probel2])
n = int(n[probel2+1:])


b = x*n
c = y*n
d = c//100
f = c%100
e = b+d
print( e,"руб.", f"коп.")

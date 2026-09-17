
q = input("Введите кол-во дррузей и кол-во конфет через пробел: ")
probel = q.find(" ")
n = int(q[:probel])
m = int(q[probel+1:])
total = m//(n+1)
print(total)


n = input("Введите стоимость шоколадок через пробел: ")
razriv = n.find(' ')
a = int(n[:razriv])
b = int(n[razriv+1:])
total = a + b
print(total)


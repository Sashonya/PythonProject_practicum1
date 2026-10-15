ant = int(input())
bor = int(input())
vic = int(input())
if ant > bor and ant > vic:
    print('Антон старше всех')
elif bor > vic and bor > ant:
    print("Борис старше всех")
elif vic > bor and vic > ant:
    print('Виктор старше всех')
elif ant == bor and ant>vic:
    print('Антон и Борис старше Виктора')
elif bor == vic and bor>ant:
    print("Борис и Виктор старше Антона")
elif ant == vic and ant > bor:
    print('Антон и Виктор старше Бориса')
else: print('Они все одного возраста')


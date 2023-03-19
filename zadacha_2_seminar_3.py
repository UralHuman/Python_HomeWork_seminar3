q = int(input("Введите натуральное число n: "))

spisok = []

for i in range(1, q + 1):
    elem = int(input(f"Введте {i}-й элемент списка: "))
    spisok.append(elem)

spisok.sort()

n = int(input("Введите элемент списка: "))

spisok.append(n)
spisok.sort()
ind = spisok.index(n)
print(spisok[ind - 1])

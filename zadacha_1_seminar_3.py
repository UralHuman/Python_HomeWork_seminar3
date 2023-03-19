q = int(input("Введите натуральное число n: "))

spisok = []

for i in range(1, q + 1):
    elem = input(f"Введте {i}-й элемент списка: ")
    spisok.append(elem)

n = input("Введите элемент списка: ")

print(spisok.count(n))

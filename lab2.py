list1 = [2, 8, 8, 3, 5, 9, 4]
list2 = [2, 8, 0, 3, 6, 9, 5]
n = 0
while n < len(list1)-1:
    for el in list1:
        if el == list2[n]:
            print(f'Cовпадение {el}[{n}]')
            break
    n += 1
def func(b):
    if not b.isdigit():
        return list(map(lambda i: i * 2, b))[0]
    else:
        return list(map(lambda i: int(i) * 2, b))[0]
a = input('Введите:')
print(func(a))
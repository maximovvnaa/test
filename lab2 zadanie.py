list1 = [1, 2, 3, 4, 5, 123, 234, 222, 333]
list2 = list(filter(lambda x: sum(int(digit) for digit in str(x))%2 == 0, list1))
print(list2)
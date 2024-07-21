#Ввод количества элементов списка
countelements = int(input("Введи количество элементов:"))
elements = []
i = 1
while countelements != 0:
    element = input(f'Введи элемент {i}:')
    elements.append(element)
    countelements -=1
    i +=1

print(elements)
stringelements = input('Введите элементы 1го списка через , или ; или /:')

elements_first: list = (stringelements.replace(',', ' ').replace(';', ' ')
                  .replace('/', ' ').split())

stringelements = input('Введите элементы 2го списка через , или ; или /:')

elements_second: list = (stringelements.replace(',', ' ').replace(';', ' ')
                  .replace('/', ' ').split())


new_elements:list = []


for elem_first in elements_first:
    find = False
    for elem_second in elements_second:
        if elem_first == elem_second:
            find = True

    if not find:
        new_elements.append(elem_first)


print(new_elements)

stringelements = input('Введите элементы списка через , или ; или /:')

elements: list = (stringelements.replace(',', ' ').replace(';', ' ')
                  .replace('/', ' ').split())

indx = 0
unique_elements: list = []
for elem in elements:
    if elements.count(elem) == 1:
        unique_elements.append(elem)

print(unique_elements)

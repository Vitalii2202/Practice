"""
задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

d1 = {'apple': 10000,
      'facebook': 5000,
      'nike': 40000,
      'adidas': 3000,
      'puma': 2000,
      'lexus': 4000
}

d2 = {}
def list():
      my_str = []
      for k, v in d1.items():
          my_str.append(v)
      return my_str


def rezult_puz():
    massiv = list()
    for i in range(0, len(massiv) - 1):
        for j in range(0, len(massiv) - 1 - i):
            if massiv[j] < massiv[j + 1]:
                massiv[j], massiv[j + 1] = massiv[j + 1], massiv[j]
    return massiv



def slov():
    x = 0
    p = 0
    d2rez = {}
    massiv = rezult_puz()
    while x < 3:
        el = massiv[p]
        d2 = {list(d1.keys())[list(d1.values()).index(el)]: el}
        d2rez.update(d2)
        p += 1
        x += 1
    return d2rez

print(slov())
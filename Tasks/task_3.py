"""
Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
"""

class PlateStackClass:
    def __init__(self, max_size):
        self.elems = []
        self.max_size = max_size        #размер стопки

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка
        если размер стопки равен пороговому значению по создается новая
        стопка и туда кладется значение"""
        if len(self.elems[len(self.elems)-1]) < self.max_size:
            self.elems[len(self.elems)-1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        '''Берем тарелку из крайней стопки, если она пустая удаляем ее'''
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        '''Общее колличество тарелок'''
        elem_sum = 0
        for stack in self.elems:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        '''Колличество стоек'''
        return len(self.elems)


if __name__ == '__main__':
    plates = PlateStackClass(3)
    print(type(plates))
    plates.push_in('Plate1')
    print(plates)
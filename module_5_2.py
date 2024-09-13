class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors >= new_floor > 0:
            for i in range(new_floor):
                print(f'Этаж   {i + 1}')
        else:
            print('Такого этажа не существует"')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(f'Название: {str(h1)}, кол-во этажей: {len(h1)}')
print(f'Название: {str(h2)}, кол-во этажей: {len(h2)}')


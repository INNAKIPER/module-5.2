class House:
    def __init__(self, name, number_of_floors):
       self.name = name
       self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        print(f'Здание {self.name} имеет {self.number_of_floors} этажей. Поднимаемся на {new_floor}-й этаж')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'Вы ввели не верный этаж {new_floor}, такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)
            print(f'Этаж № {new_floor} мы прибыли на ваш этаж, выходите')

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'{self.number_of_floors}'



h1= House('ЖК "Эльбрус"', 10)
h2 = House('ЖК Акация', 20)

txt1 = "ЖК ЭЛЬБРУС"
txt2 = "ЖК АКАЦИЯ"
print(f'{txt1}',len(h1))
print(f'{txt2}',len(h2))
print(h1)
print(h2)









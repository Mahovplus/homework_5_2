class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor+1):
            if new_floor > self.numbers_of_floors:
                print("Такого этажа не существует")
                break
            print(int(i))

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numbers_of_floors}'

    def __len__(self):
        return self.numbers_of_floors





h_1 = House('ЖК Горьский', 10)
h_2 = House('ЖК Акация', 20)
print(h_1)
print(h_2)
print(len(h_1))
print(len(h_2))
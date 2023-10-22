class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        if self.__cpu is not None and self.__memory is not None:
            return f'Performing computations: ' + self.__cpu * (self.__memory // (self.memory // 2))
        return "No CPU or memory specified"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __str__(self):
        return f"COMPUTER: CPU: {self.__cpu}, MEMORY: {self.__memory}"


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 0 < sim_card_number <= len(self.sim_cards_list):
            print(f"Calling to a number: {call_to_number} - {self.sim_cards_list[sim_card_number - 1]}")

    def __str__(self):
        return f"PHONE: SIM CARDS: {self.sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
        self.__sim_cards_list = sim_cards_list

    def use_gps(self, location):
        print(f"Routing to location: {location}")

    def __str__(self):
        return f"SmartPhone: CPU = {self.cpu}, MEMORY = {self.memory}, SIM CARDS = {self.__sim_cards_list}"


computer = Computer('Intel i7', 16)
nokia = Phone(["Beeline", "Megacom"])
iphone14 = SmartPhone('A15 Bionic', 516, ["Beeline", "O!"])
redmi10 = SmartPhone('Snapdragon 678', 8, ["Megacom", "O!"])

print(computer)
print(nokia)
print(iphone14)
print(redmi10)
print("Computer 1 computations:", computer.make_computations())

iphone14.call(1, "+996 777 888 967")
iphone14.use_gps("127, Chuy Avenue")
print(f'Iphone 14 and Redmi 10 memory comparison: {iphone14 == redmi10}')
print(f'Iphone 14 better than Redmi 10 : {iphone14 > redmi10}')
print(f'Computer better than Redmi 10 : {redmi10 < computer}')
print(f'Iphone 14 and Computer memory comparison: {iphone14 != computer}')
print(f'Iphone 14 memory better than or equal to Redmi 10 memory: {iphone14 >= redmi10}')
print(f'Iphone 14 and Computer memory comparison : {iphone14 <= computer}')

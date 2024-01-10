#Steve
#23.01.10
#Dog class


class Dog:
    def __init__(self, name):
        self.name = name
        self.trick_list = []
    def get_name(self):
        return self.name
    def sit(self):
        print(f'{self.name} sits')
        self.trick_list.append('sits')
    def run(self):
        print(f'{self.name} run 100m to the front')
        self.trick_list.append('runs')
    def fight(self):
        print(f'{self.name} trip over other dog')
        self.trick_list.append('fights')

    def print_trick_list(self):
        if self.trick_list:
            print(f'{self.get_name} has performed following tricks: {self.trick_list}')
        else:
            print(f'{self.get_name} has not performed any trick')

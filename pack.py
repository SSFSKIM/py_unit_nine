from dog import Dog  # Importing the Dog class from the dog file

class Pack:
    def __init__(self, leader):
        self.members = [leader]
        self.leader_index = 0

    def get_leader_name(self):
        return self.members[self.leader_index].get_name()

    def add_member(self, new_member):
        self.members.append(new_member)

    def print_pack(self):
        print("The pack contains:")
        for member in self.members:
            print(f"\t{member.get_name()}")

    def new_leader(self, new_leader_index):
        if 0 <= new_leader_index < len(self.members) and new_leader_index != self.leader_index:
            old_leader_name = self.get_leader_name()
            self.leader_index = new_leader_index
            print(f"{self.members[new_leader_index].get_name()} deposes {old_leader_name} as the leader of the pack.")
        else:
            print("That is not a valid dog.")

        # Check if the leadership has changed
        print(f"The new leader is {self.get_leader_name()}.")

    def all_sit(self):
        for member in self.members:
            member.sit()

    def all_print_tricks(self):
        for member in self.members:
            member.print_trick_list()

    def __str__(self):
        return f"Pack with {len(self.members)} members, leader: {self.get_leader_name()}"


dog1 = Dog("Carl")
dog2 = Dog("Jordan")
dog3 = Dog("Fyodor")

pack = Pack(dog1)
pack.add_member(dog2)
pack.add_member(dog3)

print(pack)

pack.print_pack()


pack.all_sit()

pack.all_print_tricks()

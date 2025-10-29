class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self,name):
        self.name=name
        self.friends=[]

    def add_friend(self,friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def __repr__(self):
        return f"Person: ({self.name})"

class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people={}
    
    def add_person(self,name):
        if name not in self.people:
            self.people[name]=Person(name)

    def add_friendship(self,person1_name,person2_name):
        if person1_name not in self.people or person2_name not in self.people:
            print("Both people must already be in the network before being added as a friend.")
            return
        person1=self.people[person1_name]
        person2=self.people[person2_name]
        person1.add_firend(person2)
        person2.add_firend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names=[friend.name for friend in person.firends]
            print(f"{name}:{', '.join(friend_names) if friend_names else'No Friends'}")


# Test your code here
if __name__ == "__main__":
    network = SocialNetwork()
    network.add_person("Alice")
    network.add_person("Bob")
    network.add_person("Charlie")

    network.add_friendship("Alice", "Bob")
    network.add_friendship("Bob", "Charlie")

    print("\n--- Social Network Connections ---")
    network.print_network()
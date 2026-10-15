"""
Zoo/Farm Simulation Game (Object-Oriented Programming Demonstration)
-------------------------------------------------------------------
This script demonstrates core OOP principles:
1. Inheritance: Subclasses inherit from the base `Animal` class.
2. Encapsulation: Private attributes (using double underscores `__`) protect internal data.
3. Polymorphism: Subclasses override methods (`make_sound`, `eat`, `get_status`) uniquely.
"""

from abc import ABC, abstractmethod

# ==========================================
# 1. BASE CLASS (Abstraction & Encapsulation)
# ==========================================
class Animal(ABC):
    """
    Abstract base class representing a generic animal.
    Demonstrates encapsulation by keeping attributes protected/private.
    """
    def __init__(self, name: str, species: str, age: int):
        # Encapsulated attributes (private variables using name mangling)
        self.__name = name
        self.__species = species
        self.__age = age
        self.__hunger_level = 50  # Scale from 0 (starving) to 100 (full)

    # Getter methods (Controlled Access)
    @property
    def name(self) -> str:
        return self.__name

    @property
    def species(self) -> str:
        return self.__species

    @property
    def age(self) -> int:
        return self.__age

    @property
    def hunger_level(self) -> int:
        return self.__hunger_level

    # Setter method to modify hunger safely
    def feed_animal(self, amount: int = 25):
        self.__hunger_level = min(100, self.__hunger_level + amount)

    # Abstract methods: subclasses MUST implement these (Polymorphism)
    @abstractmethod
    def make_sound(self) -> str:
        pass

    @abstractmethod
    def eat(self) -> str:
        pass

    def get_status(self) -> str:
        """Returns a formatted string of the animal's status."""
        status = "Full 🟢" if self.__hunger_level > 70 else ("Hungry 🟡" if self.__hunger_level > 30 else "Starving 🔴")
        return f"[{self.__species}] {self.__name} (Age: {self.__age}) - Status: {status} (Hunger: {self.__hunger_level}/100)"


# ==========================================
# 2. SUBCLASSES (Inheritance & Polymorphism)
# ==========================================
class Lion(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, "Lion", age)

    def make_sound(self) -> str:
        return f"{self.name} the Lion roars: 'ROAR! 🦁'"

    def eat(self) -> str:
        self.feed_animal(30)
        return f"{self.name} devours a fresh chunk of meat. 🥩"


class Elephant(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, "Elephant", age)

    def make_sound(self) -> str:
        return f"{self.name} the Elephant trumpets: 'PAWOOO! 🐘'"

    def eat(self) -> str:
        self.feed_animal(40)
        return f"{self.name} munches happily on bales of hay and fresh grass. 🌾"


class Cow(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, "Cow", age)

    def make_sound(self) -> str:
        return f"{self.name} the Cow moos: 'MooOOo! 🐮'"

    def eat(self) -> str:
        self.feed_animal(35)
        return f"{self.name} grazes peacefully in the pasture. 🌿"


class Chicken(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, "Chicken", age)

    def make_sound(self) -> str:
        return f"{self.name} the Chicken clucks: 'Cluck-cluck! 🐔'"

    def eat(self) -> str:
        self.feed_animal(20)
        return f"{self.name} pecks hungrily at scattered seeds. 🌽"


# ==========================================
# 3. ZOO / FARM MANAGEMENT CLASS
# ==========================================
class Zoo:
    """
    Manages a collection of animals in the simulation.
    """
    def __init__(self, name: str):
        self.name = name
        self.animals = []  # Composition: Zoo has a list of Animal objects

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        print(f"\nSUCCESS: Added {animal.name} the {animal.species} to {self.name}!")

    def list_animals(self):
        if not self.animals:
            print(f"\n{self.name} is currently empty! No animals found.")
            return
        
        print(f"\n--- 📋 Residents of {self.name} ---")
        for index, animal in enumerate(self.animals, start=1):
            print(f"{index}. {animal.get_status()}")

    def feed_all_animals(self):
        if not self.animals:
            print(f"\nNo animals to feed in {self.name}.")
            return

        print(f"\n--- 🍖 Feeding Time at {self.name} ---")
        for animal in self.animals:
            print(animal.eat())

    def make_all_sounds(self):
        if not self.animals:
            print(f"\nThere are no animals to make noise in {self.name}.")
            return

        print(f"\n--- 📢 Choir of Sounds at {self.name} ---")
        for animal in self.animals:
            # Demonstrates Polymorphism: Same method call (`make_sound`) behaves differently per subclass
            print(animal.make_sound())


# ==========================================
# 4. CONSOLE USER INTERFACE (Menu-Driven)
# ==========================================
def main():
    # Initialize our Zoo/Farm
    my_zoo = Zoo("Green Valley Farm & Zoo")

    # Add some default animals for quick testing
    my_zoo.add_animal(Lion("Simba", 5))
    my_zoo.add_animal(Elephant("Dumbo", 10))
    my_zoo.add_animal(Cow("Bessie", 4))
    my_zoo.add_animal(Chicken("Clucky", 1))

    while True:
        print("\n========================================")
        print(f"   welcome to {my_zoo.name.upper()}!   ")
        print("========================================")
        print("1. Add a new animal")
        print("2. View all animals")
        print("3. Feed all animals")
        print("4. Hear animal sounds")
        print("5. Exit simulation")
        
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            print("\n--- Choose Animal Type ---")
            print("1. Lion")
            print("2. Elephant")
            print("3. Cow")
            print("4. Chicken")
            
            type_choice = input("Select animal type (1-4): ").strip()
            name = input("Enter animal's name: ").strip()
            
            try:
                age = int(input("Enter animal's age: ").strip())
                if age < 0:
                    print("Age cannot be negative.")
                    continue
            except ValueError:
                print("Invalid age. Please enter a valid number.")
                continue

            # Instantiate appropriate subclass based on user choice
            if type_choice == '1':
                new_animal = Lion(name, age)
            elif type_choice == '2':
                new_animal = Elephant(name, age)
            elif type_choice == '3':
                new_animal = Cow(name, age)
            elif type_choice == '4':
                new_animal = Chicken(name, age)
            else:
                print("Invalid animal type selection.")
                continue

            my_zoo.add_animal(new_animal)

        elif choice == '2':
            my_zoo.list_animals()

        elif choice == '3':
            my_zoo.feed_all_animals()

        elif choice == '4':
            my_zoo.make_all_sounds()

        elif choice == '5':
            print("\nThank you for visiting the simulation. Goodbye! 👋")
            break
        else:
            print("\nInvalid option! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
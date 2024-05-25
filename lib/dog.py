class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "Pug", "Pointer"]

    def __init__(self, name="", breed=""):
        self.name = name
        self._breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not 1 <= len(value) <= 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value.capitalize() not in self.approved_breeds:
            print("Breed must be in the list of approved breeds.")
        else:
            self._breed = value.capitalize()


my_dog = Dog(name="")

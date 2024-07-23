#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Mutt", breed="Mastiff"):
        self.name = name
        self.breed = breed
    
    def get_name(self):
        print("Retrieving name.")
        return self._name
    
    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name
    
    def get_breed(self):
        print("Retrieving breed.")
        return self._breed
    
    def set_breed(self, breed):
        if not isinstance(breed, str) or breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
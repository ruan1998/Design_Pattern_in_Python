from enum import Enum
from abc import ABC, abstractmethod


class Species(Enum):
    CAT = 1
    DOG = 2
    HAMSTER = 3

class Character(Enum):
    TAME = 1
    NORMAL = 2
    RESTLESS = 3

class Pet:

    def __init__(self, name, species, character):
        self.name = name 
        self.species = species
        self.character = character
    def __str__(self):
        return f"{self.name} is a {self.character} {self.species}"
    def __format__(self, indent):
        indent = int(indent) if indent else 0
        return f"{' '*indent}{self.__str__()}"
# OCP = open for extension, but closed modification        
class PetFilter:

    @staticmethod
    def by_species(pets, species):
        for pet in pets:
            if pet.species == species: yield pet
    @staticmethod
    def by_character(pets, character):
        for pet in pets:
            if pet.character == character: yield pet
    def by_species_and_character(self, pets, species, character):
        for pet in pets:
            if pet.character == character and pet.species == species:
                yield pet

# 2 -> 2 ** 2 - 1 = 3
# 3 -> 2 ** 3 - 1 = 7
# Specification
class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, pet):
        pass
    def __and__(self, spec):
        return AndSpecification(self, spec)

class SpeciesSpecification(Specification):
    def __init__(self, species):
        self.species = species
    def is_satisfied(self, pet):
        return pet.species == self.species

class CharacterSpecies(Specification):
    def __init__(self, character):
        self.character = character

    def is_satisfied(self, pet):
        return pet.character == self.character

class AndSpecification(Specification):
    def __init__(self, *specs):
        self.specs = specs

    def is_satisfied(self, pet):
        return all(map(
                lambda spec: spec.is_satisfied(pet), self.specs
            ))
        

class AdvancedFilter:
    def filter(self, pets, spec):
        for pet in pets:
            if spec.is_satisfied(pet):yield pet

if __name__ == "__main__":
    cat1 = Pet("布偶猫", Species.CAT, Character.TAME)
    cat2 = Pet("短毛猫", Species.CAT, Character.RESTLESS)
    dog = Pet("边境牧羊犬", Species.DOG, Character.RESTLESS)
    hamster = Pet("灰仓鼠", Species.HAMSTER, Character.NORMAL)

    pets = cat1, cat2, dog, hamster
    
    print("Original Fitler:")
    print("  Cat:")
    for pet in PetFilter.by_species(pets, Species.CAT):
        print(f"    {pet}")
    print("Advance Filter:")
    print("  Cat:")
    cat_spec = SpeciesSpecification(Species.CAT)
    af = AdvancedFilter()
    for pet in af.filter(pets, cat_spec):
        print(f"    {pet}")
    
    print("  Restless pets:")
    restless_spec = CharacterSpecies(Character.RESTLESS)
    for pet in af.filter(pets, restless_spec):
        print(f"    {pet}")
    
    print(" Restless cat:")
    restless_cat = AndSpecification(restless_spec, cat_spec)
    for pet in af.filter(pets, restless_cat):
        print(f"    {pet}")
    print(" Restless dog:")
    restless_dog = restless_spec & SpeciesSpecification(Species.DOG)
    for pet in af.filter(pets, restless_dog):
        print(f"{pet:4}")

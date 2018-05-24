import pandas as pd
import numpy as np

dogs = pd.read_csv("dog_data.csv")

def get_attribute(breed, attribute):
  if breed in dogs.breed.unique():
    if attribute in dogs.columns:
        return dogs[dogs["breed"] == breed][attribute]
    else:
        raise NameError('Attribute {} does not exist.'.format(attribute))
  else:
      raise NameError('Breed {} does not exist.'.format(breed))
  

def get_weight(breed):
    return get_attribute(breed, 'weight')
  
def get_tail_length(breed):
    return get_attribute(breed, 'tail_length')

def get_color(breed):
    return get_attribute(breed, 'color')

def get_age(breed):
    return get_attribute(breed, 'age')

def get_is_rescue(breed):
    return get_attribute(breed, 'is_rescue')

def get_likes_children(breed):
    return get_attribute(breed, 'likes_children')

def get_is_hypoallergenic(breed):
    return get_attribute(breed, "is_hypoallergenic")

def get_name(breed):
    return get_attribute(breed, "name")

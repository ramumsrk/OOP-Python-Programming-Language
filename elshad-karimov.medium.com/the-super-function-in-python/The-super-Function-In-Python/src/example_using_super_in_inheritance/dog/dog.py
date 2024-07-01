#! /usr/bin/python3.12

import example_using_super_in_inheritance.logging_configuration

import logging

from typing import Literal, Self    

from example_using_super_in_inheritance.animal.animal import Animal as Animal

class Dog(Animal):
  """A class representing a Dog"""
  # Instance creation
  def __new__(
    klass,
    *args,
    **kwargs
  ) -> Self:
    """Instance creation"""
    logging.debug(
      f'Creating a Dog instance'
    )
    return super().__new__(klass)
  # Instance initialization
  def __init__(
    self,
    dog_name: Literal[str]
  ) -> Literal[None]:
    """Initialize a Dog instance"""
    logging.debug(
      f'Initializing a dog instance'
    )
    self.__dog_name = dog_name
    return None
  # Getter or Accessor
  # Instance method
  # Return dog_name attribute of a Dog instance
  def get_dog_name(
    self,
    /  
  ) -> Literal[str]:
    """Return do_name attribute of a Dog instance"""
    return self.__dog_name
  # Instance method
  def sound(
    self,
    /
  ) -> Literal[str]:
    return F'{super().sound()} but a Dog barks'
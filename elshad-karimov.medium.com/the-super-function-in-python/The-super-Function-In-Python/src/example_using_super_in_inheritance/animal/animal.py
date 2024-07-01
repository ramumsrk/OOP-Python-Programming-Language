#! /usr/bin/python3.12

import logging

import example_using_super_in_inheritance.logging_configuration

from typing import Self, Literal

class Animal:
  """A class representing an Animal"""
  # Instance creation
  def __new__(
    klass,
    *args,
    **kwargs
  ) -> Self:
    """Instance creation"""
    return super().__new__(klass)
  # Instance initialization
  def __init__(
    self,
    *,
    animal_name: Literal[str]
  ) -> Literal[None]:
    """Instance initialization"""
    logging.debug(
      f'Animal constructor is called'
    )
    self.__animal_name = animal_name
    return None
  # Getter or Accessor
  # Instance method
  # Return animal_name attribute
  def get_animal_name(
    self,
    /
  ) -> Literal[str]:
    """Return animal_name attribute"""
    return self.__animal_name
  # Instance method
  # Noise made by an Animal instance
  def sound(
    self,
    /
  ) -> Literal[str]:
    """Noise made by an Animal instance"""
    return f'Animal makes sound'
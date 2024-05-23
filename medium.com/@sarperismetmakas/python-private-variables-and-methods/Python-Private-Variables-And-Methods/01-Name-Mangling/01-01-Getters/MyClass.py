#! /usr/bin/python3.12

from typing import Literal, Type

class MyClass:

  # Instance creation
  def __new__(klass, *args, **kwargs):
    return super().__new__(klass)
  
  # Instance initialization
  def __init__(self, /) -> Literal[None]:
    self.__private_variable = 42
    return None
  
  # Instance method
  def get_private_variable(self, /) -> Type[int]:
    return self.__private_variable
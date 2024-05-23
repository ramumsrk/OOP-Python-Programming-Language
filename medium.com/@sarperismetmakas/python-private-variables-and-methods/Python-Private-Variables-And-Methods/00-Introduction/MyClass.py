#! /usr/bin/python3.12

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=f'{Path(__file__).parent}/MyClass.log'
)

from typing import Literal

class MyClass:

  # Instance creation
  def __new__(klass, *args, **kwargs):
    return super().__new__(klass)
  
  # Instance initialization
  def __init__(self, /) -> Literal[None]:
    self.__private_variable = 42
    return None
  
  # Instance method
  def __private_method(self, /) -> Literal[None]:
    logging.debug(f'This is a private method')
    return None
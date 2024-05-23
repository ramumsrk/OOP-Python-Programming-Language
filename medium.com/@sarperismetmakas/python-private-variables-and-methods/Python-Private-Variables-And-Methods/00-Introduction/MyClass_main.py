#! /usr/bin/python3.12

from MyClass import MyClass

import logging

from pathlib import Path

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=F'{Path(__file__).parent}/MyClass_main.log'
)

if __name__ == '__main__':

  first_instance: MyClass = MyClass()

  logging.debug(F'{first_instance.__private_variable}')
  logging.debug(f'{first_instance.__private_method()}')
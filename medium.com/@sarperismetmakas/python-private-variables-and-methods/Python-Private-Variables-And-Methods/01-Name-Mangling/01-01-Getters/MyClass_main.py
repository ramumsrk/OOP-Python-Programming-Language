#! /usr/bin/python3.12

import logging

from pathlib import Path

from MyClass import MyClass

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=f'{Path(__file__).parent}/MyClass_main.log'
)

if __name__ == '__main__':

  first_instance: MyClass = MyClass()

  logging.debug(f'{first_instance.get_private_variable()=}')
  logging.debug(F'{first_instance._MyClass__private_variable=}')
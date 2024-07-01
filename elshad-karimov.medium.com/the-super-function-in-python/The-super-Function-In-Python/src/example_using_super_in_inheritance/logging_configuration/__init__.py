#! /usr/bin/python3.12

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format=f"%(asctime)s | %(name)s | %(                    levelname)s | %(message)s",
  datefmt='%A, %B %d, %Y %H:%M:%S %Z %z',
  filemode='at+',
  filename=f'{Path(__file__).parent.parent.parent.parent}/logs/the_super_function_in_python.log'
)
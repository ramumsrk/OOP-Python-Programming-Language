#! /usr/bin/python3.12

from typing import Literal

import pytest

from example_using_super_in_inheritance.dog.dog import Dog as Dog

@pytest.fixture
def get_dog_instance() -> Dog:
  return Dog(dog_name='Buddy')

# Test-function
def test_dog_name(get_dog_instance) -> Literal[None]:
  assert "Buddy" == get_dog_instance.get_dog_name()
  return None
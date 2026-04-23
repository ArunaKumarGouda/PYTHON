from typing import List, Tuple, Dict, Union

# Variable type hint
age : int = 20

# Function type hint
def greeting(name : str) -> str:
    return f"Hello, {name}!"

# Usage 
print(greeting("Aruna"))    # Output: Hello Aruna!

# List of integer
number : List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = {"Aruna", 20}

# Dictionary with string keys and integer values
score: Dict[str, int] = {"Himansu": 30, "Aruna": 20}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345  # Also valid

# Utils Meaning
"""It contains a collection of helper functions and utility classes that provide common functionality and are used across different parts of the project.
"""

import os
"""
'os' module provides a way to interact with the operating system and perform various tasks related to file and directory operations
"""
# ======================================================================================================================================================

from box.exceptions import BoxValueError
"""
from box.exceptions import BoxValueError is an import statement that allows you to use the BoxValueError 
exception class from the box.exceptions module. This class is typically used for handling errors and exceptions that are specific to the Box library.
"""
# ======================================================================================================================================================

import yaml

"""
The yaml module is commonly used for working with YAML (YAML Ain't Markup Language) data, 
which is a human-readable data serialization format often used for configuration files, data exchange, and more.

==> some common tasks you can perform using the yaml module:

- Parsing YAML: You can use the yaml.load() function to parse YAML data from a file or a string into Python data structures (e.g., dictionaries and lists).

- Serializing to YAML: The yaml.dump() function allows you to convert Python data structures into YAML-formatted strings, which can be written to 
  files or used for other purposes.

- Reading YAML from Files: You can open YAML files using Python's open() function and then use yaml.load() to parse the content.

"""
# ======================================================================================================================================================


from deeplearningpractice import logger
"""
from deeplearningpractice import logger is an import statement that allows you to access the 
logger class from a package named deeplearningpractice in this Python script.

"""
# ======================================================================================================================================================


import json
"""
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for both humans and machines to read and write. 
It is often used to represent structured data, making it a popular choice for data serialization and communication between different programming languages and systems. 
JSON data consists of key-value pairs and supports various data types, including objects, arrays, strings, numbers, booleans, and null values.

import json is an import statement that allows you to use the json module in your Python script. The json module provides functions 
for working with JSON (JavaScript Object Notation) data, which is a common data interchange format used for representing structured data.

Here are some common tasks you can perform using the json module:

Parsing JSON: You can use the json.loads() function to parse a JSON-formatted string into a Python data structure, typically a dictionary or a list.

Serializing to JSON: The json.dumps() function allows you to convert Python data structures (e.g., dictionaries and lists) into 
JSON-formatted strings, which can be saved to files, sent over networks, or used in various data exchange scenarios.

Reading JSON from Files: You can open JSON files using Python's open() function, read the content, and then use json.loads() to parse the JSON data.

Writing JSON to Files: After processing or modifying JSON data in your script, you can use json.dump() to write it back to a file in JSON format.
"""
# ======================================================================================================================================================

import joblib

"""
import joblib is an import statement that allows you to use the joblib module in your Python script. The joblib module is a library commonly used for 
efficiently saving and loading Python objects, particularly NumPy arrays and scikit-learn models.

Joblib is often used in machine learning and data science workflows when you need to persistently store complex Python objects, such as machine learning models, 
for later use. It provides features like compression and parallelism for improved efficiency when working with large data.

"""
# ======================================================================================================================================================

from ensure import ensure_annotations

"""
ensure_annotations Decorator: The ensure_annotations decorator is applied to a function, indicating that you want to enforce the specified type hints. 
When you decorate a function with @ensure_annotations, it checks whether the function's arguments and return value match the provided type hints.

Type Checking: If the types do not match, ensure_annotations raises a TypeError at runtime. This helps catch potential type-related errors 
early in development and ensures that your code adheres to the specified type hints.

In Python, you can add type hints to function arguments and return values using the : syntax. For example:

def add(a: int, b: int) -> int:
    return a + b

"""

"""
Decorator: In Decorators, functions are passed as an argument into another function and then called inside the wrapper function.

"""


# ======================================================================================================================================================

from box import ConfigBox

"""
A ConfigBox object is like a dictionary but allows you to access its values using dot notation (attribute-style access) rather than dictionary-style indexing. 
It is often used to store configuration settings for an application.

Example:
----------
config = ConfigBox({
    'app_name': 'MyApp',
    'api_key': 'my_api_key')}

print(f"Application Name: {config.app_name}")
print(f"API Key: {config.api_key}")

"""


# ======================================================================================================================================================

from pathlib import Path

"""
The pathlib module provides an object-oriented way to work with file and directory paths in a platform-independent manner. 
It simplifies common file and directory operations and makes your code more readable and robust.

Here are some common tasks you can perform using the Path class from the pathlib module:

1. Creating Paths

2. File and Directory Operations: The Path class provides methods for common file and directory operations, such as checking if a path exists, 
creating directories, deleting files, and more.

3. Path Manipulation: You can manipulate paths by joining, splitting, and resolving them, all while ensuring platform independence.


"""

# ======================================================================================================================================================

from typing import Any

"""
from typing import Any is an import statement that allows you to use the Any type hint from the typing module in your Python script. The Any type hint is used to 
indicate that a variable or function parameter can have any possible Python data type. It is often used when you want to explicitly convey that a value can be of 
any type, and type checking is not strict.

from typing import Any

def example_function(value: Any) -> Any: # This function can accept a value of any type as an argument
    return value


"""

# ======================================================================================================================================================

import base64

"""

"""

# ======================================================================================================================================================


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
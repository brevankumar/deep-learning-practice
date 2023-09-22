import os
import sys
"""
The import sys statement is used to import the sys module in Python. The sys module is a built-in module that provides access to various variables 
and functions that interact with the Python runtime environment and system-specific settings. It is particularly useful for command-line arguments, 
system-specific configuration, and interacting with the Python interpreter.

"""
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("deeplearningpracticeLogger")
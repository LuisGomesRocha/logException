import sys
import logging

def do_something():
    raise ValueError(":(")

# Create a logging instance
logger = logging.getLogger('my_application')
logger.setLevel(logging.INFO) # you can set this to be DEBUG, INFO, ERROR

# Assign a file-handler to that instance
fh = logging.FileHandler("file_dir.txt")
fh.setLevel(logging.INFO) # again, you can set this differently

# Format your logs (optional)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter) # This will set the format to the file handler

# Add the handler to your logging instance
logger.addHandler(fh)

try:
    do_something()
    
except ValueError as e:
    logger.exception(e) # Will send the e
    
    





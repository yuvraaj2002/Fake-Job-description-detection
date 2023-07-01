import logging
import os
from datetime import datetime


# Path of the log directory
logs_path = os.path.join(os.getcwd(), "Logs")

# Creation of directory to store the log files
os.makedirs(logs_path, exist_ok=True)

# Name of the log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Path of log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# Let's check if everthing is working fine
if __name__ == "__main__":
    logging.info("Logging is working")

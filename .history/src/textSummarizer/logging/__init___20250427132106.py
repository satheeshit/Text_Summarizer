import os
import sys
import logging

log_dir="logs"
logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_filepath=os.path.join(log_dir,"continuos_logs.log")
os.makedirs(log_dir,exist_ok=True)


import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="textSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/com/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/__init__.py",
]
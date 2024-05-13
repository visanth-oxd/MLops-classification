import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

ml_name = 'classifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{ml_name}/__init__.py",
    f"src/{ml_name}/components/__init__.py",
    f"src/{ml_name}/utils/__init__.py",
    f"src/{ml_name}/config/__init__.py",
    f"src/{ml_name}/config/config.py",
    f"src/{ml_name}/pipeline/__init__.py",
    f"src/{ml_name}/entity/__init__.py",
    f"src/{ml_name}/constants/__init__.py",
    "config/config.yml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "experiments/trials.ipynb",
    "templates/index.html"
  
]

for file in list_of_files:
    file = Path(file)
    filedir, filename = os.path.split(file)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")
        
    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file, "w") as f:
            f.write("")
            logging.info(f"Created empty file: {file}")
            
    else:
        logging.info(f"File {file} already exists")        

 

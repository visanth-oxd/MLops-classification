import os
from box import ConfigBox
from box.exceptions import BoxError
import yaml
from classifier import logger
import json
import joblib
from ensure import ensure_annotations

from pathlib import Path
from typing import Any
import base64




@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e    

@ensure_annotations
def create_directory(directory_path: list, verbose=True):
    for directory in directory_path:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {directory}")
            
            
@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"Data saveed at {path}")  
    
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        data = json.load(f)
        
    logger.info(f"Data loaded from {path}") 
    return ConfigBox(data)


@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(data, path)
    logger.info(f"Binary file saved at {path}")
    

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data

    
           
@ensure_annotations
def get_size(path: Path) -> int:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB" if size_in_kb < 1024 else f"{round(size_in_kb/1024)} MB"


def decodeImage(imgstring, filenName):
    imgdata = base64.b64decode(imgstring)
    with open(filenName, 'wb') as f:
        f.write(imgdata)
        f.close()
        
   
def encodeImage(croppped_image_path):
    with open(croppped_image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode('utf-8')
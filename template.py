import os
from pathlib import Path

package_name = "Book_recommendation_system"

list_of_files = [
     "github/workflows/.gitkeep",
     f"src/{package_name}/__init__.py",
     f"src/{package_name}/components/__init__.py",
     f"src/{package_name}/components/data_ingestion.py",
     f"src/{package_name}/components/data_transformation.py",
     f"src/{package_name}/components/model_trainer.py",
     f"src/{package_name}/pipelines/__init__.py",
     f"src/{package_name}/pipelines/training_pipeline.py",
     f"src/{package_name}/pipelines/prediction_pipeline.py",
     f"src/{package_name}/logger.py",
     f"src/{package_name}/exception.py",
     f"src/{package_name}/utils/__init__.py",
     "notebooks/research.ipynb",
     "notebooks/data/.gitkeep",
     "requirements.txt",
     "setup.py",
     "init_setup.sh"
]

for filepath in list_of_files:
     filepath = Path(filepath) #generates the system compatable path
     filedir, filename = os.path.split(filepath)
     
     if filedir != "":
          os.makedirs(filedir, exist_ok=True)
          """
          exist_ok is used if the directory already exists then it does not raise an error but if 
          directory does not exist the it will craete the directory
          """
          
     if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
          with open(filepath, "w") as f:
               pass
          
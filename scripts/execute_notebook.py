import os
import subprocess

def execute_notebook(notebook_name):
    # Directorio relativo
    relative_directory = os.path.join(os.path.dirname(__file__), '../notebooks')
    notebook_path = os.path.join(relative_directory, notebook_name)
    print(notebook_path)
    
    if not os.path.exists(notebook_path):
        raise FileNotFoundError(f"The notebook {notebook_name} was not found at {notebook_path}")
    
    # Ejecuta el cuaderno
    subprocess.run([
        'jupyter', 'nbconvert', '--to', 'notebook', '--execute',
        '--inplace', notebook_path
    ])
    print(f"Executed the notebook: {notebook_name}")
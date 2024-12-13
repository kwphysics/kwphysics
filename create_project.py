import os

def create_project(project_name):
    structure = [
        f"{project_name}/src/backend",
        f"{project_name}/src/frontend",
        f"{project_name}/tests",
        f"{project_name}/docs",
        f"{project_name}/.vscode",
    ]
    files = [
        f"{project_name}/requirements.txt",
        f"{project_name}/.gitignore",
        f"{project_name}/README.md",
        f"{project_name}/src/main.py",
        f"{project_name}/.vscode/settings.json",
    ]
    gitignore_content = """
# Byte-compiled files
*.py[cod]
__pycache__/
*.so

# Virtual environments
.env/
.venv/
env/
venv/

# Cache files
*.cache
*.log
*.tmp
*.bak

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# Distribution/build artifacts
*.egg-info/
build/
dist/

# IDEs/Editors
.vscode/
.idea/
*.swp

# OS-specific
.DS_Store
Thumbs.db

# Test Coverage
.coverage
*.cover
*.gcda
*.gcno
*.gcov
coverage.xml

# Others
*.pyo
*.pyd
"""

    for folder in structure:
        os.makedirs(folder, exist_ok=True)

    for file in files:
        with open(file, "w") as f:
            if "settings.json" in file:
                f.write('{ "python.formatting.provider": "black", "editor.formatOnSave": true }')
            elif ".gitignore" in file:
                f.write(gitignore_content.strip())
    
    print(f"Project {project_name} created successfully!")

if __name__ == "__main__":
    project_name = input("Enter project name: ")
    create_project(project_name)
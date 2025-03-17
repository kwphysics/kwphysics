#!/bin/bash
project_name="HyperspectralAnalysis"
venv_path=".venv"

echo "Setting up $project_name..."

# Create virtual environment
python3 -m venv $venv_path
source $venv_path/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install black numpy matplotlib pytest pands

# Save dependencies
pip freeze > requirements.txt

echo "Setup complete. Run 'source .venv/bin/activate' to activate."
    
    The script creates a virtual environment, installs the required packages, and saves the dependencies to a  requirements.txt  file. 
    To run the script, make it executable by running: 
    chmod +x setup_project.sh
    
    Then, execute the script: 
    ./setup_project.sh
    
    This will create a virtual environment, install the required packages, and save the dependencies to a  requirements.txt  file. 
    Step 3 — Writing the Hyperspectral Analysis Script 
    Now that you have set up the project, you can write the script that will perform the hyperspectral analysis. 
    Create a new Python script named  hyperspectral_analysis.py : 
    nano hyperspectral_analysis.py
    
    Add the following code to the script:
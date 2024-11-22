#!/bin/bash

# Make sure to give this script execute permissions:
# chmod +x run_scripts.sh

# Array of Python scripts to execute
scripts=("DataCollection.py" "DataPreprocessing.py" "DataVisualization.py")

# Loop through each script and execute it
for script in "${scripts[@]}"
do
  echo "Running $script..."
  python "$script"  # Use 'python3' to ensure Python 3 is used
  if [ $? -ne 0 ]; then
    echo "Error occurred while running $script. Exiting."
    exit 1
  fi
done

echo "All scripts executed successfully."

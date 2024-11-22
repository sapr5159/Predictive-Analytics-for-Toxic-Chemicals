#!/bin/bash

# Define the virtual environment directory
VENV_DIR="venv"

# Check if the virtual environment already exists
if [ ! -d "$VENV_DIR" ]; then
  echo "Virtual environment not found. Creating a new one..."
  python3 -m venv "$VENV_DIR"
  if [ $? -ne 0 ]; then
    echo "Failed to create the virtual environment. Exiting."
    exit 1
  fi
else
  echo "Virtual environment already exists. Skipping creation."
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"
if [ $? -ne 0 ]; then
  echo "Failed to activate the virtual environment. Exiting."
  exit 1
fi
echo "Virtual environment activated."

# Install required packages
echo "Installing required packages..."
pip install --upgrade pip  # Upgrade pip
pip install pandas requests matplotlib seaborn statsmodels numpy

if [ $? -ne 0 ]; then
  echo "Failed to install required packages. Exiting."
  deactivate
  exit 1
fi

echo "All packages installed successfully."
echo "Virtual environment setup complete."

# Deactivate the virtual environment (optional step)
# deactivate

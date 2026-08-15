import sys
import os

# Add root folder to Python path to ensure module imports function correctly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.app import run

if __name__ == "__main__":
    run()

"""Handles Command-Line exceution of Project Generator"""
import logging
import sys
from app import category_generator as cg

categories = ["Wildlife", "Automobiles", "Health"]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("Running project-generator...")
    category = cg.get_random_category(categories)
    print(f"Selected category \"{category}\" for your project!")

    logging.info("Program exiting normally.")
    sys.exit(0)

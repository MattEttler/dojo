"""Handles Command-Line exceution of Project Generator"""
import logging
import sys
from app import category_generator as cg
from app import attribute_generator as ag
import attribute_config

categories = ["Wildlife", "Automobiles", "Health"]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("Running project-generator...")
    category = cg.generate_category(categories)
    print(f"Selected category \"{category}\" for your project!")
    attribute = ag.generate_attribute(attribute_config.attributes)
    print(f"Selected attribute \"{attribute}\" for your project!")
    logging.info("Program exiting normally.")
    sys.exit(0)

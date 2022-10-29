"""Entry module for project-generator built with the command-line in mind."""
import logging
import random
from app import errors

def generate_category(unordered_categories):
    """Get a single random category selected from the input list"""
    logging.info("Getting random category...")
    if not isinstance(unordered_categories, list) or len(unordered_categories) == 0:
        raise errors.NoCategoriesFoundError()
    return random.choice(unordered_categories)

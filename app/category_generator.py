"""Entry module for project-generator built with the command-line in mind."""
import logging
from typing import List
import random
from app import errors

def generate_category(unordered_categories: List[str]) -> str:
    """Get a single random category selected from the input list"""
    logging.info("Generating category...")
    if not isinstance(unordered_categories, list) or len(unordered_categories) == 0:
        raise errors.NoCategoriesFoundError()
    return random.choice(unordered_categories)

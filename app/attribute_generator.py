"""Module responsible for generating attributes"""
import logging
import random
from app import errors

def generate_attribute(attributes):
    """Chooses an attribute from the input list and returns it"""
    logging.info("Generating attribute...")
    if not isinstance(attributes, list) or len(attributes) == 0:
        raise errors.NoAttributesFoundError()
    return random.choice(attributes)

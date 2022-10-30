"""Test module for app.attribute_generator"""
# pylint: disable=R0201
import unittest
from typing import List
from hypothesis import given, strategies as st
from app import attribute_generator as ag
from app import errors

class TestGenerateAttribute(unittest.TestCase):
    """Test class for app.attribute_generator.generate_attribute"""

    @given(st.lists(st.text(), min_size=1))
    def test_should_return_result_in_attribute_list(self, attributes: List[str]) -> None:
        """Test that generate_attribute returns a result that is in the input list of attributes"""
        result = ag.generate_attribute(attributes)
        assert result in attributes

    @given(st.lists(st.text(), min_size=0, max_size=0))
    def test_should_raise_error_when_input_is_empty(self, attributes: List[str]) -> None:
        """Test that generate_attribute raises a NoAttributesFoundError when the input is empty"""
        with self.assertRaises(errors.NoAttributesFoundError):
            ag.generate_attribute(attributes)

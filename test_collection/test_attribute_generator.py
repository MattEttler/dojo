"""Test module for app.attribute_generator"""
# pylint: disable=R0201
import unittest
from hypothesis import given, strategies as st
from app import attribute_generator as ag

class TestGenerateAttribute(unittest.TestCase):
    """Test class for app.attribute_generator.generate_attribute"""

    @given(st.lists(st.text(), min_size=1))
    def test_generate_attribute_should_return_result_in_attribute_list(self, attributes):
        """Test that generate_attribute returns a result that is in the input list of attributes"""
        result = ag.generate_attribute(attributes)
        assert result in attributes

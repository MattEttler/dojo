"""Test module for app.project_generator"""
# pylint: disable=R0201
import unittest
import sys
from hypothesis import given, strategies as st
from app import category_generator as cg
from app import errors
sys.path.append('../app')

class ProjectGeneratorTestCase(unittest.TestCase):
    """Test class for app.project_generator"""
    @given(st.lists(st.text(), min_size=1))
    def test_result_in_categories(self, categories):
        """Ensure that any result returned from get_random_project
is contained within the input list of categories."""
        result = cg.generate_category(categories)
        assert result in categories

    @given(st.lists(st.text(), min_size=0, max_size=0))
    def test_result_in_categories_throws_error_when_categories_empty(self, categories):
        """Ensure proper errors are thrown when no categories exist"""
        with self.assertRaises(errors.NoCategoriesFoundError):
            cg.generate_category(categories)

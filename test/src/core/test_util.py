import unittest
from pydantic import BaseModel
from src.core.util import populate_pydantic_base_model_from_dict


class TestUtil(unittest.TestCase):

    class __User(BaseModel):
        first_name: str
        last_name: str

    def test_populate_pydantic_base_model_from_dict(self):
        data_lower = dict(first_name="Gabriel", last_name="Pagotto")

        # Test default params
        user = populate_pydantic_base_model_from_dict(self.__User, data_lower)
        self.assertEqual(user.first_name, "Gabriel")
        self.assertEqual(user.last_name, "Pagotto")

        # Test with keys as upper case
        data_lower = dict(FIRST_NAME="Gabriel", LAST_NAME="Pagotto")
        user = populate_pydantic_base_model_from_dict(self.__User, data_lower, upper_keys=True)
        self.assertEqual(user.first_name, "Gabriel")
        self.assertEqual(user.last_name, "Pagotto")

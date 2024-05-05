import unittest
from src.features.credit_score.data import get_data
from src.features.credit_score.model import CarInsuranceClaimModel


class TestData(unittest.TestCase):

    def test_get_data(self):
        data = get_data()
        self.assertGreater(len(data), 0)
        self.assertIsInstance(data[0], CarInsuranceClaimModel)

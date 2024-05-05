import unittest
from src.features.credit_score.util import check_age, check_driving_experience, check_vehicle_year


class TestUtil(unittest.TestCase):

    def test_check_age(self):
        self.assertTrue(check_age("30-40", 30))
        self.assertTrue(check_age("30-40", 35))
        self.assertTrue(check_age("30-40", 40))
        self.assertFalse(check_age("30-40", 50))

        self.assertTrue(check_age("60+", 60))
        self.assertTrue(check_age("60+", 80))
        self.assertFalse(check_age("60+", 50))

    def test_check_driving_experience(self):
        self.assertTrue(check_driving_experience("5-10y", 5))
        self.assertTrue(check_driving_experience("5-10y", 7))
        self.assertTrue(check_driving_experience("5-10y", 10))

        self.assertFalse(check_driving_experience("5-10y", 4))
        self.assertFalse(check_driving_experience("5-10y", 11))

        self.assertTrue(check_driving_experience("25y+", 30))
        self.assertTrue(check_driving_experience("25y+", 25))
        self.assertFalse(check_driving_experience("25y+", 24))

    def test_check_vehicle_year(self):
        self.assertTrue(check_vehicle_year("before 2015", 2000))
        self.assertTrue(check_vehicle_year("before 2015", 2014))
        self.assertTrue(check_vehicle_year("before 2015", 2015))

        self.assertFalse(check_vehicle_year("before 2015", 2016))
        self.assertFalse(check_vehicle_year("before 2015", 2020))

        self.assertTrue(check_vehicle_year("after 2015", 2015))
        self.assertTrue(check_vehicle_year("after 2015", 2017))
        self.assertTrue(check_vehicle_year("after 2015", 2020))

        self.assertFalse(check_vehicle_year("after 2015", 2014))
        self.assertFalse(check_vehicle_year("after 2015", 2000))

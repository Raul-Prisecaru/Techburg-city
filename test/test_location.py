import unittest
from model.location import Location

class TestLocation(unittest.TestCase):

    def test_getter(self):
        location = Location(1, 2)
        self.assertEqual(location.get_x(), 2, "X value was incorrectly returned")
        self.assertEqual(location.get_y(), 1, "Y value was incorrectly returned")


    def test_setter(self):
        location = Location(1,2)
        location.set_x(3)
        location.set_y(4)

        self.assertEqual(location.get_x(), 3, "X value was incorrectly updated")
        self.assertEqual(location.get_y(), 4, "Y value was incorrectly updated")

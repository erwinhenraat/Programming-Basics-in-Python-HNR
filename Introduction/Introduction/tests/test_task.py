import unittest

from ..introduction import name


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(name("Erwin"), "Erwin", msg="Good luck with this course")

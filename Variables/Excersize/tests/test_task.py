import unittest

from ..task import name


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(name, "good morning", msg="Good morning to you too")

import unittest
from josephNoob import chance_to_kill
from volleyball_legend import volleyball_legend
from pay_for_win import pay_pls


class TestL1(unittest.TestCase):
    def test_lesson_1(self):
        self.assertEqual(chance_to_kill(1, 70), 7)
        self.assertEqual(chance_to_kill(2, 70), 8)
        self.assertEqual(chance_to_kill(5, 70), 10)


class TestL2(unittest.TestCase):
    def test_lesson_1(self):
        self.assertEqual(volleyball_legend(3, 2), 80)


class TestL3(unittest.TestCase):
    def test_lesson_1(self):
        self.assertEqual(pay_pls(500, -50), 275)


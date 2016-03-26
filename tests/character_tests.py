import unittest
from lib import Character


class TestMoney(unittest.TestCase):
    """Test money operations on Character class"""
    def setUp(self):
        self.character = Character([], [], 0, 0, 0, 1000, 1, 0, 0)

    def test_defaults(self):
        """Test defaults"""
        self.assertEquals(self.character.Money, 1000)

    def test_add(self):
        """Test addition of money"""
        char = self.character
        money = char.Money
        amount = 100
        char.add_money(amount)
        self.assertEquals(char.Money, money + amount)

    def test_subtract_ok(self):
        """Test subtration is ok"""
        char = self.character
        money = char.Money
        amount = 999
        result = char.subtract_money(amount)
        self.assertTrue(result)
        self.assertEquals(char.Money, money - amount)


    def test_subtract_fail(self):
        """Test failure of subtraction"""
        char = self.character
        money = char.Money
        amount = 1001
        result = char.subtract_money(amount)
        self.assertFalse(result)
        self.assertEqual(char.Money, money)

if __name__ == '__main__':
    unittest.main()

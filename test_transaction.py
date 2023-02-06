import unittest

from transaction import Transaction


class TestTransaction(unittest.TestCase):
    def test_transaction_attributes(self):
        t = Transaction("sender", "recipient", 100)
        self.assertEqual(t.sender, "sender")
        self.assertEqual(t.recipient, "recipient")
        self.assertEqual(t.amount, 100)


if __name__ == '__main__':
    unittest.main()

import unittest
from blockchain import Blockchain


class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_genesis_block(self):
        genesis_block = self.blockchain.chain[0]
        self.assertEqual(genesis_block.index, 1)
        self.assertEqual(genesis_block.proof, 100)
        # Add more checks for the properties of the genesis block

    def test_new_block(self):
        previous_block = self.blockchain.last_block
        new_block = self.blockchain.new_block(proof=123, previous_hash=previous_block.hash)
        self.assertEqual(new_block.index, 2)
        self.assertEqual(new_block.previous_hash, previous_block.hash)
        # Add more checks for the properties of the new block

    # Add more tests for the Blockchain class


if __name__ == '__main__':
    unittest.main()

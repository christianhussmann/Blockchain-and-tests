import hashlib
import json
import unittest

from block import Block


class TestBlock(unittest.TestCase):
    def test_hash(self):
        index = 0
        timestamp = "some_timestamp"
        transactions = ["transaction1", "transaction2"]
        proof = 42
        previous_hash = "some_previous_hash"
        merkle_root = "some_merkle_root"
        block = Block(index, timestamp, transactions, proof, previous_hash, merkle_root)

        # Ensure that the hash method returns the expected value
        self.assertEqual(
            block.hash(),
            hashlib.sha256(
                json.dumps(
                    {
                        "index": 0,
                        "timestamp": "some_timestamp",
                        "transactions": ["transaction1", "transaction2"],
                        "proof": 42,
                        "previous_hash": "some_previous_hash",
                        "merkle_root": "some_merkle_root",
                    },
                    sort_keys=True,
                ).encode()
            ).hexdigest()
        )


if __name__ == "__main__":
    unittest.main()
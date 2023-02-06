import hashlib
import json


class Block:
    def __init__(self, index, timestamp, transactions, proof, previous_hash, merkle_root):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash
        self.merkle_root = merkle_root

    def hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

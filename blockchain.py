import hashlib
import time
from transaction import Transaction
from block import Block
from merkle_tree import MerkleTree


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash):
        """
        Create a new Block in the Blockchain
        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of previous Block
        :return: New Block
        """
        # Create the Merkle tree from the current transactions
        leaves = [tx.to_dict() for tx in self.current_transactions]
        merkle_tree = MerkleTree(leaves)
        root_hash = merkle_tree.root()

        block = Block(
            index=len(self.chain) + 1,
            timestamp=time.time(),
            transactions=self.current_transactions,
            proof=proof,
            previous_hash=previous_hash or self.hash(self.chain[-1]),
            merkle_root=root_hash
        )

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: Amount
        :return: The index of the Block that will hold this transaction
        """
        self.current_transactions.append(Transaction(sender, recipient, amount))
        return self.last_block.index + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: Block
        """
        block_string = f"{block.index}{block.timestamp}{block.transactions}{block.proof}{block.previous_hash}{block.merkle_root} "
        return hashlib.sha256(block_string.encode()).hexdigest()

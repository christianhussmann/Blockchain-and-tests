from blockchain import Blockchain

if __name__ == '__main__':
    blockchain = Blockchain()

    print("Mining block 1...")
    blockchain.new_block(proof=100, previous_hash=1)

    print("Mining block 2...")
    blockchain.new_block(proof=67, previous_hash=blockchain.hash(blockchain.last_block))

    print("Mining block 3...")
    blockchain.new_block(proof=234, previous_hash=blockchain.hash(blockchain.last_block))

    print(blockchain.chain)
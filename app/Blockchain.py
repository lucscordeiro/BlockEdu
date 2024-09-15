import hashlib
import time
from .Transaction import Transaction

class Block:
    def __init__(self, index, previous_hash, data, transactions=None, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.data = data
        self.transactions = transactions or []
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.transactions}"
        return hashlib.sha256(block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []

    def create_genesis_block(self):
        return Block(0, "0", "Bloco Gênesis")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(latest_block.index + 1, latest_block.hash, data, self.pending_transactions)
        self.chain.append(new_block)
        self.pending_transactions = []  # Clear pending transactions once they are added to a block
        return new_block

    def add_transaction(self, transaction):
        if isinstance(transaction, Transaction):
            self.pending_transactions.append(transaction.to_dict())
        else:
            raise ValueError("Invalid transaction format")

    def get_chain(self):
        return [block.__dict__ for block in self.chain]

    def get_pending_transactions(self):
        return self.pending_transactions

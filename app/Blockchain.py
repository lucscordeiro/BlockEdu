import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}"
        return hashlib.sha256(block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Bloco Gênesis")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(latest_block.index + 1, latest_block.hash, data)
        self.chain.append(new_block)
        return new_block

    def get_chain(self):
        return [block.__dict__ for block in self.chain]

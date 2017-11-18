#!/usr/bin/env python

import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        s = (str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash)
        )
        s = s.encode('utf-8')

        sha = hasher.sha256()
        sha.update(s)
        return sha.hexdigest()



def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


if __name__ == '__main__':
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    n = 20

    for i in range(n):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add

        print(f'Block #{block_to_add.index} has been added.')
        print(f'Hash: {block_to_add.hash}\n')

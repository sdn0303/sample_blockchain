# -*- Coding: UTF-8 -*-
from cryptocurrency_genesis import create_genesis_block
from cryptocurrency_new_block import next_block

blockchain = [create_genesis_block()]
previous_block = blockchain[0]
num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    blocks_to_add = next_block(previous_block)
    blockchain.append(blocks_to_add)
    previous_block = blocks_to_add
    print('Block {} has been added to the blockchain.'.format(blocks_to_add.index))
    print('Hash: {}\n'.format(blocks_to_add.hash))

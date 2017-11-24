# -*- Coding: UTF-8 -*-
import datetime as date

from cryptocurrency_block import Block


def next_block(last_block) -> callable(object):
    """ 次のブロックを生成
    :param last_block: 前のブロックの情報
    :return: 新しく生成したブロック
    """
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Create the new block." + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

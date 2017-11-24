# -*- Coding: UTF-8 -*-
import datetime as date

from cryptocurrency_block import Block


def create_genesis_block() -> callable(object):
    """ 最初のブロックを生成
    :return: 最初のBlock
    """
    return Block(0, date.datetime.now(), 'Genesis Block', '0')

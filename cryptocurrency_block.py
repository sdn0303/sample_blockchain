# -*- Coding: UTF-8 -*-
import hashlib


class Block(object):
    """ ブロック生成クラス
    """

    def __init__(self, index: int, timestamp: object, data: str, previous_hash: hash):
        """ 初期値
        :param index: インデックス
        :param timestamp: 日付情報
        :param data: 取引内容
        :param previous_hash: ハッシュ値
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self) -> hash:
        """
        一個前のindex, timestamp, data, previous_hashのhashを生成
        :return: hash
        """
        sha = hashlib.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_inbox_client.model import *


class ReadMessagesResult(object):

    def __init__(self, response):
        """
        コンストラクタ
        :type response: レスポンスボディ
        :type response: dict
        """
        self.__items = list(
            map(
                lambda data:
                Message(data),
                response['items']
            )
        )
        self.__cooperation_response = unicode(response['cooperationResponse']) if 'cooperationResponse' in response.keys() and response['cooperationResponse'] is not None else None
    def get_items(self):
        """
        メッセージを取得
        :return: メッセージ
        :rtype: list[Message]
        """
        return self.__items
    def get_cooperation_response(self):
        """
        開封通知のレスポンス内容を取得
        :return: 開封通知のレスポンス内容
        :rtype: unicode
        """
        return self.__cooperation_response

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(ReadMessagesResult, self).__getitem__(key)

    def to_dict(self):
        """
        辞書配列に変換
        :return: 辞書配列
        :rtype: dict
        """
        return {
            'items': map(lambda item: item.to_dict(), self.__items),
            'cooperationResponse': self.__cooperation_response,
        }

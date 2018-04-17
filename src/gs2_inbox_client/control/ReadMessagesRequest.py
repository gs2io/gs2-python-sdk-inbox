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

from gs2_core_client.Gs2UserRequest import Gs2UserRequest
from gs2_inbox_client.Gs2Inbox import Gs2Inbox


class ReadMessagesRequest(Gs2UserRequest):

    class Constant(Gs2Inbox):
        FUNCTION = "ReadMessages"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(ReadMessagesRequest, self).__init__(params)
        if params is None:
            self.__inbox_name = None
            self.__message_ids = None
        else:
            self.set_inbox_name(params['inboxName'] if 'inboxName' in params.keys() else None)
            self.set_message_ids(params['messageIds'] if 'messageIds' in params.keys() else None)

    def get_inbox_name(self):
        """
        受信ボックスの名前を指定します。を取得
        :return: 受信ボックスの名前を指定します。
        :rtype: unicode
        """
        return self.__inbox_name

    def set_inbox_name(self, inbox_name):
        """
        受信ボックスの名前を指定します。を設定
        :param inbox_name: 受信ボックスの名前を指定します。
        :type inbox_name: unicode
        """
        if _inbox_name and not (isinstance(_inbox_name, str) or isinstance(_inbox_name, unicode)):
            raise TypeError(type(inbox_name))
        self.__inbox_name = inbox_name

    def with_inbox_name(self, inbox_name):
        """
        受信ボックスの名前を指定します。を設定
        :param inbox_name: 受信ボックスの名前を指定します。
        :type inbox_name: unicode
        :return: this
        :rtype: ReadMessagesRequest
        """
        self.set_inbox_name(inbox_name)
        return self

    def get_message_ids(self):
        """
        カンマ区切りの開封するメッセージのメッセージIDリストを取得
        :return: カンマ区切りの開封するメッセージのメッセージIDリスト
        :rtype: unicode
        """
        return self.__message_ids

    def set_message_ids(self, message_ids):
        """
        カンマ区切りの開封するメッセージのメッセージIDリストを設定
        :param message_ids: カンマ区切りの開封するメッセージのメッセージIDリスト
        :type message_ids: unicode
        """
        if _message_ids and not (isinstance(_message_ids, str) or isinstance(_message_ids, unicode)):
            raise TypeError(type(message_ids))
        self.__message_ids = message_ids

    def with_message_ids(self, message_ids):
        """
        カンマ区切りの開封するメッセージのメッセージIDリストを設定
        :param message_ids: カンマ区切りの開封するメッセージのメッセージIDリスト
        :type message_ids: unicode
        :return: this
        :rtype: ReadMessagesRequest
        """
        self.set_message_ids(message_ids)
        return self

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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_inbox_client.Gs2Inbox import Gs2Inbox


class SendMessageRequest(Gs2BasicRequest):

    class Constant(Gs2Inbox):
        FUNCTION = "SendMessage"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(SendMessageRequest, self).__init__(params)
        if params is None:
            self.__inbox_name = None
        else:
            self.set_inbox_name(params['inboxName'] if 'inboxName' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
        if params is None:
            self.__message = None
        else:
            self.set_message(params['message'] if 'message' in params.keys() else None)
        if params is None:
            self.__cooperation = None
        else:
            self.set_cooperation(params['cooperation'] if 'cooperation' in params.keys() else None)

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
        if inbox_name and not (isinstance(inbox_name, str) or isinstance(inbox_name, unicode)):
            raise TypeError(type(inbox_name))
        self.__inbox_name = inbox_name

    def with_inbox_name(self, inbox_name):
        """
        受信ボックスの名前を指定します。を設定
        :param inbox_name: 受信ボックスの名前を指定します。
        :type inbox_name: unicode
        :return: this
        :rtype: SendMessageRequest
        """
        self.set_inbox_name(inbox_name)
        return self

    def get_user_id(self):
        """
        メッセージを送信する相手のユーザIDを取得
        :return: メッセージを送信する相手のユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        メッセージを送信する相手のユーザIDを設定
        :param user_id: メッセージを送信する相手のユーザID
        :type user_id: unicode
        """
        if user_id and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        メッセージを送信する相手のユーザIDを設定
        :param user_id: メッセージを送信する相手のユーザID
        :type user_id: unicode
        :return: this
        :rtype: SendMessageRequest
        """
        self.set_user_id(user_id)
        return self

    def get_message(self):
        """
        送信するメッセージ本文を取得
        :return: 送信するメッセージ本文
        :rtype: unicode
        """
        return self.__message

    def set_message(self, message):
        """
        送信するメッセージ本文を設定
        :param message: 送信するメッセージ本文
        :type message: unicode
        """
        if message and not (isinstance(message, str) or isinstance(message, unicode)):
            raise TypeError(type(message))
        self.__message = message

    def with_message(self, message):
        """
        送信するメッセージ本文を設定
        :param message: 送信するメッセージ本文
        :type message: unicode
        :return: this
        :rtype: SendMessageRequest
        """
        self.set_message(message)
        return self

    def get_cooperation(self):
        """
        true を設定すると、メッセージ開封時に受信ボックスに指定された連携用URLにメッセージIDが通知されますを取得
        :return: true を設定すると、メッセージ開封時に受信ボックスに指定された連携用URLにメッセージIDが通知されます
        :rtype: bool
        """
        return self.__cooperation

    def set_cooperation(self, cooperation):
        """
        true を設定すると、メッセージ開封時に受信ボックスに指定された連携用URLにメッセージIDが通知されますを設定
        :param cooperation: true を設定すると、メッセージ開封時に受信ボックスに指定された連携用URLにメッセージIDが通知されます
        :type cooperation: bool
        """
        if cooperation and not isinstance(cooperation, bool):
            raise TypeError(type(cooperation))
        self.__cooperation = cooperation

    def with_cooperation(self, cooperation):
        """
        true を設定すると、メッセージ開封時に受信ボックスに指定された連携用URLにメッセージIDが通知されますを設定
        :param cooperation: true を設定すると、メッセージ開封時に受信ボックスに指定された連携用URLにメッセージIDが通知されます
        :type cooperation: bool
        :return: this
        :rtype: SendMessageRequest
        """
        self.set_cooperation(cooperation)
        return self

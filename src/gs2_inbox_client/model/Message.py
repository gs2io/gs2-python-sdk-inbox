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

class Message(object):

    def __init__(self, params=None):
        if params is None:
            self.__message_id = None
            self.__inbox_id = None
            self.__user_id = None
            self.__message = None
            self.__cooperation = None
            self.__read = None
            self.__date = None
        else:
            self.set_message_id(params['messageId'] if 'messageId' in params.keys() else None)
            self.set_inbox_id(params['inboxId'] if 'inboxId' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_message(params['message'] if 'message' in params.keys() else None)
            self.set_cooperation(params['cooperation'] if 'cooperation' in params.keys() else None)
            self.set_read(params['read'] if 'read' in params.keys() else None)
            self.set_date(params['date'] if 'date' in params.keys() else None)


    def get_message_id(self):
        """
        メッセージIDを取得
        :return: メッセージID
        :rtype: unicode
        """
        return self.__message_id

    def set_message_id(self, message_id):
        """
        メッセージIDを設定
        :param message_id: メッセージID
        :type message_id: unicode
        """
        self.__message_id = message_id

    def get_inbox_id(self):
        """
        受信ボックスGRNを取得
        :return: 受信ボックスGRN
        :rtype: unicode
        """
        return self.__inbox_id

    def set_inbox_id(self, inbox_id):
        """
        受信ボックスGRNを設定
        :param inbox_id: 受信ボックスGRN
        :type inbox_id: unicode
        """
        self.__inbox_id = inbox_id

    def get_user_id(self):
        """
        発言者ユーザIDを取得
        :return: 発言者ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        発言者ユーザIDを設定
        :param user_id: 発言者ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

    def get_message(self):
        """
        メッセージ本文を取得
        :return: メッセージ本文
        :rtype: unicode
        """
        return self.__message

    def set_message(self, message):
        """
        メッセージ本文を設定
        :param message: メッセージ本文
        :type message: unicode
        """
        self.__message = message

    def get_cooperation(self):
        """
        開封時に通知を出すかを取得
        :return: 開封時に通知を出すか
        :rtype: bool
        """
        return self.__cooperation

    def set_cooperation(self, cooperation):
        """
        開封時に通知を出すかを設定
        :param cooperation: 開封時に通知を出すか
        :type cooperation: bool
        """
        self.__cooperation = cooperation

    def get_read(self):
        """
        既読状態を取得
        :return: 既読状態
        :rtype: bool
        """
        return self.__read

    def set_read(self, read):
        """
        既読状態を設定
        :param read: 既読状態
        :type read: bool
        """
        self.__read = read

    def get_date(self):
        """
        受信日時(エポック秒)を取得
        :return: 受信日時(エポック秒)
        :rtype: int
        """
        return self.__date

    def set_date(self, date):
        """
        受信日時(エポック秒)を設定
        :param date: 受信日時(エポック秒)
        :type date: int
        """
        self.__date = date

    def to_dict(self):
        return { 
            "messageId": self.__message_id,
            "inboxId": self.__inbox_id,
            "userId": self.__user_id,
            "message": self.__message,
            "cooperation": self.__cooperation,
            "read": self.__read,
            "date": self.__date,
        }
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


class Inbox(object):

    def __init__(self, params=None):
        if params is None:
            self.__inbox_id = None
            self.__owner_id = None
            self.__name = None
            self.__description = None
            self.__service_class = None
            self.__auto_delete = None
            self.__cooperation_url = None
            self.__receive_message_trigger_script = None
            self.__receive_message_done_trigger_script = None
            self.__read_message_trigger_script = None
            self.__read_message_done_trigger_script = None
            self.__delete_message_trigger_script = None
            self.__delete_message_done_trigger_script = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_inbox_id(params['inboxId'] if 'inboxId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_auto_delete(params['autoDelete'] if 'autoDelete' in params.keys() else None)
            self.set_cooperation_url(params['cooperationUrl'] if 'cooperationUrl' in params.keys() else None)
            self.set_receive_message_trigger_script(params['receiveMessageTriggerScript'] if 'receiveMessageTriggerScript' in params.keys() else None)
            self.set_receive_message_done_trigger_script(params['receiveMessageDoneTriggerScript'] if 'receiveMessageDoneTriggerScript' in params.keys() else None)
            self.set_read_message_trigger_script(params['readMessageTriggerScript'] if 'readMessageTriggerScript' in params.keys() else None)
            self.set_read_message_done_trigger_script(params['readMessageDoneTriggerScript'] if 'readMessageDoneTriggerScript' in params.keys() else None)
            self.set_delete_message_trigger_script(params['deleteMessageTriggerScript'] if 'deleteMessageTriggerScript' in params.keys() else None)
            self.set_delete_message_done_trigger_script(params['deleteMessageDoneTriggerScript'] if 'deleteMessageDoneTriggerScript' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

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

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_name(self):
        """
        受信ボックス名を取得
        :return: 受信ボックス名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        受信ボックス名を設定
        :param name: 受信ボックス名
        :type name: unicode
        """
        self.__name = name

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        self.__description = description

    def get_service_class(self):
        """
        サービスクラスを取得
        :return: サービスクラス
        :rtype: unicode
        """
        return self.__service_class

    def set_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        """
        self.__service_class = service_class

    def get_auto_delete(self):
        """
        開封時自動削除を取得
        :return: 開封時自動削除
        :rtype: bool
        """
        return self.__auto_delete

    def set_auto_delete(self, auto_delete):
        """
        開封時自動削除を設定
        :param auto_delete: 開封時自動削除
        :type auto_delete: bool
        """
        self.__auto_delete = auto_delete

    def get_cooperation_url(self):
        """
        メッセージの開封通知先URLを取得
        :return: メッセージの開封通知先URL
        :rtype: unicode
        """
        return self.__cooperation_url

    def set_cooperation_url(self, cooperation_url):
        """
        メッセージの開封通知先URLを設定
        :param cooperation_url: メッセージの開封通知先URL
        :type cooperation_url: unicode
        """
        self.__cooperation_url = cooperation_url

    def get_receive_message_trigger_script(self):
        """
        メッセージ受信時 に実行されるGS2-Scriptを取得
        :return: メッセージ受信時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__receive_message_trigger_script

    def set_receive_message_trigger_script(self, receive_message_trigger_script):
        """
        メッセージ受信時 に実行されるGS2-Scriptを設定
        :param receive_message_trigger_script: メッセージ受信時 に実行されるGS2-Script
        :type receive_message_trigger_script: unicode
        """
        self.__receive_message_trigger_script = receive_message_trigger_script

    def get_receive_message_done_trigger_script(self):
        """
        メッセージ受信完了時 に実行されるGS2-Scriptを取得
        :return: メッセージ受信完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__receive_message_done_trigger_script

    def set_receive_message_done_trigger_script(self, receive_message_done_trigger_script):
        """
        メッセージ受信完了時 に実行されるGS2-Scriptを設定
        :param receive_message_done_trigger_script: メッセージ受信完了時 に実行されるGS2-Script
        :type receive_message_done_trigger_script: unicode
        """
        self.__receive_message_done_trigger_script = receive_message_done_trigger_script

    def get_read_message_trigger_script(self):
        """
        メッセージ開封時 に実行されるGS2-Scriptを取得
        :return: メッセージ開封時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__read_message_trigger_script

    def set_read_message_trigger_script(self, read_message_trigger_script):
        """
        メッセージ開封時 に実行されるGS2-Scriptを設定
        :param read_message_trigger_script: メッセージ開封時 に実行されるGS2-Script
        :type read_message_trigger_script: unicode
        """
        self.__read_message_trigger_script = read_message_trigger_script

    def get_read_message_done_trigger_script(self):
        """
        メッセージ開封完了時 に実行されるGS2-Scriptを取得
        :return: メッセージ開封完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__read_message_done_trigger_script

    def set_read_message_done_trigger_script(self, read_message_done_trigger_script):
        """
        メッセージ開封完了時 に実行されるGS2-Scriptを設定
        :param read_message_done_trigger_script: メッセージ開封完了時 に実行されるGS2-Script
        :type read_message_done_trigger_script: unicode
        """
        self.__read_message_done_trigger_script = read_message_done_trigger_script

    def get_delete_message_trigger_script(self):
        """
        メッセージ削除時 に実行されるGS2-Scriptを取得
        :return: メッセージ削除時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__delete_message_trigger_script

    def set_delete_message_trigger_script(self, delete_message_trigger_script):
        """
        メッセージ削除時 に実行されるGS2-Scriptを設定
        :param delete_message_trigger_script: メッセージ削除時 に実行されるGS2-Script
        :type delete_message_trigger_script: unicode
        """
        self.__delete_message_trigger_script = delete_message_trigger_script

    def get_delete_message_done_trigger_script(self):
        """
        メッセージ削除完了時 に実行されるGS2-Scriptを取得
        :return: メッセージ削除完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__delete_message_done_trigger_script

    def set_delete_message_done_trigger_script(self, delete_message_done_trigger_script):
        """
        メッセージ削除完了時 に実行されるGS2-Scriptを設定
        :param delete_message_done_trigger_script: メッセージ削除完了時 に実行されるGS2-Script
        :type delete_message_done_trigger_script: unicode
        """
        self.__delete_message_done_trigger_script = delete_message_done_trigger_script

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(Inbox, self).__getitem__(key)

    def to_dict(self):
        return {
            "inboxId": self.__inbox_id,
            "ownerId": self.__owner_id,
            "name": self.__name,
            "description": self.__description,
            "serviceClass": self.__service_class,
            "autoDelete": self.__auto_delete,
            "cooperationUrl": self.__cooperation_url,
            "receiveMessageTriggerScript": self.__receive_message_trigger_script,
            "receiveMessageDoneTriggerScript": self.__receive_message_done_trigger_script,
            "readMessageTriggerScript": self.__read_message_trigger_script,
            "readMessageDoneTriggerScript": self.__read_message_done_trigger_script,
            "deleteMessageTriggerScript": self.__delete_message_trigger_script,
            "deleteMessageDoneTriggerScript": self.__delete_message_done_trigger_script,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }

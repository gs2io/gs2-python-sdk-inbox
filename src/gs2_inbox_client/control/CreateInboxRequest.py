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


class CreateInboxRequest(Gs2BasicRequest):

    class Constant(Gs2Inbox):
        FUNCTION = "CreateInbox"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateInboxRequest, self).__init__(params)
        if params is None:
            self.__name = None
            self.__service_class = None
            self.__auto_delete = None
            self.__cooperation_url = None
            self.__receive_message_trigger_script = None
            self.__receive_message_done_trigger_script = None
            self.__read_message_trigger_script = None
            self.__read_message_done_trigger_script = None
            self.__delete_message_trigger_script = None
            self.__delete_message_done_trigger_script = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_auto_delete(params['autoDelete'] if 'autoDelete' in params.keys() else None)
            self.set_cooperation_url(params['cooperationUrl'] if 'cooperationUrl' in params.keys() else None)
            self.set_receive_message_trigger_script(params['receiveMessageTriggerScript'] if 'receiveMessageTriggerScript' in params.keys() else None)
            self.set_receive_message_done_trigger_script(params['receiveMessageDoneTriggerScript'] if 'receiveMessageDoneTriggerScript' in params.keys() else None)
            self.set_read_message_trigger_script(params['readMessageTriggerScript'] if 'readMessageTriggerScript' in params.keys() else None)
            self.set_read_message_done_trigger_script(params['readMessageDoneTriggerScript'] if 'readMessageDoneTriggerScript' in params.keys() else None)
            self.set_delete_message_trigger_script(params['deleteMessageTriggerScript'] if 'deleteMessageTriggerScript' in params.keys() else None)
            self.set_delete_message_done_trigger_script(params['deleteMessageDoneTriggerScript'] if 'deleteMessageDoneTriggerScript' in params.keys() else None)

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

    def with_name(self, name):
        """
        受信ボックス名を設定
        :param name: 受信ボックス名
        :type name: unicode
        :return: this
        :rtype: CreateInboxRequest
        """
        self.set_name(name)
        return self

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

    def with_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        :return: this
        :rtype: CreateInboxRequest
        """
        self.set_service_class(service_class)
        return self

    def get_auto_delete(self):
        """
        開封時自動削除機能を使用するかを取得
        :return: 開封時自動削除機能を使用するか
        :rtype: bool
        """
        return self.__auto_delete

    def set_auto_delete(self, auto_delete):
        """
        開封時自動削除機能を使用するかを設定
        :param auto_delete: 開封時自動削除機能を使用するか
        :type auto_delete: bool
        """
        self.__auto_delete = auto_delete

    def with_auto_delete(self, auto_delete):
        """
        開封時自動削除機能を使用するかを設定
        :param auto_delete: 開封時自動削除機能を使用するか
        :type auto_delete: bool
        :return: this
        :rtype: CreateInboxRequest
        """
        self.set_auto_delete(auto_delete)
        return self

    def get_cooperation_url(self):
        """
        開封時通知設定が有効な場合に通知するURLを取得
        :return: 開封時通知設定が有効な場合に通知するURL
        :rtype: unicode
        """
        return self.__cooperation_url

    def set_cooperation_url(self, cooperation_url):
        """
        開封時通知設定が有効な場合に通知するURLを設定
        :param cooperation_url: 開封時通知設定が有効な場合に通知するURL
        :type cooperation_url: unicode
        """
        self.__cooperation_url = cooperation_url

    def with_cooperation_url(self, cooperation_url):
        """
        開封時通知設定が有効な場合に通知するURLを設定
        :param cooperation_url: 開封時通知設定が有効な場合に通知するURL
        :type cooperation_url: unicode
        :return: this
        :rtype: CreateInboxRequest
        """
        self.set_cooperation_url(cooperation_url)
        return self

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

    def with_receive_message_trigger_script(self, receive_message_trigger_script):
        """
        メッセージ受信時 に実行されるGS2-Scriptを設定
        :param receive_message_trigger_script: メッセージ受信時 に実行されるGS2-Script
        :type receive_message_trigger_script: unicode
        :return: this
        :rtype: CreateInboxRequest
        """
        self.set_receive_message_trigger_script(receive_message_trigger_script)
        return self

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

    def with_receive_message_done_trigger_script(self, receive_message_done_trigger_script):
        """
        メッセージ受信完了時 に実行されるGS2-Scriptを設定
        :param receive_message_done_trigger_script: メッセージ受信完了時 に実行されるGS2-Script
        :type receive_message_done_trigger_script: unicode
        :return: this
        :rtype: CreateInboxRequest
        """
        self.set_receive_message_done_trigger_script(receive_message_done_trigger_script)
        return self

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

    def with_read_message_trigger_script(self, read_message_trigger_script):
        """
        メッセージ開封時 に実行されるGS2-Scriptを設定
        :param read_message_trigger_script: メッセージ開封時 に実行されるGS2-Script
        :type read_message_trigger_script: unicode
        :return: this
        :rtype: CreateInboxRequest
        """
        self.set_read_message_trigger_script(read_message_trigger_script)
        return self

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

    def with_read_message_done_trigger_script(self, read_message_done_trigger_script):
        """
        メッセージ開封完了時 に実行されるGS2-Scriptを設定
        :param read_message_done_trigger_script: メッセージ開封完了時 に実行されるGS2-Script
        :type read_message_done_trigger_script: unicode
        :return: this
        :rtype: CreateInboxRequest
        """
        self.set_read_message_done_trigger_script(read_message_done_trigger_script)
        return self

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

    def with_delete_message_trigger_script(self, delete_message_trigger_script):
        """
        メッセージ削除時 に実行されるGS2-Scriptを設定
        :param delete_message_trigger_script: メッセージ削除時 に実行されるGS2-Script
        :type delete_message_trigger_script: unicode
        :return: this
        :rtype: CreateInboxRequest
        """
        self.set_delete_message_trigger_script(delete_message_trigger_script)
        return self

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

    def with_delete_message_done_trigger_script(self, delete_message_done_trigger_script):
        """
        メッセージ削除完了時 に実行されるGS2-Scriptを設定
        :param delete_message_done_trigger_script: メッセージ削除完了時 に実行されるGS2-Script
        :type delete_message_done_trigger_script: unicode
        :return: this
        :rtype: CreateInboxRequest
        """
        self.set_delete_message_done_trigger_script(delete_message_done_trigger_script)
        return self

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
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
        if params is None:
            self.__description = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)
        if params is None:
            self.__service_class = None
        else:
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
        if params is None:
            self.__auto_delete = None
        else:
            self.set_auto_delete(params['autoDelete'] if 'autoDelete' in params.keys() else None)
        if params is None:
            self.__cooperation_url = None
        else:
            self.set_cooperation_url(params['cooperationUrl'] if 'cooperationUrl' in params.keys() else None)
        if params is None:
            self.__receive_message_trigger_script = None
        else:
            self.set_receive_message_trigger_script(params['receiveMessageTriggerScript'] if 'receiveMessageTriggerScript' in params.keys() else None)
        if params is None:
            self.__receive_message_done_trigger_script = None
        else:
            self.set_receive_message_done_trigger_script(params['receiveMessageDoneTriggerScript'] if 'receiveMessageDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__read_message_trigger_script = None
        else:
            self.set_read_message_trigger_script(params['readMessageTriggerScript'] if 'readMessageTriggerScript' in params.keys() else None)
        if params is None:
            self.__read_message_done_trigger_script = None
        else:
            self.set_read_message_done_trigger_script(params['readMessageDoneTriggerScript'] if 'readMessageDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__delete_message_trigger_script = None
        else:
            self.set_delete_message_trigger_script(params['deleteMessageTriggerScript'] if 'deleteMessageTriggerScript' in params.keys() else None)
        if params is None:
            self.__delete_message_done_trigger_script = None
        else:
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
        if name is not None and not (isinstance(name, str) or isinstance(name, unicode)):
            raise TypeError(type(name))
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
        if description is not None and not (isinstance(description, str) or isinstance(description, unicode)):
            raise TypeError(type(description))
        self.__description = description

    def with_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        :return: this
        :rtype: CreateInboxRequest
        """
        self.set_description(description)
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
        if service_class is not None and not (isinstance(service_class, str) or isinstance(service_class, unicode)):
            raise TypeError(type(service_class))
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
        if auto_delete is not None and not isinstance(auto_delete, bool):
            raise TypeError(type(auto_delete))
        self.__auto_delete = auto_delete

    def with_auto_delete(self, auto_delete):
        """
        開封時自動削除を設定
        :param auto_delete: 開封時自動削除
        :type auto_delete: bool
        :return: this
        :rtype: CreateInboxRequest
        """
        self.set_auto_delete(auto_delete)
        return self

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
        if cooperation_url is not None and not (isinstance(cooperation_url, str) or isinstance(cooperation_url, unicode)):
            raise TypeError(type(cooperation_url))
        self.__cooperation_url = cooperation_url

    def with_cooperation_url(self, cooperation_url):
        """
        メッセージの開封通知先URLを設定
        :param cooperation_url: メッセージの開封通知先URL
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
        if receive_message_trigger_script is not None and not (isinstance(receive_message_trigger_script, str) or isinstance(receive_message_trigger_script, unicode)):
            raise TypeError(type(receive_message_trigger_script))
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
        if receive_message_done_trigger_script is not None and not (isinstance(receive_message_done_trigger_script, str) or isinstance(receive_message_done_trigger_script, unicode)):
            raise TypeError(type(receive_message_done_trigger_script))
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
        if read_message_trigger_script is not None and not (isinstance(read_message_trigger_script, str) or isinstance(read_message_trigger_script, unicode)):
            raise TypeError(type(read_message_trigger_script))
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
        if read_message_done_trigger_script is not None and not (isinstance(read_message_done_trigger_script, str) or isinstance(read_message_done_trigger_script, unicode)):
            raise TypeError(type(read_message_done_trigger_script))
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
        if delete_message_trigger_script is not None and not (isinstance(delete_message_trigger_script, str) or isinstance(delete_message_trigger_script, unicode)):
            raise TypeError(type(delete_message_trigger_script))
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
        if delete_message_done_trigger_script is not None and not (isinstance(delete_message_done_trigger_script, str) or isinstance(delete_message_done_trigger_script, unicode)):
            raise TypeError(type(delete_message_done_trigger_script))
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

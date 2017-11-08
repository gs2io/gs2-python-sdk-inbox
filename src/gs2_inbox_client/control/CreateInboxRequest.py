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
            self.__service_class = None
            self.__name = None
            self.__cooperation_url = None
            self.__auto_delete = None
        else:
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_cooperation_url(params['cooperationUrl'] if 'cooperationUrl' in params.keys() else None)
            self.set_auto_delete(params['autoDelete'] if 'autoDelete' in params.keys() else None)

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

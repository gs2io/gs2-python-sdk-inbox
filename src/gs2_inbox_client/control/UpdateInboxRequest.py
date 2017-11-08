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


class UpdateInboxRequest(Gs2BasicRequest):

    class Constant(Gs2Inbox):
        FUNCTION = "UpdateInbox"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateInboxRequest, self).__init__(params)
        if params is None:
            self.__inbox_name = None
            self.__service_class = None
            self.__cooperation_url = None
        else:
            self.set_inbox_name(params['inboxName'] if 'inboxName' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_cooperation_url(params['cooperationUrl'] if 'cooperationUrl' in params.keys() else None)

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
        self.__inbox_name = inbox_name

    def with_inbox_name(self, inbox_name):
        """
        受信ボックスの名前を指定します。を設定
        :param inbox_name: 受信ボックスの名前を指定します。
        :type inbox_name: unicode
        :return: this
        :rtype: UpdateInboxRequest
        """
        self.set_inbox_name(inbox_name)
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
        :rtype: UpdateInboxRequest
        """
        self.set_service_class(service_class)
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
        :rtype: UpdateInboxRequest
        """
        self.set_cooperation_url(cooperation_url)
        return self

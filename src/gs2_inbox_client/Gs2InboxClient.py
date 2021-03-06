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

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client
from aws_sdk_for_serverless.common import url_encoder


class Gs2InboxClient(AbstractGs2Client):

    ENDPOINT = "inbox"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2InboxClient, self).__init__(credential, region)

    def create_inbox(self, request):
        """
        受信ボックスを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.CreateInboxRequest.CreateInboxRequest
        :return: 結果
        :rtype: gs2_inbox_client.control.CreateInboxResult.CreateInboxResult
        """
        body = { 
            "name": request.get_name(),
            "serviceClass": request.get_service_class(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_auto_delete() is not None:
            body["autoDelete"] = request.get_auto_delete()
        if request.get_cooperation_url() is not None:
            body["cooperationUrl"] = request.get_cooperation_url()
        if request.get_receive_message_trigger_script() is not None:
            body["receiveMessageTriggerScript"] = request.get_receive_message_trigger_script()
        if request.get_receive_message_done_trigger_script() is not None:
            body["receiveMessageDoneTriggerScript"] = request.get_receive_message_done_trigger_script()
        if request.get_read_message_trigger_script() is not None:
            body["readMessageTriggerScript"] = request.get_read_message_trigger_script()
        if request.get_read_message_done_trigger_script() is not None:
            body["readMessageDoneTriggerScript"] = request.get_read_message_done_trigger_script()
        if request.get_delete_message_trigger_script() is not None:
            body["deleteMessageTriggerScript"] = request.get_delete_message_trigger_script()
        if request.get_delete_message_done_trigger_script() is not None:
            body["deleteMessageDoneTriggerScript"] = request.get_delete_message_done_trigger_script()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.CreateInboxRequest import CreateInboxRequest
        from gs2_inbox_client.control.CreateInboxResult import CreateInboxResult
        return CreateInboxResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox",
            service=self.ENDPOINT,
            component=CreateInboxRequest.Constant.MODULE,
            target_function=CreateInboxRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_inbox(self, request):
        """
        受信ボックスを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.DeleteInboxRequest.DeleteInboxRequest
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.DeleteInboxRequest import DeleteInboxRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox/" + str(("null" if request.get_inbox_name() is None or request.get_inbox_name() == "" else request.get_inbox_name())) + "",
            service=self.ENDPOINT,
            component=DeleteInboxRequest.Constant.MODULE,
            target_function=DeleteInboxRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_inbox(self, request):
        """
        受信ボックスの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.DescribeInboxRequest.DescribeInboxRequest
        :return: 結果
        :rtype: gs2_inbox_client.control.DescribeInboxResult.DescribeInboxResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.DescribeInboxRequest import DescribeInboxRequest

        from gs2_inbox_client.control.DescribeInboxResult import DescribeInboxResult
        return DescribeInboxResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox",
            service=self.ENDPOINT,
            component=DescribeInboxRequest.Constant.MODULE,
            target_function=DescribeInboxRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_service_class(self, request):
        """
        サービスクラスの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.DescribeServiceClassRequest.DescribeServiceClassRequest
        :return: 結果
        :rtype: gs2_inbox_client.control.DescribeServiceClassResult.DescribeServiceClassResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.DescribeServiceClassRequest import DescribeServiceClassRequest

        from gs2_inbox_client.control.DescribeServiceClassResult import DescribeServiceClassResult
        return DescribeServiceClassResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox/serviceClass",
            service=self.ENDPOINT,
            component=DescribeServiceClassRequest.Constant.MODULE,
            target_function=DescribeServiceClassRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_inbox(self, request):
        """
        受信ボックスを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.GetInboxRequest.GetInboxRequest
        :return: 結果
        :rtype: gs2_inbox_client.control.GetInboxResult.GetInboxResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.GetInboxRequest import GetInboxRequest

        from gs2_inbox_client.control.GetInboxResult import GetInboxResult
        return GetInboxResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox/" + str(("null" if request.get_inbox_name() is None or request.get_inbox_name() == "" else request.get_inbox_name())) + "",
            service=self.ENDPOINT,
            component=GetInboxRequest.Constant.MODULE,
            target_function=GetInboxRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_inbox_status(self, request):
        """
        受信ボックスの状態を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.GetInboxStatusRequest.GetInboxStatusRequest
        :return: 結果
        :rtype: gs2_inbox_client.control.GetInboxStatusResult.GetInboxStatusResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.GetInboxStatusRequest import GetInboxStatusRequest

        from gs2_inbox_client.control.GetInboxStatusResult import GetInboxStatusResult
        return GetInboxStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox/" + str(("null" if request.get_inbox_name() is None or request.get_inbox_name() == "" else request.get_inbox_name())) + "/status",
            service=self.ENDPOINT,
            component=GetInboxStatusRequest.Constant.MODULE,
            target_function=GetInboxStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_inbox(self, request):
        """
        受信ボックスを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.UpdateInboxRequest.UpdateInboxRequest
        :return: 結果
        :rtype: gs2_inbox_client.control.UpdateInboxResult.UpdateInboxResult
        """
        body = { 
        }
        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_service_class() is not None:
            body["serviceClass"] = request.get_service_class()
        if request.get_cooperation_url() is not None:
            body["cooperationUrl"] = request.get_cooperation_url()
        if request.get_receive_message_trigger_script() is not None:
            body["receiveMessageTriggerScript"] = request.get_receive_message_trigger_script()
        if request.get_receive_message_done_trigger_script() is not None:
            body["receiveMessageDoneTriggerScript"] = request.get_receive_message_done_trigger_script()
        if request.get_read_message_trigger_script() is not None:
            body["readMessageTriggerScript"] = request.get_read_message_trigger_script()
        if request.get_read_message_done_trigger_script() is not None:
            body["readMessageDoneTriggerScript"] = request.get_read_message_done_trigger_script()
        if request.get_delete_message_trigger_script() is not None:
            body["deleteMessageTriggerScript"] = request.get_delete_message_trigger_script()
        if request.get_delete_message_done_trigger_script() is not None:
            body["deleteMessageDoneTriggerScript"] = request.get_delete_message_done_trigger_script()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.UpdateInboxRequest import UpdateInboxRequest
        from gs2_inbox_client.control.UpdateInboxResult import UpdateInboxResult
        return UpdateInboxResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox/" + str(("null" if request.get_inbox_name() is None or request.get_inbox_name() == "" else request.get_inbox_name())) + "",
            service=self.ENDPOINT,
            component=UpdateInboxRequest.Constant.MODULE,
            target_function=UpdateInboxRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_message(self, request):
        """
        メッセージを削除します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.DeleteMessageRequest.DeleteMessageRequest
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.DeleteMessageRequest import DeleteMessageRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox/" + str(("null" if request.get_inbox_name() is None or request.get_inbox_name() == "" else request.get_inbox_name())) + "/message/" + str(("null" if request.get_message_id() is None or request.get_message_id() == "" else request.get_message_id())) + "",
            service=self.ENDPOINT,
            component=DeleteMessageRequest.Constant.MODULE,
            target_function=DeleteMessageRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def delete_messages(self, request):
        """
        複数のメッセージをまとめて削除します<br>
        <br>
        - 消費クオータ: 削除するメッセージの数 * 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.DeleteMessagesRequest.DeleteMessagesRequest
        """
        query_strings = {}
        if request.get_message_ids() is not None:
            query_strings['messageIds'] = u','.join(request.get_message_ids())
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.DeleteMessagesRequest import DeleteMessagesRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox/" + str(("null" if request.get_inbox_name() is None or request.get_inbox_name() == "" else request.get_inbox_name())) + "/message/multiple",
            service=self.ENDPOINT,
            component=DeleteMessagesRequest.Constant.MODULE,
            target_function=DeleteMessagesRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_message(self, request):
        """
        受信メッセージの一覧を取得します<br>
        <br>
        - 消費クオータ: 50件あたり5<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.DescribeMessageRequest.DescribeMessageRequest
        :return: 結果
        :rtype: gs2_inbox_client.control.DescribeMessageResult.DescribeMessageResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_access_token() is not None:
            headers["X-GS2-ACCESS-TOKEN"] = request.get_access_token()
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.DescribeMessageRequest import DescribeMessageRequest

        from gs2_inbox_client.control.DescribeMessageResult import DescribeMessageResult
        return DescribeMessageResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox/" + str(("null" if request.get_inbox_name() is None or request.get_inbox_name() == "" else request.get_inbox_name())) + "/message",
            service=self.ENDPOINT,
            component=DescribeMessageRequest.Constant.MODULE,
            target_function=DescribeMessageRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_message(self, request):
        """
        メッセージを取得します<br>
        <br>
        - 消費クオータ: 5<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.GetMessageRequest.GetMessageRequest
        :return: 結果
        :rtype: gs2_inbox_client.control.GetMessageResult.GetMessageResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.GetMessageRequest import GetMessageRequest

        from gs2_inbox_client.control.GetMessageResult import GetMessageResult
        return GetMessageResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox/" + str(("null" if request.get_inbox_name() is None or request.get_inbox_name() == "" else request.get_inbox_name())) + "/message/" + str(("null" if request.get_message_id() is None or request.get_message_id() == "" else request.get_message_id())) + "",
            service=self.ENDPOINT,
            component=GetMessageRequest.Constant.MODULE,
            target_function=GetMessageRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def read_message(self, request):
        """
        メッセージを開封します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.ReadMessageRequest.ReadMessageRequest
        :return: 結果
        :rtype: gs2_inbox_client.control.ReadMessageResult.ReadMessageResult
        """
        body = { 
        }

        headers = {}
        if request.get_access_token() is not None:
            headers["X-GS2-ACCESS-TOKEN"] = request.get_access_token()
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.ReadMessageRequest import ReadMessageRequest
        from gs2_inbox_client.control.ReadMessageResult import ReadMessageResult
        return ReadMessageResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox/" + str(("null" if request.get_inbox_name() is None or request.get_inbox_name() == "" else request.get_inbox_name())) + "/message/" + str(("null" if request.get_message_id() is None or request.get_message_id() == "" else request.get_message_id())) + "",
            service=self.ENDPOINT,
            component=ReadMessageRequest.Constant.MODULE,
            target_function=ReadMessageRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def read_messages(self, request):
        """
        複数のメッセージをまとめて開封します<br>
        <br>
        連携用URLと複数メッセージの開封処理を同時に利用する場合は、200レスポンスを応答すると、GS2側では指定されたすべてのメッセージを開封したことにします。<br>
        <br>
        200 以外のステータスコードを応答する場合はレスポンスボディにJSON形式で、<br>
        "success" というパラメータに開封に成功したメッセージIDのリストを返す必要があります。<br>
        success に指定されたメッセージIDのみ開封成功処理を行い、BadGateway(502)応答を返します。<br>
        <br>
        BadGateway(502) のレスポンスボディには、コールバックで返された値がそのまま含まれます。<br>
        例えば、メッセージにアイテムを添付されていたが、一部アイテムが所有できる上限を超えていたため開封できなかった。という場合<br>
        success にはアイテムを付与できたメッセージIDのみを応答し、reason など任意のパラメータでアイテムの所持上限を迎えたため<br>
        メッセージID hoge のメッセージは開封に失敗した。というようなレスポンスを返すことでクライアントにも開封に失敗した理由を伝えることができます。<br>
        <br>
        - 消費クオータ: 開封するメッセージの数 * 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.ReadMessagesRequest.ReadMessagesRequest
        :return: 結果
        :rtype: gs2_inbox_client.control.ReadMessagesResult.ReadMessagesResult
        """
        body = { 
            "messageIds": request.get_message_ids(),
        }

        headers = {}
        if request.get_access_token() is not None:
            headers["X-GS2-ACCESS-TOKEN"] = request.get_access_token()
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.ReadMessagesRequest import ReadMessagesRequest
        from gs2_inbox_client.control.ReadMessagesResult import ReadMessagesResult
        return ReadMessagesResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox/" + str(("null" if request.get_inbox_name() is None or request.get_inbox_name() == "" else request.get_inbox_name())) + "/message/multiple",
            service=self.ENDPOINT,
            component=ReadMessagesRequest.Constant.MODULE,
            target_function=ReadMessagesRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def send_message(self, request):
        """
        メッセージを送信します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_inbox_client.control.SendMessageRequest.SendMessageRequest
        :return: 結果
        :rtype: gs2_inbox_client.control.SendMessageResult.SendMessageResult
        """
        body = { 
            "userId": request.get_user_id(),
            "message": request.get_message(),
        }

        if request.get_cooperation() is not None:
            body["cooperation"] = request.get_cooperation()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_inbox_client.control.SendMessageRequest import SendMessageRequest
        from gs2_inbox_client.control.SendMessageResult import SendMessageResult
        return SendMessageResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inbox/" + str(("null" if request.get_inbox_name() is None or request.get_inbox_name() == "" else request.get_inbox_name())) + "/message",
            service=self.ENDPOINT,
            component=SendMessageRequest.Constant.MODULE,
            target_function=SendMessageRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

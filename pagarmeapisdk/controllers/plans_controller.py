# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.configuration import Server
from pagarmeapisdk.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from pagarmeapisdk.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from pagarmeapisdk.models.get_plan_response import GetPlanResponse
from pagarmeapisdk.models.get_plan_item_response import GetPlanItemResponse
from pagarmeapisdk.models.list_plans_response import ListPlansResponse


class PlansController(BaseController):

    """A Controller to access Endpoints in the pagarmeapisdk API."""
    def __init__(self, config):
        super(PlansController, self).__init__(config)

    def get_plan(self,
                 plan_id):
        """Does a GET request to /plans/{plan_id}.

        Gets a plan

        Args:
            plan_id (string): Plan id

        Returns:
            GetPlanResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/plans/{plan_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('plan_id')
                            .value(plan_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetPlanResponse.from_dictionary)
        ).execute()

    def update_plan(self,
                    plan_id,
                    request,
                    idempotency_key=None):
        """Does a PUT request to /plans/{plan_id}.

        Updates a plan

        Args:
            plan_id (string): Plan id
            request (UpdatePlanRequest): Request for updating a plan
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/plans/{plan_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('plan_id')
                            .value(plan_id)
                            .should_encode(True))
            .body_param(Parameter()
                        .value(request))
            .header_param(Parameter()
                          .key('idempotency-key')
                          .value(idempotency_key))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/json; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetPlanResponse.from_dictionary)
        ).execute()

    def update_plan_metadata(self,
                             plan_id,
                             request,
                             idempotency_key=None):
        """Does a PATCH request to /Plans/{plan_id}/metadata.

        Updates the metadata from a plan

        Args:
            plan_id (string): The plan id
            request (UpdateMetadataRequest): Request for updating the plan
                metadata
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/Plans/{plan_id}/metadata')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('plan_id')
                            .value(plan_id)
                            .should_encode(True))
            .body_param(Parameter()
                        .value(request))
            .header_param(Parameter()
                          .key('idempotency-key')
                          .value(idempotency_key))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/json; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetPlanResponse.from_dictionary)
        ).execute()

    def delete_plan_item(self,
                         plan_id,
                         plan_item_id,
                         idempotency_key=None):
        """Does a DELETE request to /plans/{plan_id}/items/{plan_item_id}.

        Removes an item from a plan

        Args:
            plan_id (string): Plan id
            plan_item_id (string): Plan item id
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanItemResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/plans/{plan_id}/items/{plan_item_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('plan_id')
                            .value(plan_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('plan_item_id')
                            .value(plan_item_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('idempotency-key')
                          .value(idempotency_key))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetPlanItemResponse.from_dictionary)
        ).execute()

    def get_plans(self,
                  page=None,
                  size=None,
                  name=None,
                  status=None,
                  billing_type=None,
                  created_since=None,
                  created_until=None):
        """Does a GET request to /plans.

        Gets all plans

        Args:
            page (int, optional): Page number
            size (int, optional): Page size
            name (string, optional): Filter for Plan's name
            status (string, optional): Filter for Plan's status
            billing_type (string, optional): Filter for plan's billing type
            created_since (datetime, optional): Filter for plan's creation
                date start range
            created_until (datetime, optional): Filter for plan's creation
                date end range

        Returns:
            ListPlansResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/plans')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('page')
                         .value(page))
            .query_param(Parameter()
                         .key('size')
                         .value(size))
            .query_param(Parameter()
                         .key('name')
                         .value(name))
            .query_param(Parameter()
                         .key('status')
                         .value(status))
            .query_param(Parameter()
                         .key('billing_type')
                         .value(billing_type))
            .query_param(Parameter()
                         .key('created_since')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_since)))
            .query_param(Parameter()
                         .key('created_until')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_until)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListPlansResponse.from_dictionary)
        ).execute()

    def get_plan_item(self,
                      plan_id,
                      plan_item_id):
        """Does a GET request to /plans/{plan_id}/items/{plan_item_id}.

        Gets a plan item

        Args:
            plan_id (string): Plan id
            plan_item_id (string): Plan item id

        Returns:
            GetPlanItemResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/plans/{plan_id}/items/{plan_item_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('plan_id')
                            .value(plan_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('plan_item_id')
                            .value(plan_item_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetPlanItemResponse.from_dictionary)
        ).execute()

    def delete_plan(self,
                    plan_id,
                    idempotency_key=None):
        """Does a DELETE request to /plans/{plan_id}.

        Deletes a plan

        Args:
            plan_id (string): Plan id
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/plans/{plan_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('plan_id')
                            .value(plan_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('idempotency-key')
                          .value(idempotency_key))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetPlanResponse.from_dictionary)
        ).execute()

    def update_plan_item(self,
                         plan_id,
                         plan_item_id,
                         body,
                         idempotency_key=None):
        """Does a PUT request to /plans/{plan_id}/items/{plan_item_id}.

        Updates a plan item

        Args:
            plan_id (string): Plan id
            plan_item_id (string): Plan item id
            body (UpdatePlanItemRequest): Request for updating the plan item
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanItemResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/plans/{plan_id}/items/{plan_item_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('plan_id')
                            .value(plan_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('plan_item_id')
                            .value(plan_item_id)
                            .should_encode(True))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('idempotency-key')
                          .value(idempotency_key))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/json; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetPlanItemResponse.from_dictionary)
        ).execute()

    def create_plan_item(self,
                         plan_id,
                         request,
                         idempotency_key=None):
        """Does a POST request to /plans/{plan_id}/items.

        Adds a new item to a plan

        Args:
            plan_id (string): Plan id
            request (CreatePlanItemRequest): Request for creating a plan item
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanItemResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/plans/{plan_id}/items')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('plan_id')
                            .value(plan_id)
                            .should_encode(True))
            .body_param(Parameter()
                        .value(request))
            .header_param(Parameter()
                          .key('idempotency-key')
                          .value(idempotency_key))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/json; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetPlanItemResponse.from_dictionary)
        ).execute()

    def create_plan(self,
                    body,
                    idempotency_key=None):
        """Does a POST request to /plans.

        Creates a new plan

        Args:
            body (CreatePlanRequest): Request for creating a plan
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/plans')
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('idempotency-key')
                          .value(idempotency_key))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/json; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetPlanResponse.from_dictionary)
        ).execute()

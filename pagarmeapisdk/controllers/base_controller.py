# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import platform
from apimatic_core.api_call import ApiCall
from apimatic_core.types.error_case import ErrorCase
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException


class BaseController(object):

    """All controllers inherit from this base class.

    Attributes:
        config (Configuration): The HttpClient which a specific controller
            instance will use. By default all the controller objects share
            the same HttpClient. A user can use his own custom HttpClient
            as well.
        http_call_back (HttpCallBack): An object which holds call back
            methods to be called before and after the execution of an HttpRequest.
        new_api_call_builder (APICall): Returns the API Call builder instance.
        auth_managers (dict): A dictionary which holds the instances of authentication managers.

    """

    @staticmethod
    def user_agent():
        return 'PagarmeApiSDK - Python 6.7.12'

    @staticmethod
    def user_agent_parameters():
        return {
        }

    @staticmethod
    def global_errors():
        return {
            'default': ErrorCase().error_message('HTTP response not OK.').exception_type(APIException),
            '400': ErrorCase().error_message('Invalid request').exception_type(ErrorException),
            '401': ErrorCase().error_message('Invalid API key').exception_type(ErrorException),
            '404': ErrorCase().error_message('An informed resource was not found').exception_type(ErrorException),
            '412': ErrorCase().error_message('Business validation error').exception_type(ErrorException),
            '422': ErrorCase().error_message('Contract validation error').exception_type(ErrorException),
            '500': ErrorCase().error_message('Internal server error').exception_type(ErrorException),
        }

    def __init__(self, config):
        self._global_config = config
        self._config = self._global_config.get_http_client_configuration()
        self._http_call_back = self.config.http_callback
        self.api_call = ApiCall(config)

    @property
    def config(self):
        return self._config

    @property
    def http_call_back(self):
        return self._http_call_back

    @property
    def new_api_call_builder(self):
        return self.api_call.new_builder

    @property
    def auth_managers(self):
        return self._global_config.get_auth_managers()

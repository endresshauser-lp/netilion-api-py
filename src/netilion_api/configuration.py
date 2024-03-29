# coding: utf-8

"""
    Netilion API Documentation

    Welcome to the Netilion API Documentation, which provides interactive access and documentation to our REST API. Please visit our developer portal for further instructions and information: https://developer.netilion.endress.com/   # noqa: E501

    OpenAPI spec version: 01.00.00
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import copy
import logging
import multiprocessing
import sys
import time
import urllib3

import six
from six.moves import http_client as httplib
from enum import Enum

from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session


class TypeWithDefault(type):
    def __init__(cls, name, bases, dct):
        super(TypeWithDefault, cls).__init__(name, bases, dct)
        cls._default = None

    def __call__(cls):
        if cls._default is None:
            cls._default = type.__call__(cls)
        return copy.copy(cls._default)

    def set_default(cls, default):
        cls._default = copy.copy(default)

class AuthType(Enum):
    BASIC = 1
    OAUTH_PASSWORD_GRANT = 2
    CUSTOM = 99

class OAuthPasswordGrant():
    """NOTE: You can inherit from this class in case this implementation 
    of OAuth 2.0 password grant type does not work for you.
    Alternatively you can use AuthType.CUSTOM to have full control over auth headers. 
    """
    def __init__(self, username, password, api_key, api_secret, oauth_token_url, prefix = 'Bearer '):
        # necessary parameters
        self._username = username
        self._password = password
        self._api_key = api_key
        self._api_secret = api_secret
        self._oauth_token_url = oauth_token_url

        # optional parameters
        self._prefix = prefix

        # internal variables
        self._token = None
        self._oauth = OAuth2Session(client=LegacyApplicationClient(client_id=self._api_key))

    def get_token(self):
        """Gets HTTP oauth 2.0 password grant type authentication header (string).

        :return: The token for oauth 2.0 grant type HTTP authentication.
        """
        if not self._token:
            self._token = self._fetch_token()
        else: 
            token_expiry = self._token["created_at"] + self._token["expires_in"]
            token_expired = token_expiry <= time.time()
            if token_expired:
                self._token = self._refresh_token()
        token = self._prefix + self._token["access_token"]
        return token

    def _fetch_token(self):
        headers = {
            "API-Key": self._api_key,
            "Content-Type": "application/x-www-form-urlencoded",
        }
        token =  self._oauth.fetch_token(token_url=self._oauth_token_url,
                                       username=self._username, password=self._password, client_id=self._api_key,
                                       client_secret=self._api_secret, include_client_id=True, headers=headers)
        return token

    def _refresh_token(self, **kwargs):
        kwargs["client_id"] = self._api_key
        kwargs["client_secret"] = self._api_secret
        return self._oauth.refresh_token(self._oauth_token_url, **kwargs)

class Configuration(six.with_metaclass(TypeWithDefault, object)):
    """NOTE: This class is auto generated by the swagger code generator program.

    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.
    """

    def __init__(self):
        """Constructor"""
        # Default Base url
        self.host = "/v1"
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # Select auth type
        self.auth_type = AuthType.BASIC
        ######################### 
        # BASIC
        # Do not encapsulate basic in a class to stay backwards-compatible
        #########################
        # dict to store API key(s)
        self.api_key = {}
        # dict to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}
        # function to refresh API key if expired
        self.refresh_api_key_hook = None
        # Username for HTTP basic authentication
        self.username = ""
        # Password for HTTP basic authentication
        self.password = ""
        ######################### 
        # OAuth 2.0 Password Grant 
        # https://oauth.net/2/grant-types/password/
        #########################
        self.oauth_password_grant: OAuthPasswordGrant = None
        ######################### 
        # Custom hook to get Auth dictionary header
        #########################
        self.get_auth_settings_hook = None
        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("netilion_api")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API
        # from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        self.assert_hostname = None

        # urllib3 connection pool's maximum number of connections saved
        # per pool. urllib3 uses 1 connection as default value, but this is
        # not the best value when you are making a lot of possibly parallel
        # requests to the same host, which is often the case here.
        # cpu_count * 5 is used as default value to increase performance.
        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5

        # Proxy URL
        self.proxy = None
        # Safe chars for path_param
        self.safe_chars_for_path_param = ''

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.refresh_api_key_hook:
            self.refresh_api_key_hook(self)

        key = self.api_key.get(identifier)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        return urllib3.util.make_headers(
            basic_auth=self.username + ':' + self.password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        if self.auth_type == AuthType.BASIC:
            return {
                'API-Key':
                    {
                        'type': 'api_key',
                        'in': 'header',
                        'key': 'API-Key',
                        'value': self.get_api_key_with_prefix('API-Key')
                    },
                'Authentication':
                    {
                        'type': 'basic',
                        'in': 'header',
                        'key': 'Authorization',
                        'value': self.get_basic_auth_token()
                    },
            }
        elif self.auth_type == AuthType.OAUTH_PASSWORD_GRANT:
            if not self.oauth_password_grant:
                raise RuntimeError('Oauth grant type credentials need to be provided, please initialize oauth_password_grant.')
            return {
                'Authentication':
                {
                    'type': 'oauth_password_grant',
                    'in': 'header',
                    'key': 'Authorization',
                    'value': self.oauth_password_grant.get_token()
                },
            }
        elif self.auth_type == AuthType.CUSTOM:
            if not self.get_auth_settings_hook:
                raise RuntimeError('Please provide a get_auth_settings_hook returning authentication headers, see basic implementation here for an example.')
            return self.get_auth_settings_hook(self)
        else:
            msg = "Auth type {} is not supported".format(self.auth_type)
            raise ValueError(msg)

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 01.00.00\n"\
               "SDK Package Version: 01.02.02".\
               format(env=sys.platform, pyversion=sys.version)

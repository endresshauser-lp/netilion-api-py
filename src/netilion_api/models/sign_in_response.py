# coding: utf-8

"""
    Netilion API Documentation

    Welcome to the Netilion API Documentation, which provides interactive access and documentation to our REST API. Please visit our developer portal for further instructions and information: https://developer.netilion.endress.com/   # noqa: E501

    OpenAPI spec version: 01.00.00
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SignInResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'time': 'str',
        'application': 'str',
        'ip': 'str',
        'browser_name': 'str',
        'browser_version': 'str',
        'device_type': 'str',
        'platform_name': 'str',
        'platform_version': 'str',
        'client_application': 'NestedIDHrefName'
    }

    attribute_map = {
        'time': 'time',
        'application': 'application',
        'ip': 'ip',
        'browser_name': 'browser_name',
        'browser_version': 'browser_version',
        'device_type': 'device_type',
        'platform_name': 'platform_name',
        'platform_version': 'platform_version',
        'client_application': 'client_application'
    }

    def __init__(self, time=None, application=None, ip=None, browser_name=None, browser_version=None, device_type=None, platform_name=None, platform_version=None, client_application=None):  # noqa: E501
        """SignInResponse - a model defined in Swagger"""  # noqa: E501
        self._time = None
        self._application = None
        self._ip = None
        self._browser_name = None
        self._browser_version = None
        self._device_type = None
        self._platform_name = None
        self._platform_version = None
        self._client_application = None
        self.discriminator = None
        self.time = time
        self.application = application
        self.ip = ip
        if browser_name is not None:
            self.browser_name = browser_name
        if browser_version is not None:
            self.browser_version = browser_version
        if device_type is not None:
            self.device_type = device_type
        if platform_name is not None:
            self.platform_name = platform_name
        if platform_version is not None:
            self.platform_version = platform_version
        if client_application is not None:
            self.client_application = client_application

    @property
    def time(self):
        """Gets the time of this SignInResponse.  # noqa: E501

        time at which the user signed in  # noqa: E501

        :return: The time of this SignInResponse.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SignInResponse.

        time at which the user signed in  # noqa: E501

        :param time: The time of this SignInResponse.  # noqa: E501
        :type: str
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def application(self):
        """Gets the application of this SignInResponse.  # noqa: E501

        name of the application the user signed in  # noqa: E501

        :return: The application of this SignInResponse.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this SignInResponse.

        name of the application the user signed in  # noqa: E501

        :param application: The application of this SignInResponse.  # noqa: E501
        :type: str
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def ip(self):
        """Gets the ip of this SignInResponse.  # noqa: E501

        remote ip used by the user  # noqa: E501

        :return: The ip of this SignInResponse.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this SignInResponse.

        remote ip used by the user  # noqa: E501

        :param ip: The ip of this SignInResponse.  # noqa: E501
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def browser_name(self):
        """Gets the browser_name of this SignInResponse.  # noqa: E501

        name of the used browser  # noqa: E501

        :return: The browser_name of this SignInResponse.  # noqa: E501
        :rtype: str
        """
        return self._browser_name

    @browser_name.setter
    def browser_name(self, browser_name):
        """Sets the browser_name of this SignInResponse.

        name of the used browser  # noqa: E501

        :param browser_name: The browser_name of this SignInResponse.  # noqa: E501
        :type: str
        """

        self._browser_name = browser_name

    @property
    def browser_version(self):
        """Gets the browser_version of this SignInResponse.  # noqa: E501

        version of the used browser  # noqa: E501

        :return: The browser_version of this SignInResponse.  # noqa: E501
        :rtype: str
        """
        return self._browser_version

    @browser_version.setter
    def browser_version(self, browser_version):
        """Sets the browser_version of this SignInResponse.

        version of the used browser  # noqa: E501

        :param browser_version: The browser_version of this SignInResponse.  # noqa: E501
        :type: str
        """

        self._browser_version = browser_version

    @property
    def device_type(self):
        """Gets the device_type of this SignInResponse.  # noqa: E501

        type of the used device (desktop, tablet or mobile)  # noqa: E501

        :return: The device_type of this SignInResponse.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this SignInResponse.

        type of the used device (desktop, tablet or mobile)  # noqa: E501

        :param device_type: The device_type of this SignInResponse.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def platform_name(self):
        """Gets the platform_name of this SignInResponse.  # noqa: E501

        name of the used platform  # noqa: E501

        :return: The platform_name of this SignInResponse.  # noqa: E501
        :rtype: str
        """
        return self._platform_name

    @platform_name.setter
    def platform_name(self, platform_name):
        """Sets the platform_name of this SignInResponse.

        name of the used platform  # noqa: E501

        :param platform_name: The platform_name of this SignInResponse.  # noqa: E501
        :type: str
        """

        self._platform_name = platform_name

    @property
    def platform_version(self):
        """Gets the platform_version of this SignInResponse.  # noqa: E501

        version of the used platform  # noqa: E501

        :return: The platform_version of this SignInResponse.  # noqa: E501
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """Sets the platform_version of this SignInResponse.

        version of the used platform  # noqa: E501

        :param platform_version: The platform_version of this SignInResponse.  # noqa: E501
        :type: str
        """

        self._platform_version = platform_version

    @property
    def client_application(self):
        """Gets the client_application of this SignInResponse.  # noqa: E501


        :return: The client_application of this SignInResponse.  # noqa: E501
        :rtype: NestedIDHrefName
        """
        return self._client_application

    @client_application.setter
    def client_application(self, client_application):
        """Sets the client_application of this SignInResponse.


        :param client_application: The client_application of this SignInResponse.  # noqa: E501
        :type: NestedIDHrefName
        """

        self._client_application = client_application

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SignInResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SignInResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

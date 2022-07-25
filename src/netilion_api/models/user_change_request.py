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

from netilion_api.configuration import Configuration


class UserChangeRequest(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'disabled': 'bool',
        'address': 'UserAddressRequest'
    }

    attribute_map = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'disabled': 'disabled',
        'address': 'address'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, first_name=None, last_name=None, disabled=False, address=None, _configuration=None):  # noqa: E501
        """UserChangeRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._first_name = None
        self._last_name = None
        self._disabled = None
        self._address = None
        self.discriminator = 'userChangeRequest'

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if disabled is not None:
            self.disabled = disabled
        if address is not None:
            self.address = address

    @property
    def first_name(self):
        """Gets the first_name of this UserChangeRequest.  # noqa: E501


        :return: The first_name of this UserChangeRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserChangeRequest.


        :param first_name: The first_name of this UserChangeRequest.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserChangeRequest.  # noqa: E501


        :return: The last_name of this UserChangeRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserChangeRequest.


        :param last_name: The last_name of this UserChangeRequest.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def disabled(self):
        """Gets the disabled of this UserChangeRequest.  # noqa: E501

        Disables user from acces. Can be set by the user, but cannot be undone without an administrator.  # noqa: E501

        :return: The disabled of this UserChangeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this UserChangeRequest.

        Disables user from acces. Can be set by the user, but cannot be undone without an administrator.  # noqa: E501

        :param disabled: The disabled of this UserChangeRequest.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def address(self):
        """Gets the address of this UserChangeRequest.  # noqa: E501


        :return: The address of this UserChangeRequest.  # noqa: E501
        :rtype: UserAddressRequest
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this UserChangeRequest.


        :param address: The address of this UserChangeRequest.  # noqa: E501
        :type: UserAddressRequest
        """

        self._address = address

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(UserChangeRequest, dict):
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
        if not isinstance(other, UserChangeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserChangeRequest):
            return True

        return self.to_dict() != other.to_dict()

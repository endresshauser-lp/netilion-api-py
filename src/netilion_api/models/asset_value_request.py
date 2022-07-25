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


class AssetValueRequest(object):
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
        'key': 'str',
        'unit': 'NestedIDCode',
        'group': 'str',
        'data': 'list[AssetValueRequestData]'
    }

    attribute_map = {
        'key': 'key',
        'unit': 'unit',
        'group': 'group',
        'data': 'data'
    }

    def __init__(self, key=None, unit=None, group=None, data=None, _configuration=None):  # noqa: E501
        """AssetValueRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._unit = None
        self._group = None
        self._data = None
        self.discriminator = None

        self.key = key
        self.unit = unit
        if group is not None:
            self.group = group
        if data is not None:
            self.data = data

    @property
    def key(self):
        """Gets the key of this AssetValueRequest.  # noqa: E501


        :return: The key of this AssetValueRequest.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AssetValueRequest.


        :param key: The key of this AssetValueRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def unit(self):
        """Gets the unit of this AssetValueRequest.  # noqa: E501


        :return: The unit of this AssetValueRequest.  # noqa: E501
        :rtype: NestedIDCode
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this AssetValueRequest.


        :param unit: The unit of this AssetValueRequest.  # noqa: E501
        :type: NestedIDCode
        """
        if self._configuration.client_side_validation and unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

    @property
    def group(self):
        """Gets the group of this AssetValueRequest.  # noqa: E501


        :return: The group of this AssetValueRequest.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this AssetValueRequest.


        :param group: The group of this AssetValueRequest.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def data(self):
        """Gets the data of this AssetValueRequest.  # noqa: E501


        :return: The data of this AssetValueRequest.  # noqa: E501
        :rtype: list[AssetValueRequestData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AssetValueRequest.


        :param data: The data of this AssetValueRequest.  # noqa: E501
        :type: list[AssetValueRequestData]
        """

        self._data = data

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
        if issubclass(AssetValueRequest, dict):
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
        if not isinstance(other, AssetValueRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetValueRequest):
            return True

        return self.to_dict() != other.to_dict()

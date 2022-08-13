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

class AssetKeyValueObjectsResponse(object):
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
        'data': 'list[AssetKeyValueObjectsData]',
        'pagination': 'AssetValueObjectsPagination'
    }

    attribute_map = {
        'key': 'key',
        'data': 'data',
        'pagination': 'pagination'
    }

    def __init__(self, key=None, data=None, pagination=None):  # noqa: E501
        """AssetKeyValueObjectsResponse - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._data = None
        self._pagination = None
        self.discriminator = None
        self.key = key
        if data is not None:
            self.data = data
        self.pagination = pagination

    @property
    def key(self):
        """Gets the key of this AssetKeyValueObjectsResponse.  # noqa: E501

        key of the asset value object  # noqa: E501

        :return: The key of this AssetKeyValueObjectsResponse.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AssetKeyValueObjectsResponse.

        key of the asset value object  # noqa: E501

        :param key: The key of this AssetKeyValueObjectsResponse.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def data(self):
        """Gets the data of this AssetKeyValueObjectsResponse.  # noqa: E501


        :return: The data of this AssetKeyValueObjectsResponse.  # noqa: E501
        :rtype: list[AssetKeyValueObjectsData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AssetKeyValueObjectsResponse.


        :param data: The data of this AssetKeyValueObjectsResponse.  # noqa: E501
        :type: list[AssetKeyValueObjectsData]
        """

        self._data = data

    @property
    def pagination(self):
        """Gets the pagination of this AssetKeyValueObjectsResponse.  # noqa: E501


        :return: The pagination of this AssetKeyValueObjectsResponse.  # noqa: E501
        :rtype: AssetValueObjectsPagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this AssetKeyValueObjectsResponse.


        :param pagination: The pagination of this AssetKeyValueObjectsResponse.  # noqa: E501
        :type: AssetValueObjectsPagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")  # noqa: E501

        self._pagination = pagination

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
        if issubclass(AssetKeyValueObjectsResponse, dict):
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
        if not isinstance(other, AssetKeyValueObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
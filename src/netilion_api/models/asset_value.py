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

class AssetValue(object):
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
        'unit': 'NestedID',
        'group': 'str',
        'timestamp': 'str',
        'value': 'float'
    }

    attribute_map = {
        'key': 'key',
        'unit': 'unit',
        'group': 'group',
        'timestamp': 'timestamp',
        'value': 'value'
    }

    def __init__(self, key=None, unit=None, group=None, timestamp=None, value=None):  # noqa: E501
        """AssetValue - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._unit = None
        self._group = None
        self._timestamp = None
        self._value = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if unit is not None:
            self.unit = unit
        if group is not None:
            self.group = group
        if timestamp is not None:
            self.timestamp = timestamp
        if value is not None:
            self.value = value

    @property
    def key(self):
        """Gets the key of this AssetValue.  # noqa: E501

        key of the asset value  # noqa: E501

        :return: The key of this AssetValue.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AssetValue.

        key of the asset value  # noqa: E501

        :param key: The key of this AssetValue.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def unit(self):
        """Gets the unit of this AssetValue.  # noqa: E501


        :return: The unit of this AssetValue.  # noqa: E501
        :rtype: NestedID
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this AssetValue.


        :param unit: The unit of this AssetValue.  # noqa: E501
        :type: NestedID
        """

        self._unit = unit

    @property
    def group(self):
        """Gets the group of this AssetValue.  # noqa: E501

        group of the asset value.  # noqa: E501

        :return: The group of this AssetValue.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this AssetValue.

        group of the asset value.  # noqa: E501

        :param group: The group of this AssetValue.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def timestamp(self):
        """Gets the timestamp of this AssetValue.  # noqa: E501

        timestamp of the value  # noqa: E501

        :return: The timestamp of this AssetValue.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AssetValue.

        timestamp of the value  # noqa: E501

        :param timestamp: The timestamp of this AssetValue.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def value(self):
        """Gets the value of this AssetValue.  # noqa: E501

        value / aggregated value  # noqa: E501

        :return: The value of this AssetValue.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AssetValue.

        value / aggregated value  # noqa: E501

        :param value: The value of this AssetValue.  # noqa: E501
        :type: float
        """

        self._value = value

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
        if issubclass(AssetValue, dict):
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
        if not isinstance(other, AssetValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
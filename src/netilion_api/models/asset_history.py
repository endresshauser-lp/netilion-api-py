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

class AssetHistory(object):
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
        'asset': 'AssetHistoryBase',
        '_datetime': 'datetime'
    }

    attribute_map = {
        'asset': 'asset',
        '_datetime': 'datetime'
    }

    def __init__(self, asset=None, _datetime=None):  # noqa: E501
        """AssetHistory - a model defined in Swagger"""  # noqa: E501
        self._asset = None
        self.__datetime = None
        self.discriminator = None
        self.asset = asset
        self._datetime = _datetime

    @property
    def asset(self):
        """Gets the asset of this AssetHistory.  # noqa: E501


        :return: The asset of this AssetHistory.  # noqa: E501
        :rtype: AssetHistoryBase
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this AssetHistory.


        :param asset: The asset of this AssetHistory.  # noqa: E501
        :type: AssetHistoryBase
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def _datetime(self):
        """Gets the _datetime of this AssetHistory.  # noqa: E501

        Date and time when the asset was changed  # noqa: E501

        :return: The _datetime of this AssetHistory.  # noqa: E501
        :rtype: datetime
        """
        return self.__datetime

    @_datetime.setter
    def _datetime(self, _datetime):
        """Sets the _datetime of this AssetHistory.

        Date and time when the asset was changed  # noqa: E501

        :param _datetime: The _datetime of this AssetHistory.  # noqa: E501
        :type: datetime
        """
        if _datetime is None:
            raise ValueError("Invalid value for `_datetime`, must not be `None`")  # noqa: E501

        self.__datetime = _datetime

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
        if issubclass(AssetHistory, dict):
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
        if not isinstance(other, AssetHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
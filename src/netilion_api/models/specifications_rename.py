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

class SpecificationsRename(object):
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
        'old_key': 'str'
    }

    attribute_map = {
        'old_key': 'old_key'
    }

    def __init__(self, old_key=None):  # noqa: E501
        """SpecificationsRename - a model defined in Swagger"""  # noqa: E501
        self._old_key = None
        self.discriminator = None
        self.old_key = old_key

    @property
    def old_key(self):
        """Gets the old_key of this SpecificationsRename.  # noqa: E501

        the value is the old_keys' new name  # noqa: E501

        :return: The old_key of this SpecificationsRename.  # noqa: E501
        :rtype: str
        """
        return self._old_key

    @old_key.setter
    def old_key(self, old_key):
        """Sets the old_key of this SpecificationsRename.

        the value is the old_keys' new name  # noqa: E501

        :param old_key: The old_key of this SpecificationsRename.  # noqa: E501
        :type: str
        """
        if old_key is None:
            raise ValueError("Invalid value for `old_key`, must not be `None`")  # noqa: E501

        self._old_key = old_key

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
        if issubclass(SpecificationsRename, dict):
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
        if not isinstance(other, SpecificationsRename):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

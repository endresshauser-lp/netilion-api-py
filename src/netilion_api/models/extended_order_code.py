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

class ExtendedOrderCode(object):
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
        'extended_order_code': 'str'
    }

    attribute_map = {
        'extended_order_code': 'extended_order_code'
    }

    def __init__(self, extended_order_code=None):  # noqa: E501
        """ExtendedOrderCode - a model defined in Swagger"""  # noqa: E501
        self._extended_order_code = None
        self.discriminator = None
        if extended_order_code is not None:
            self.extended_order_code = extended_order_code

    @property
    def extended_order_code(self):
        """Gets the extended_order_code of this ExtendedOrderCode.  # noqa: E501

        Extended order code  # noqa: E501

        :return: The extended_order_code of this ExtendedOrderCode.  # noqa: E501
        :rtype: str
        """
        return self._extended_order_code

    @extended_order_code.setter
    def extended_order_code(self, extended_order_code):
        """Sets the extended_order_code of this ExtendedOrderCode.

        Extended order code  # noqa: E501

        :param extended_order_code: The extended_order_code of this ExtendedOrderCode.  # noqa: E501
        :type: str
        """

        self._extended_order_code = extended_order_code

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
        if issubclass(ExtendedOrderCode, dict):
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
        if not isinstance(other, ExtendedOrderCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

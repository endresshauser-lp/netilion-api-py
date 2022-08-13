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

class CustomerBase(object):
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
        'number': 'str',
        'name': 'str'
    }

    attribute_map = {
        'number': 'number',
        'name': 'name'
    }

    discriminator_value_class_map = {
          'CustomerResponse': 'CustomerResponse',
'CustomerRequest': 'CustomerRequest'    }

    def __init__(self, number=None, name=None):  # noqa: E501
        """CustomerBase - a model defined in Swagger"""  # noqa: E501
        self._number = None
        self._name = None
        self.discriminator = 'customerBaseType'
        if number is not None:
            self.number = number
        if name is not None:
            self.name = name

    @property
    def number(self):
        """Gets the number of this CustomerBase.  # noqa: E501

        customer number  # noqa: E501

        :return: The number of this CustomerBase.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CustomerBase.

        customer number  # noqa: E501

        :param number: The number of this CustomerBase.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def name(self):
        """Gets the name of this CustomerBase.  # noqa: E501

        Name of the customer  # noqa: E501

        :return: The name of this CustomerBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomerBase.

        Name of the customer  # noqa: E501

        :param name: The name of this CustomerBase.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(CustomerBase, dict):
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
        if not isinstance(other, CustomerBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
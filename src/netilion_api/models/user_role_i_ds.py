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

class UserRoleIDs(object):
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
        'userroles': 'list[NestedID]'
    }

    attribute_map = {
        'userroles': 'userroles'
    }

    def __init__(self, userroles=None):  # noqa: E501
        """UserRoleIDs - a model defined in Swagger"""  # noqa: E501
        self._userroles = None
        self.discriminator = None
        self.userroles = userroles

    @property
    def userroles(self):
        """Gets the userroles of this UserRoleIDs.  # noqa: E501


        :return: The userroles of this UserRoleIDs.  # noqa: E501
        :rtype: list[NestedID]
        """
        return self._userroles

    @userroles.setter
    def userroles(self, userroles):
        """Sets the userroles of this UserRoleIDs.


        :param userroles: The userroles of this UserRoleIDs.  # noqa: E501
        :type: list[NestedID]
        """
        if userroles is None:
            raise ValueError("Invalid value for `userroles`, must not be `None`")  # noqa: E501

        self._userroles = userroles

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
        if issubclass(UserRoleIDs, dict):
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
        if not isinstance(other, UserRoleIDs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
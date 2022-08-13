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

class TechnicalUserBase(object):
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
        'email': 'str',
        'disabled': 'bool'
    }

    attribute_map = {
        'email': 'email',
        'disabled': 'disabled'
    }

    discriminator_value_class_map = {
          'TechnicalUserCreateResponse': 'TechnicalUserCreateResponse',
'TechnicalUserRequest': 'TechnicalUserRequest',
'TechnicalUserResponse': 'TechnicalUserResponse'    }

    def __init__(self, email=None, disabled=False):  # noqa: E501
        """TechnicalUserBase - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._disabled = None
        self.discriminator = 'technicalUserBaseType'
        self.email = email
        if disabled is not None:
            self.disabled = disabled

    @property
    def email(self):
        """Gets the email of this TechnicalUserBase.  # noqa: E501

        needs to be a valid email address  # noqa: E501

        :return: The email of this TechnicalUserBase.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TechnicalUserBase.

        needs to be a valid email address  # noqa: E501

        :param email: The email of this TechnicalUserBase.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def disabled(self):
        """Gets the disabled of this TechnicalUserBase.  # noqa: E501

        Disables user from access. Can be set by the user, but cannot be undone without an administrator.  # noqa: E501

        :return: The disabled of this TechnicalUserBase.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this TechnicalUserBase.

        Disables user from access. Can be set by the user, but cannot be undone without an administrator.  # noqa: E501

        :param disabled: The disabled of this TechnicalUserBase.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

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
        if issubclass(TechnicalUserBase, dict):
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
        if not isinstance(other, TechnicalUserBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
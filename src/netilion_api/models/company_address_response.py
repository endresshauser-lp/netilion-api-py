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
from netilion_api.models.address_base import AddressBase  # noqa: F401,E501

class CompanyAddressResponse(AddressBase):
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
        'email': 'str',
        'country_name': 'str'
    }
    if hasattr(AddressBase, "swagger_types"):
        swagger_types.update(AddressBase.swagger_types)

    attribute_map = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'country_name': 'country_name'
    }
    if hasattr(AddressBase, "attribute_map"):
        attribute_map.update(AddressBase.attribute_map)

    def __init__(self, first_name=None, last_name=None, email=None, country_name=None, *args, **kwargs):  # noqa: E501
        """CompanyAddressResponse - a model defined in Swagger"""  # noqa: E501
        self._first_name = None
        self._last_name = None
        self._email = None
        self._country_name = None
        self.discriminator = None
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if country_name is not None:
            self.country_name = country_name
        AddressBase.__init__(self, *args, **kwargs)

    @property
    def first_name(self):
        """Gets the first_name of this CompanyAddressResponse.  # noqa: E501

        first_name  # noqa: E501

        :return: The first_name of this CompanyAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CompanyAddressResponse.

        first_name  # noqa: E501

        :param first_name: The first_name of this CompanyAddressResponse.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CompanyAddressResponse.  # noqa: E501

        last_name  # noqa: E501

        :return: The last_name of this CompanyAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CompanyAddressResponse.

        last_name  # noqa: E501

        :param last_name: The last_name of this CompanyAddressResponse.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this CompanyAddressResponse.  # noqa: E501

        email  # noqa: E501

        :return: The email of this CompanyAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CompanyAddressResponse.

        email  # noqa: E501

        :param email: The email of this CompanyAddressResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def country_name(self):
        """Gets the country_name of this CompanyAddressResponse.  # noqa: E501

        name of the country  # noqa: E501

        :return: The country_name of this CompanyAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this CompanyAddressResponse.

        name of the country  # noqa: E501

        :param country_name: The country_name of this CompanyAddressResponse.  # noqa: E501
        :type: str
        """

        self._country_name = country_name

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
        if issubclass(CompanyAddressResponse, dict):
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
        if not isinstance(other, CompanyAddressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

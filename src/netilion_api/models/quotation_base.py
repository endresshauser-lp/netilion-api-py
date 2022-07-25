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


class QuotationBase(object):
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
        'name': 'str',
        '_date': 'str',
        'description': 'str'
    }

    attribute_map = {
        'number': 'number',
        'name': 'name',
        '_date': 'date',
        'description': 'description'
    }

    discriminator_value_class_map = {
        'QuotationRequest': 'QuotationRequest',
        'QuotationResponse': 'QuotationResponse'
    }

    def __init__(self, number=None, name=None, _date=None, description=None, _configuration=None):  # noqa: E501
        """QuotationBase - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._number = None
        self._name = None
        self.__date = None
        self._description = None
        self.discriminator = 'quotationBaseType'

        self.number = number
        self.name = name
        if _date is not None:
            self._date = _date
        if description is not None:
            self.description = description

    @property
    def number(self):
        """Gets the number of this QuotationBase.  # noqa: E501


        :return: The number of this QuotationBase.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this QuotationBase.


        :param number: The number of this QuotationBase.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def name(self):
        """Gets the name of this QuotationBase.  # noqa: E501


        :return: The name of this QuotationBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QuotationBase.


        :param name: The name of this QuotationBase.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def _date(self):
        """Gets the _date of this QuotationBase.  # noqa: E501

        Date must be in format '2016-01-01'  # noqa: E501

        :return: The _date of this QuotationBase.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this QuotationBase.

        Date must be in format '2016-01-01'  # noqa: E501

        :param _date: The _date of this QuotationBase.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def description(self):
        """Gets the description of this QuotationBase.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this QuotationBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QuotationBase.

        Description  # noqa: E501

        :param description: The description of this QuotationBase.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(QuotationBase, dict):
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
        if not isinstance(other, QuotationBase):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuotationBase):
            return True

        return self.to_dict() != other.to_dict()

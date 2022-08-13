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

class BillOfMaterialBase(object):
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
        'name': 'str',
        'description': 'str',
        '_date': 'str',
        'author': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        '_date': 'date',
        'author': 'author'
    }

    discriminator_value_class_map = {
          'BillOfMaterialResponse': 'BillOfMaterialResponse',
'BillOfMaterialRequest': 'BillOfMaterialRequest'    }

    def __init__(self, name=None, description=None, _date=None, author=None):  # noqa: E501
        """BillOfMaterialBase - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self.__date = None
        self._author = None
        self.discriminator = 'billOfMaterialBaseType'
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if _date is not None:
            self._date = _date
        if author is not None:
            self.author = author

    @property
    def name(self):
        """Gets the name of this BillOfMaterialBase.  # noqa: E501

        Bill of material name  # noqa: E501

        :return: The name of this BillOfMaterialBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BillOfMaterialBase.

        Bill of material name  # noqa: E501

        :param name: The name of this BillOfMaterialBase.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this BillOfMaterialBase.  # noqa: E501

        description text of the Instrumentation  # noqa: E501

        :return: The description of this BillOfMaterialBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BillOfMaterialBase.

        description text of the Instrumentation  # noqa: E501

        :param description: The description of this BillOfMaterialBase.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def _date(self):
        """Gets the _date of this BillOfMaterialBase.  # noqa: E501

        Date must be in format '2016-01-01'  # noqa: E501

        :return: The _date of this BillOfMaterialBase.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this BillOfMaterialBase.

        Date must be in format '2016-01-01'  # noqa: E501

        :param _date: The _date of this BillOfMaterialBase.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def author(self):
        """Gets the author of this BillOfMaterialBase.  # noqa: E501

        Author who created the bill of material  # noqa: E501

        :return: The author of this BillOfMaterialBase.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this BillOfMaterialBase.

        Author who created the bill of material  # noqa: E501

        :param author: The author of this BillOfMaterialBase.  # noqa: E501
        :type: str
        """

        self._author = author

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
        if issubclass(BillOfMaterialBase, dict):
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
        if not isinstance(other, BillOfMaterialBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
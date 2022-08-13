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

class NestedIDHrefSerialnumber(object):
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
        'id': 'int',
        'href': 'str',
        'serial_number': 'str'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'serial_number': 'serial_number'
    }

    def __init__(self, id=None, href=None, serial_number=None):  # noqa: E501
        """NestedIDHrefSerialnumber - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._serial_number = None
        self.discriminator = None
        self.id = id
        self.href = href
        self.serial_number = serial_number

    @property
    def id(self):
        """Gets the id of this NestedIDHrefSerialnumber.  # noqa: E501

        ID of the nested resources  # noqa: E501

        :return: The id of this NestedIDHrefSerialnumber.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NestedIDHrefSerialnumber.

        ID of the nested resources  # noqa: E501

        :param id: The id of this NestedIDHrefSerialnumber.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this NestedIDHrefSerialnumber.  # noqa: E501

        href to the nested resource  # noqa: E501

        :return: The href of this NestedIDHrefSerialnumber.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this NestedIDHrefSerialnumber.

        href to the nested resource  # noqa: E501

        :param href: The href of this NestedIDHrefSerialnumber.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def serial_number(self):
        """Gets the serial_number of this NestedIDHrefSerialnumber.  # noqa: E501

        serial number of the nested resource  # noqa: E501

        :return: The serial_number of this NestedIDHrefSerialnumber.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this NestedIDHrefSerialnumber.

        serial number of the nested resource  # noqa: E501

        :param serial_number: The serial_number of this NestedIDHrefSerialnumber.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

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
        if issubclass(NestedIDHrefSerialnumber, dict):
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
        if not isinstance(other, NestedIDHrefSerialnumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

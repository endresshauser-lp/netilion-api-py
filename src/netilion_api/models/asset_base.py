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

class AssetBase(object):
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
        'serial_number': 'str',
        'description': 'str',
        'production_date': 'str',
        'last_seen_at': 'str'
    }

    attribute_map = {
        'serial_number': 'serial_number',
        'description': 'description',
        'production_date': 'production_date',
        'last_seen_at': 'last_seen_at'
    }

    discriminator_value_class_map = {
          'AssetHistoryBase': 'AssetHistoryBase',
'AssetRequest': 'AssetRequest',
'AssetResponse': 'AssetResponse'    }

    def __init__(self, serial_number=None, description=None, production_date=None, last_seen_at=None):  # noqa: E501
        """AssetBase - a model defined in Swagger"""  # noqa: E501
        self._serial_number = None
        self._description = None
        self._production_date = None
        self._last_seen_at = None
        self.discriminator = 'assetBaseType'
        self.serial_number = serial_number
        if description is not None:
            self.description = description
        if production_date is not None:
            self.production_date = production_date
        if last_seen_at is not None:
            self.last_seen_at = last_seen_at

    @property
    def serial_number(self):
        """Gets the serial_number of this AssetBase.  # noqa: E501

        at least 4 characters long and unique within the manufacturers scope. Whitespaces are trimmed  # noqa: E501

        :return: The serial_number of this AssetBase.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this AssetBase.

        at least 4 characters long and unique within the manufacturers scope. Whitespaces are trimmed  # noqa: E501

        :param serial_number: The serial_number of this AssetBase.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def description(self):
        """Gets the description of this AssetBase.  # noqa: E501

        description text of the asset  # noqa: E501

        :return: The description of this AssetBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AssetBase.

        description text of the asset  # noqa: E501

        :param description: The description of this AssetBase.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def production_date(self):
        """Gets the production_date of this AssetBase.  # noqa: E501

        Date of production of the asset  # noqa: E501

        :return: The production_date of this AssetBase.  # noqa: E501
        :rtype: str
        """
        return self._production_date

    @production_date.setter
    def production_date(self, production_date):
        """Sets the production_date of this AssetBase.

        Date of production of the asset  # noqa: E501

        :param production_date: The production_date of this AssetBase.  # noqa: E501
        :type: str
        """

        self._production_date = production_date

    @property
    def last_seen_at(self):
        """Gets the last_seen_at of this AssetBase.  # noqa: E501

        last time this asset has been visited/seen/scanned by a person or edge device  # noqa: E501

        :return: The last_seen_at of this AssetBase.  # noqa: E501
        :rtype: str
        """
        return self._last_seen_at

    @last_seen_at.setter
    def last_seen_at(self, last_seen_at):
        """Sets the last_seen_at of this AssetBase.

        last time this asset has been visited/seen/scanned by a person or edge device  # noqa: E501

        :param last_seen_at: The last_seen_at of this AssetBase.  # noqa: E501
        :type: str
        """

        self._last_seen_at = last_seen_at

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
        if issubclass(AssetBase, dict):
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
        if not isinstance(other, AssetBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
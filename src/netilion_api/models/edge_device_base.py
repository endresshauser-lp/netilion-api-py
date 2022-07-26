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

class EdgeDeviceBase(object):
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
        'name': 'str',
        'description': 'str',
        'log_level': 'str',
        'apply_timestamp': 'str'
    }

    attribute_map = {
        'serial_number': 'serial_number',
        'name': 'name',
        'description': 'description',
        'log_level': 'log_level',
        'apply_timestamp': 'apply_timestamp'
    }

    discriminator_value_class_map = {
          'EdgeDeviceResponse': 'EdgeDeviceResponse'    }

    def __init__(self, serial_number=None, name=None, description=None, log_level=None, apply_timestamp=None):  # noqa: E501
        """EdgeDeviceBase - a model defined in Swagger"""  # noqa: E501
        self._serial_number = None
        self._name = None
        self._description = None
        self._log_level = None
        self._apply_timestamp = None
        self.discriminator = 'edgeDeviceBaseType'
        self.serial_number = serial_number
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if log_level is not None:
            self.log_level = log_level
        if apply_timestamp is not None:
            self.apply_timestamp = apply_timestamp

    @property
    def serial_number(self):
        """Gets the serial_number of this EdgeDeviceBase.  # noqa: E501

        serial number of the edge device  # noqa: E501

        :return: The serial_number of this EdgeDeviceBase.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this EdgeDeviceBase.

        serial number of the edge device  # noqa: E501

        :param serial_number: The serial_number of this EdgeDeviceBase.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def name(self):
        """Gets the name of this EdgeDeviceBase.  # noqa: E501

        name of the edge device  # noqa: E501

        :return: The name of this EdgeDeviceBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EdgeDeviceBase.

        name of the edge device  # noqa: E501

        :param name: The name of this EdgeDeviceBase.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this EdgeDeviceBase.  # noqa: E501

        description of the edge device  # noqa: E501

        :return: The description of this EdgeDeviceBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EdgeDeviceBase.

        description of the edge device  # noqa: E501

        :param description: The description of this EdgeDeviceBase.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def log_level(self):
        """Gets the log_level of this EdgeDeviceBase.  # noqa: E501

        log level the edge device should use (allowed values: trace, debug, info, warning, error, critical, off)  # noqa: E501

        :return: The log_level of this EdgeDeviceBase.  # noqa: E501
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this EdgeDeviceBase.

        log level the edge device should use (allowed values: trace, debug, info, warning, error, critical, off)  # noqa: E501

        :param log_level: The log_level of this EdgeDeviceBase.  # noqa: E501
        :type: str
        """

        self._log_level = log_level

    @property
    def apply_timestamp(self):
        """Gets the apply_timestamp of this EdgeDeviceBase.  # noqa: E501

        timestamp when the current settings have been applied at in the edge device. Expected date format is YYYY-MM-DDThh:mm:ss  # noqa: E501

        :return: The apply_timestamp of this EdgeDeviceBase.  # noqa: E501
        :rtype: str
        """
        return self._apply_timestamp

    @apply_timestamp.setter
    def apply_timestamp(self, apply_timestamp):
        """Sets the apply_timestamp of this EdgeDeviceBase.

        timestamp when the current settings have been applied at in the edge device. Expected date format is YYYY-MM-DDThh:mm:ss  # noqa: E501

        :param apply_timestamp: The apply_timestamp of this EdgeDeviceBase.  # noqa: E501
        :type: str
        """

        self._apply_timestamp = apply_timestamp

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
        if issubclass(EdgeDeviceBase, dict):
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
        if not isinstance(other, EdgeDeviceBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

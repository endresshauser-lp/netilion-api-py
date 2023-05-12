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

class ResourceNotificationBase(object):
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
        'enabled': 'bool',
        'event_type': 'str',
        'asset_statuses': 'list[str]',
        'diagnosis_codes': 'list[str]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'event_type': 'event_type',
        'asset_statuses': 'asset_statuses',
        'diagnosis_codes': 'diagnosis_codes'
    }

    discriminator_value_class_map = {
          'ResourceNotificationRequest': 'ResourceNotificationRequest',
'ResourceNotificationResponse': 'ResourceNotificationResponse'    }

    def __init__(self, enabled=None, event_type=None, asset_statuses=None, diagnosis_codes=None):  # noqa: E501
        """ResourceNotificationBase - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._event_type = None
        self._asset_statuses = None
        self._diagnosis_codes = None
        self.discriminator = 'resourceNotificationBaseType'
        if enabled is not None:
            self.enabled = enabled
        self.event_type = event_type
        if asset_statuses is not None:
            self.asset_statuses = asset_statuses
        if diagnosis_codes is not None:
            self.diagnosis_codes = diagnosis_codes

    @property
    def enabled(self):
        """Gets the enabled of this ResourceNotificationBase.  # noqa: E501

        Whether the notification is enabled or not (default true).  # noqa: E501

        :return: The enabled of this ResourceNotificationBase.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ResourceNotificationBase.

        Whether the notification is enabled or not (default true).  # noqa: E501

        :param enabled: The enabled of this ResourceNotificationBase.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def event_type(self):
        """Gets the event_type of this ResourceNotificationBase.  # noqa: E501

        possible values are: 'health_status'  # noqa: E501

        :return: The event_type of this ResourceNotificationBase.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ResourceNotificationBase.

        possible values are: 'health_status'  # noqa: E501

        :param event_type: The event_type of this ResourceNotificationBase.  # noqa: E501
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def asset_statuses(self):
        """Gets the asset_statuses of this ResourceNotificationBase.  # noqa: E501

        An array of asset status code strings. Example: ['out_of_specification']  # noqa: E501

        :return: The asset_statuses of this ResourceNotificationBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._asset_statuses

    @asset_statuses.setter
    def asset_statuses(self, asset_statuses):
        """Sets the asset_statuses of this ResourceNotificationBase.

        An array of asset status code strings. Example: ['out_of_specification']  # noqa: E501

        :param asset_statuses: The asset_statuses of this ResourceNotificationBase.  # noqa: E501
        :type: list[str]
        """

        self._asset_statuses = asset_statuses

    @property
    def diagnosis_codes(self):
        """Gets the diagnosis_codes of this ResourceNotificationBase.  # noqa: E501

        An array of diagnosis code strings. Example: ['F123']  # noqa: E501

        :return: The diagnosis_codes of this ResourceNotificationBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._diagnosis_codes

    @diagnosis_codes.setter
    def diagnosis_codes(self, diagnosis_codes):
        """Sets the diagnosis_codes of this ResourceNotificationBase.

        An array of diagnosis code strings. Example: ['F123']  # noqa: E501

        :param diagnosis_codes: The diagnosis_codes of this ResourceNotificationBase.  # noqa: E501
        :type: list[str]
        """

        self._diagnosis_codes = diagnosis_codes

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
        if issubclass(ResourceNotificationBase, dict):
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
        if not isinstance(other, ResourceNotificationBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

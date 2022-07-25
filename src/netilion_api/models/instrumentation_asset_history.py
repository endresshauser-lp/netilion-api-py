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


class InstrumentationAssetHistory(object):
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
        'asset': 'NestedIDHrefSerialnumber',
        'event': 'str',
        'event_datetime': 'datetime'
    }

    attribute_map = {
        'asset': 'asset',
        'event': 'event',
        'event_datetime': 'event_datetime'
    }

    def __init__(self, asset=None, event=None, event_datetime=None, _configuration=None):  # noqa: E501
        """InstrumentationAssetHistory - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._asset = None
        self._event = None
        self._event_datetime = None
        self.discriminator = None

        self.asset = asset
        self.event = event
        self.event_datetime = event_datetime

    @property
    def asset(self):
        """Gets the asset of this InstrumentationAssetHistory.  # noqa: E501


        :return: The asset of this InstrumentationAssetHistory.  # noqa: E501
        :rtype: NestedIDHrefSerialnumber
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InstrumentationAssetHistory.


        :param asset: The asset of this InstrumentationAssetHistory.  # noqa: E501
        :type: NestedIDHrefSerialnumber
        """
        if self._configuration.client_side_validation and asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def event(self):
        """Gets the event of this InstrumentationAssetHistory.  # noqa: E501

        Event type, can be create or destroy  # noqa: E501

        :return: The event of this InstrumentationAssetHistory.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this InstrumentationAssetHistory.

        Event type, can be create or destroy  # noqa: E501

        :param event: The event of this InstrumentationAssetHistory.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def event_datetime(self):
        """Gets the event_datetime of this InstrumentationAssetHistory.  # noqa: E501

        Date of the Event  # noqa: E501

        :return: The event_datetime of this InstrumentationAssetHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._event_datetime

    @event_datetime.setter
    def event_datetime(self, event_datetime):
        """Sets the event_datetime of this InstrumentationAssetHistory.

        Date of the Event  # noqa: E501

        :param event_datetime: The event_datetime of this InstrumentationAssetHistory.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and event_datetime is None:
            raise ValueError("Invalid value for `event_datetime`, must not be `None`")  # noqa: E501

        self._event_datetime = event_datetime

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
        if issubclass(InstrumentationAssetHistory, dict):
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
        if not isinstance(other, InstrumentationAssetHistory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstrumentationAssetHistory):
            return True

        return self.to_dict() != other.to_dict()

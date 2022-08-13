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

class EdgeDeviceFeaturesResponse(object):
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
        'edge_device_features': 'list[EdgeDeviceFeatureResponse]',
        'pagination': 'Pagination'
    }

    attribute_map = {
        'edge_device_features': 'edge_device_features',
        'pagination': 'pagination'
    }

    def __init__(self, edge_device_features=None, pagination=None):  # noqa: E501
        """EdgeDeviceFeaturesResponse - a model defined in Swagger"""  # noqa: E501
        self._edge_device_features = None
        self._pagination = None
        self.discriminator = None
        self.edge_device_features = edge_device_features
        self.pagination = pagination

    @property
    def edge_device_features(self):
        """Gets the edge_device_features of this EdgeDeviceFeaturesResponse.  # noqa: E501


        :return: The edge_device_features of this EdgeDeviceFeaturesResponse.  # noqa: E501
        :rtype: list[EdgeDeviceFeatureResponse]
        """
        return self._edge_device_features

    @edge_device_features.setter
    def edge_device_features(self, edge_device_features):
        """Sets the edge_device_features of this EdgeDeviceFeaturesResponse.


        :param edge_device_features: The edge_device_features of this EdgeDeviceFeaturesResponse.  # noqa: E501
        :type: list[EdgeDeviceFeatureResponse]
        """
        if edge_device_features is None:
            raise ValueError("Invalid value for `edge_device_features`, must not be `None`")  # noqa: E501

        self._edge_device_features = edge_device_features

    @property
    def pagination(self):
        """Gets the pagination of this EdgeDeviceFeaturesResponse.  # noqa: E501


        :return: The pagination of this EdgeDeviceFeaturesResponse.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EdgeDeviceFeaturesResponse.


        :param pagination: The pagination of this EdgeDeviceFeaturesResponse.  # noqa: E501
        :type: Pagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")  # noqa: E501

        self._pagination = pagination

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
        if issubclass(EdgeDeviceFeaturesResponse, dict):
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
        if not isinstance(other, EdgeDeviceFeaturesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

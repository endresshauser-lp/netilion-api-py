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

class Features(object):
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
        'feature_key': 'str',
        'options': 'list[Ooptions]'
    }

    attribute_map = {
        'feature_key': 'feature_key',
        'options': 'options'
    }

    def __init__(self, feature_key=None, options=None):  # noqa: E501
        """Features - a model defined in Swagger"""  # noqa: E501
        self._feature_key = None
        self._options = None
        self.discriminator = None
        self.feature_key = feature_key
        if options is not None:
            self.options = options

    @property
    def feature_key(self):
        """Gets the feature_key of this Features.  # noqa: E501

        feature_key of product feature  # noqa: E501

        :return: The feature_key of this Features.  # noqa: E501
        :rtype: str
        """
        return self._feature_key

    @feature_key.setter
    def feature_key(self, feature_key):
        """Sets the feature_key of this Features.

        feature_key of product feature  # noqa: E501

        :param feature_key: The feature_key of this Features.  # noqa: E501
        :type: str
        """
        if feature_key is None:
            raise ValueError("Invalid value for `feature_key`, must not be `None`")  # noqa: E501

        self._feature_key = feature_key

    @property
    def options(self):
        """Gets the options of this Features.  # noqa: E501


        :return: The options of this Features.  # noqa: E501
        :rtype: list[Ooptions]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Features.


        :param options: The options of this Features.  # noqa: E501
        :type: list[Ooptions]
        """

        self._options = options

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
        if issubclass(Features, dict):
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
        if not isinstance(other, Features):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
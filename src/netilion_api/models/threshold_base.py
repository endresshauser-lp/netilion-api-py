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

class ThresholdBase(object):
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
        'key': 'str',
        'unit_id': 'int',
        'value': 'float',
        'tolerance': 'float',
        'threshold_type': 'str',
        'notification': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'key': 'key',
        'unit_id': 'unit_id',
        'value': 'value',
        'tolerance': 'tolerance',
        'threshold_type': 'threshold_type',
        'notification': 'notification'
    }

    discriminator_value_class_map = {
          'ThresholdRequest': 'ThresholdRequest'    }

    def __init__(self, name=None, description=None, key=None, unit_id=None, value=None, tolerance=None, threshold_type=None, notification=None):  # noqa: E501
        """ThresholdBase - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._key = None
        self._unit_id = None
        self._value = None
        self._tolerance = None
        self._threshold_type = None
        self._notification = None
        self.discriminator = 'ThresholdBaseType'
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if key is not None:
            self.key = key
        if unit_id is not None:
            self.unit_id = unit_id
        if value is not None:
            self.value = value
        if tolerance is not None:
            self.tolerance = tolerance
        if threshold_type is not None:
            self.threshold_type = threshold_type
        if notification is not None:
            self.notification = notification

    @property
    def name(self):
        """Gets the name of this ThresholdBase.  # noqa: E501

        name of the threshold. The name of the threshold.  # noqa: E501

        :return: The name of this ThresholdBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThresholdBase.

        name of the threshold. The name of the threshold.  # noqa: E501

        :param name: The name of this ThresholdBase.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ThresholdBase.  # noqa: E501

        description of the threshold. The description of the threshold.  # noqa: E501

        :return: The description of this ThresholdBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ThresholdBase.

        description of the threshold. The description of the threshold.  # noqa: E501

        :param description: The description of this ThresholdBase.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def key(self):
        """Gets the key of this ThresholdBase.  # noqa: E501

        key of the threshold. This key is related to the keys set in asset values.  # noqa: E501

        :return: The key of this ThresholdBase.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ThresholdBase.

        key of the threshold. This key is related to the keys set in asset values.  # noqa: E501

        :param key: The key of this ThresholdBase.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def unit_id(self):
        """Gets the unit_id of this ThresholdBase.  # noqa: E501

        Id of the unit used for the threshold value property.  # noqa: E501

        :return: The unit_id of this ThresholdBase.  # noqa: E501
        :rtype: int
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """Sets the unit_id of this ThresholdBase.

        Id of the unit used for the threshold value property.  # noqa: E501

        :param unit_id: The unit_id of this ThresholdBase.  # noqa: E501
        :type: int
        """

        self._unit_id = unit_id

    @property
    def value(self):
        """Gets the value of this ThresholdBase.  # noqa: E501

        the threshold value  # noqa: E501

        :return: The value of this ThresholdBase.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ThresholdBase.

        the threshold value  # noqa: E501

        :param value: The value of this ThresholdBase.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def tolerance(self):
        """Gets the tolerance of this ThresholdBase.  # noqa: E501

        the threshold tolerance, should be a positive value  # noqa: E501

        :return: The tolerance of this ThresholdBase.  # noqa: E501
        :rtype: float
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance):
        """Sets the tolerance of this ThresholdBase.

        the threshold tolerance, should be a positive value  # noqa: E501

        :param tolerance: The tolerance of this ThresholdBase.  # noqa: E501
        :type: float
        """

        self._tolerance = tolerance

    @property
    def threshold_type(self):
        """Gets the threshold_type of this ThresholdBase.  # noqa: E501

        the threshold type, tree values can be given for now, 'low' if the it is a lower threshold, 'high' if it is an upper threshold and 'deviation' if it is as deviation from reference values  # noqa: E501

        :return: The threshold_type of this ThresholdBase.  # noqa: E501
        :rtype: str
        """
        return self._threshold_type

    @threshold_type.setter
    def threshold_type(self, threshold_type):
        """Sets the threshold_type of this ThresholdBase.

        the threshold type, tree values can be given for now, 'low' if the it is a lower threshold, 'high' if it is an upper threshold and 'deviation' if it is as deviation from reference values  # noqa: E501

        :param threshold_type: The threshold_type of this ThresholdBase.  # noqa: E501
        :type: str
        """

        self._threshold_type = threshold_type

    @property
    def notification(self):
        """Gets the notification of this ThresholdBase.  # noqa: E501

        Whether the threshold should send notifications when exceeded  # noqa: E501

        :return: The notification of this ThresholdBase.  # noqa: E501
        :rtype: bool
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this ThresholdBase.

        Whether the threshold should send notifications when exceeded  # noqa: E501

        :param notification: The notification of this ThresholdBase.  # noqa: E501
        :type: bool
        """

        self._notification = notification

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
        if issubclass(ThresholdBase, dict):
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
        if not isinstance(other, ThresholdBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
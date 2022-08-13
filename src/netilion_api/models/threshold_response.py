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

class ThresholdResponse(object):
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
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'key': 'key',
        'unit_id': 'unit_id',
        'value': 'value',
        'tolerance': 'tolerance',
        'threshold_type': 'threshold_type',
        'notification': 'notification'
    }

    def __init__(self, id=None, name=None, description=None, key=None, unit_id=None, value=None, tolerance=None, threshold_type=None, notification=None):  # noqa: E501
        """ThresholdResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._key = None
        self._unit_id = None
        self._value = None
        self._tolerance = None
        self._threshold_type = None
        self._notification = None
        self.discriminator = None
        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.key = key
        if unit_id is not None:
            self.unit_id = unit_id
        self.value = value
        self.tolerance = tolerance
        self.threshold_type = threshold_type
        self.notification = notification

    @property
    def id(self):
        """Gets the id of this ThresholdResponse.  # noqa: E501

        Id of object  # noqa: E501

        :return: The id of this ThresholdResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThresholdResponse.

        Id of object  # noqa: E501

        :param id: The id of this ThresholdResponse.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ThresholdResponse.  # noqa: E501

        name of the threshold. The name of the threshold.  # noqa: E501

        :return: The name of this ThresholdResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThresholdResponse.

        name of the threshold. The name of the threshold.  # noqa: E501

        :param name: The name of this ThresholdResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ThresholdResponse.  # noqa: E501

        description of the threshold. The description of the threshold.  # noqa: E501

        :return: The description of this ThresholdResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ThresholdResponse.

        description of the threshold. The description of the threshold.  # noqa: E501

        :param description: The description of this ThresholdResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def key(self):
        """Gets the key of this ThresholdResponse.  # noqa: E501

        key of the threshold. This key is related to the keys set in asset values.  # noqa: E501

        :return: The key of this ThresholdResponse.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ThresholdResponse.

        key of the threshold. This key is related to the keys set in asset values.  # noqa: E501

        :param key: The key of this ThresholdResponse.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def unit_id(self):
        """Gets the unit_id of this ThresholdResponse.  # noqa: E501

        Id of the unit used for the threshold value property.  # noqa: E501

        :return: The unit_id of this ThresholdResponse.  # noqa: E501
        :rtype: int
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """Sets the unit_id of this ThresholdResponse.

        Id of the unit used for the threshold value property.  # noqa: E501

        :param unit_id: The unit_id of this ThresholdResponse.  # noqa: E501
        :type: int
        """

        self._unit_id = unit_id

    @property
    def value(self):
        """Gets the value of this ThresholdResponse.  # noqa: E501

        the threshold value  # noqa: E501

        :return: The value of this ThresholdResponse.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ThresholdResponse.

        the threshold value  # noqa: E501

        :param value: The value of this ThresholdResponse.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def tolerance(self):
        """Gets the tolerance of this ThresholdResponse.  # noqa: E501

        the threshold tolerance, should be a positive value  # noqa: E501

        :return: The tolerance of this ThresholdResponse.  # noqa: E501
        :rtype: float
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance):
        """Sets the tolerance of this ThresholdResponse.

        the threshold tolerance, should be a positive value  # noqa: E501

        :param tolerance: The tolerance of this ThresholdResponse.  # noqa: E501
        :type: float
        """
        if tolerance is None:
            raise ValueError("Invalid value for `tolerance`, must not be `None`")  # noqa: E501

        self._tolerance = tolerance

    @property
    def threshold_type(self):
        """Gets the threshold_type of this ThresholdResponse.  # noqa: E501

        the threshold type, tree values can be given for now, 'low' if the it is a lower threshold, 'high' if it is an upper threshold and 'deviation' if it is as deviation from reference values  # noqa: E501

        :return: The threshold_type of this ThresholdResponse.  # noqa: E501
        :rtype: str
        """
        return self._threshold_type

    @threshold_type.setter
    def threshold_type(self, threshold_type):
        """Sets the threshold_type of this ThresholdResponse.

        the threshold type, tree values can be given for now, 'low' if the it is a lower threshold, 'high' if it is an upper threshold and 'deviation' if it is as deviation from reference values  # noqa: E501

        :param threshold_type: The threshold_type of this ThresholdResponse.  # noqa: E501
        :type: str
        """
        if threshold_type is None:
            raise ValueError("Invalid value for `threshold_type`, must not be `None`")  # noqa: E501

        self._threshold_type = threshold_type

    @property
    def notification(self):
        """Gets the notification of this ThresholdResponse.  # noqa: E501

        Whether the threshold should send notifications when exceeded  # noqa: E501

        :return: The notification of this ThresholdResponse.  # noqa: E501
        :rtype: bool
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this ThresholdResponse.

        Whether the threshold should send notifications when exceeded  # noqa: E501

        :param notification: The notification of this ThresholdResponse.  # noqa: E501
        :type: bool
        """
        if notification is None:
            raise ValueError("Invalid value for `notification`, must not be `None`")  # noqa: E501

        self._notification = notification

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
        if issubclass(ThresholdResponse, dict):
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
        if not isinstance(other, ThresholdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

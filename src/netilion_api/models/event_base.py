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

class EventBase(object):
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
        'responsible': 'str',
        'start_datetime': 'str',
        'end_datetime': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'responsible': 'responsible',
        'start_datetime': 'start_datetime',
        'end_datetime': 'end_datetime'
    }

    discriminator_value_class_map = {
          'EventRequestNoAssets': 'EventRequestNoAssets',
'EventResponse': 'EventResponse',
'EventRequestNoInstrumentations': 'EventRequestNoInstrumentations',
'EventRequest': 'EventRequest'    }

    def __init__(self, name=None, description=None, responsible=None, start_datetime=None, end_datetime=None):  # noqa: E501
        """EventBase - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._responsible = None
        self._start_datetime = None
        self._end_datetime = None
        self.discriminator = 'eventBaseType'
        self.name = name
        if description is not None:
            self.description = description
        if responsible is not None:
            self.responsible = responsible
        if start_datetime is not None:
            self.start_datetime = start_datetime
        if end_datetime is not None:
            self.end_datetime = end_datetime

    @property
    def name(self):
        """Gets the name of this EventBase.  # noqa: E501

        Name of the event  # noqa: E501

        :return: The name of this EventBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventBase.

        Name of the event  # noqa: E501

        :param name: The name of this EventBase.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this EventBase.  # noqa: E501

        description text of the event  # noqa: E501

        :return: The description of this EventBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventBase.

        description text of the event  # noqa: E501

        :param description: The description of this EventBase.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def responsible(self):
        """Gets the responsible of this EventBase.  # noqa: E501

        responsible of the event  # noqa: E501

        :return: The responsible of this EventBase.  # noqa: E501
        :rtype: str
        """
        return self._responsible

    @responsible.setter
    def responsible(self, responsible):
        """Sets the responsible of this EventBase.

        responsible of the event  # noqa: E501

        :param responsible: The responsible of this EventBase.  # noqa: E501
        :type: str
        """

        self._responsible = responsible

    @property
    def start_datetime(self):
        """Gets the start_datetime of this EventBase.  # noqa: E501

        start date/time of the event: format example: 2016-01-01T18:30:00  # noqa: E501

        :return: The start_datetime of this EventBase.  # noqa: E501
        :rtype: str
        """
        return self._start_datetime

    @start_datetime.setter
    def start_datetime(self, start_datetime):
        """Sets the start_datetime of this EventBase.

        start date/time of the event: format example: 2016-01-01T18:30:00  # noqa: E501

        :param start_datetime: The start_datetime of this EventBase.  # noqa: E501
        :type: str
        """

        self._start_datetime = start_datetime

    @property
    def end_datetime(self):
        """Gets the end_datetime of this EventBase.  # noqa: E501

        end date/time of the event: format example: 2016-01-01T18:30:00  # noqa: E501

        :return: The end_datetime of this EventBase.  # noqa: E501
        :rtype: str
        """
        return self._end_datetime

    @end_datetime.setter
    def end_datetime(self, end_datetime):
        """Sets the end_datetime of this EventBase.

        end date/time of the event: format example: 2016-01-01T18:30:00  # noqa: E501

        :param end_datetime: The end_datetime of this EventBase.  # noqa: E501
        :type: str
        """

        self._end_datetime = end_datetime

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
        if issubclass(EventBase, dict):
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
        if not isinstance(other, EventBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

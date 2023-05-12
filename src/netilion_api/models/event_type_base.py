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

class EventTypeBase(object):
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
        'code': 'str',
        'name': 'str',
        'description': 'str',
        'deletable': 'bool'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'deletable': 'deletable'
    }

    discriminator_value_class_map = {
          'EventTypeResponse': 'EventTypeResponse',
'EventTypeRequest': 'EventTypeRequest'    }

    def __init__(self, code=None, name=None, description=None, deletable=None):  # noqa: E501
        """EventTypeBase - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._name = None
        self._description = None
        self._deletable = None
        self.discriminator = 'eventTypeBaseType'
        if code is not None:
            self.code = code
        self.name = name
        if description is not None:
            self.description = description
        if deletable is not None:
            self.deletable = deletable

    @property
    def code(self):
        """Gets the code of this EventTypeBase.  # noqa: E501

        The value must be unique. Whitespaces are trimmed.  # noqa: E501

        :return: The code of this EventTypeBase.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EventTypeBase.

        The value must be unique. Whitespaces are trimmed.  # noqa: E501

        :param code: The code of this EventTypeBase.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this EventTypeBase.  # noqa: E501

        Supports translations. Whitespaces are trimmed.  # noqa: E501

        :return: The name of this EventTypeBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventTypeBase.

        Supports translations. Whitespaces are trimmed.  # noqa: E501

        :param name: The name of this EventTypeBase.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this EventTypeBase.  # noqa: E501

        Supports translations.  # noqa: E501

        :return: The description of this EventTypeBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventTypeBase.

        Supports translations.  # noqa: E501

        :param description: The description of this EventTypeBase.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def deletable(self):
        """Gets the deletable of this EventTypeBase.  # noqa: E501

        Events with deletable types can be deleted.  # noqa: E501

        :return: The deletable of this EventTypeBase.  # noqa: E501
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        """Sets the deletable of this EventTypeBase.

        Events with deletable types can be deleted.  # noqa: E501

        :param deletable: The deletable of this EventTypeBase.  # noqa: E501
        :type: bool
        """

        self._deletable = deletable

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
        if issubclass(EventTypeBase, dict):
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
        if not isinstance(other, EventTypeBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

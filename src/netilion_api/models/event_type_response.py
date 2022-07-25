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


class EventTypeResponse(object):
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
        'tenant': 'NestedIDHref'
    }

    attribute_map = {
        'id': 'id',
        'tenant': 'tenant'
    }

    def __init__(self, id=None, tenant=None, _configuration=None):  # noqa: E501
        """EventTypeResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._tenant = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant is not None:
            self.tenant = tenant

    @property
    def id(self):
        """Gets the id of this EventTypeResponse.  # noqa: E501

        Id of object  # noqa: E501

        :return: The id of this EventTypeResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventTypeResponse.

        Id of object  # noqa: E501

        :param id: The id of this EventTypeResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def tenant(self):
        """Gets the tenant of this EventTypeResponse.  # noqa: E501


        :return: The tenant of this EventTypeResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this EventTypeResponse.


        :param tenant: The tenant of this EventTypeResponse.  # noqa: E501
        :type: NestedIDHref
        """

        self._tenant = tenant

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
        if issubclass(EventTypeResponse, dict):
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
        if not isinstance(other, EventTypeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventTypeResponse):
            return True

        return self.to_dict() != other.to_dict()

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

class NodeTypes(object):
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
        'node_types': 'list[NodeTypeResponse]',
        'pagination': 'Pagination'
    }

    attribute_map = {
        'node_types': 'node_types',
        'pagination': 'pagination'
    }

    def __init__(self, node_types=None, pagination=None):  # noqa: E501
        """NodeTypes - a model defined in Swagger"""  # noqa: E501
        self._node_types = None
        self._pagination = None
        self.discriminator = None
        if node_types is not None:
            self.node_types = node_types
        if pagination is not None:
            self.pagination = pagination

    @property
    def node_types(self):
        """Gets the node_types of this NodeTypes.  # noqa: E501


        :return: The node_types of this NodeTypes.  # noqa: E501
        :rtype: list[NodeTypeResponse]
        """
        return self._node_types

    @node_types.setter
    def node_types(self, node_types):
        """Sets the node_types of this NodeTypes.


        :param node_types: The node_types of this NodeTypes.  # noqa: E501
        :type: list[NodeTypeResponse]
        """

        self._node_types = node_types

    @property
    def pagination(self):
        """Gets the pagination of this NodeTypes.  # noqa: E501


        :return: The pagination of this NodeTypes.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this NodeTypes.


        :param pagination: The pagination of this NodeTypes.  # noqa: E501
        :type: Pagination
        """

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
        if issubclass(NodeTypes, dict):
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
        if not isinstance(other, NodeTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

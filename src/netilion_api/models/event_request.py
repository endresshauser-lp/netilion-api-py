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
from netilion_api.models.event_base import EventBase  # noqa: F401,E501

class EventRequest(EventBase):
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
        'status': 'NestedID',
        'type': 'NestedID',
        'tenant': 'NestedID',
        'assets': 'list[NestedID]',
        'instrumentations': 'list[NestedID]',
        'nodes': 'list[NestedID]'
    }
    if hasattr(EventBase, "swagger_types"):
        swagger_types.update(EventBase.swagger_types)

    attribute_map = {
        'status': 'status',
        'type': 'type',
        'tenant': 'tenant',
        'assets': 'assets',
        'instrumentations': 'instrumentations',
        'nodes': 'nodes'
    }
    if hasattr(EventBase, "attribute_map"):
        attribute_map.update(EventBase.attribute_map)

    def __init__(self, status=None, type=None, tenant=None, assets=None, instrumentations=None, nodes=None, *args, **kwargs):  # noqa: E501
        """EventRequest - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._type = None
        self._tenant = None
        self._assets = None
        self._instrumentations = None
        self._nodes = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if tenant is not None:
            self.tenant = tenant
        if assets is not None:
            self.assets = assets
        if instrumentations is not None:
            self.instrumentations = instrumentations
        if nodes is not None:
            self.nodes = nodes
        EventBase.__init__(self, *args, **kwargs)

    @property
    def status(self):
        """Gets the status of this EventRequest.  # noqa: E501


        :return: The status of this EventRequest.  # noqa: E501
        :rtype: NestedID
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EventRequest.


        :param status: The status of this EventRequest.  # noqa: E501
        :type: NestedID
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this EventRequest.  # noqa: E501


        :return: The type of this EventRequest.  # noqa: E501
        :rtype: NestedID
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EventRequest.


        :param type: The type of this EventRequest.  # noqa: E501
        :type: NestedID
        """

        self._type = type

    @property
    def tenant(self):
        """Gets the tenant of this EventRequest.  # noqa: E501


        :return: The tenant of this EventRequest.  # noqa: E501
        :rtype: NestedID
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this EventRequest.


        :param tenant: The tenant of this EventRequest.  # noqa: E501
        :type: NestedID
        """

        self._tenant = tenant

    @property
    def assets(self):
        """Gets the assets of this EventRequest.  # noqa: E501


        :return: The assets of this EventRequest.  # noqa: E501
        :rtype: list[NestedID]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this EventRequest.


        :param assets: The assets of this EventRequest.  # noqa: E501
        :type: list[NestedID]
        """

        self._assets = assets

    @property
    def instrumentations(self):
        """Gets the instrumentations of this EventRequest.  # noqa: E501


        :return: The instrumentations of this EventRequest.  # noqa: E501
        :rtype: list[NestedID]
        """
        return self._instrumentations

    @instrumentations.setter
    def instrumentations(self, instrumentations):
        """Sets the instrumentations of this EventRequest.


        :param instrumentations: The instrumentations of this EventRequest.  # noqa: E501
        :type: list[NestedID]
        """

        self._instrumentations = instrumentations

    @property
    def nodes(self):
        """Gets the nodes of this EventRequest.  # noqa: E501


        :return: The nodes of this EventRequest.  # noqa: E501
        :rtype: list[NestedID]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this EventRequest.


        :param nodes: The nodes of this EventRequest.  # noqa: E501
        :type: list[NestedID]
        """

        self._nodes = nodes

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
        if issubclass(EventRequest, dict):
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
        if not isinstance(other, EventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

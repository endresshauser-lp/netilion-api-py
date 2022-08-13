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
from netilion_api.models.instrumentation_type_base import InstrumentationTypeBase  # noqa: F401,E501

class InstrumentationTypeResponse(InstrumentationTypeBase):
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
        'tenant': 'NestedIDHref',
        'parent': 'NestedIDHref'
    }
    if hasattr(InstrumentationTypeBase, "swagger_types"):
        swagger_types.update(InstrumentationTypeBase.swagger_types)

    attribute_map = {
        'id': 'id',
        'tenant': 'tenant',
        'parent': 'parent'
    }
    if hasattr(InstrumentationTypeBase, "attribute_map"):
        attribute_map.update(InstrumentationTypeBase.attribute_map)

    def __init__(self, id=None, tenant=None, parent=None, *args, **kwargs):  # noqa: E501
        """InstrumentationTypeResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._tenant = None
        self._parent = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if tenant is not None:
            self.tenant = tenant
        if parent is not None:
            self.parent = parent
        InstrumentationTypeBase.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this InstrumentationTypeResponse.  # noqa: E501

        Id of object  # noqa: E501

        :return: The id of this InstrumentationTypeResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstrumentationTypeResponse.

        Id of object  # noqa: E501

        :param id: The id of this InstrumentationTypeResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def tenant(self):
        """Gets the tenant of this InstrumentationTypeResponse.  # noqa: E501


        :return: The tenant of this InstrumentationTypeResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this InstrumentationTypeResponse.


        :param tenant: The tenant of this InstrumentationTypeResponse.  # noqa: E501
        :type: NestedIDHref
        """

        self._tenant = tenant

    @property
    def parent(self):
        """Gets the parent of this InstrumentationTypeResponse.  # noqa: E501


        :return: The parent of this InstrumentationTypeResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this InstrumentationTypeResponse.


        :param parent: The parent of this InstrumentationTypeResponse.  # noqa: E501
        :type: NestedIDHref
        """

        self._parent = parent

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
        if issubclass(InstrumentationTypeResponse, dict):
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
        if not isinstance(other, InstrumentationTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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
from netilion_api.models.user_base import UserBase  # noqa: F401,E501

class CurrentUserResponse(UserBase):
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
        'disabled': 'bool',
        'address': 'UserAddressResponse',
        'links': 'CurrentUserResponseLinks'
    }
    if hasattr(UserBase, "swagger_types"):
        swagger_types.update(UserBase.swagger_types)

    attribute_map = {
        'id': 'id',
        'disabled': 'disabled',
        'address': 'address',
        'links': 'links'
    }
    if hasattr(UserBase, "attribute_map"):
        attribute_map.update(UserBase.attribute_map)

    def __init__(self, id=None, disabled=None, address=None, links=None, *args, **kwargs):  # noqa: E501
        """CurrentUserResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._disabled = None
        self._address = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if disabled is not None:
            self.disabled = disabled
        if address is not None:
            self.address = address
        if links is not None:
            self.links = links
        UserBase.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this CurrentUserResponse.  # noqa: E501

        Id of object  # noqa: E501

        :return: The id of this CurrentUserResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CurrentUserResponse.

        Id of object  # noqa: E501

        :param id: The id of this CurrentUserResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def disabled(self):
        """Gets the disabled of this CurrentUserResponse.  # noqa: E501


        :return: The disabled of this CurrentUserResponse.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this CurrentUserResponse.


        :param disabled: The disabled of this CurrentUserResponse.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def address(self):
        """Gets the address of this CurrentUserResponse.  # noqa: E501


        :return: The address of this CurrentUserResponse.  # noqa: E501
        :rtype: UserAddressResponse
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CurrentUserResponse.


        :param address: The address of this CurrentUserResponse.  # noqa: E501
        :type: UserAddressResponse
        """

        self._address = address

    @property
    def links(self):
        """Gets the links of this CurrentUserResponse.  # noqa: E501


        :return: The links of this CurrentUserResponse.  # noqa: E501
        :rtype: CurrentUserResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CurrentUserResponse.


        :param links: The links of this CurrentUserResponse.  # noqa: E501
        :type: CurrentUserResponseLinks
        """

        self._links = links

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
        if issubclass(CurrentUserResponse, dict):
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
        if not isinstance(other, CurrentUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
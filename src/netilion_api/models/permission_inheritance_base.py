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

class PermissionInheritanceBase(object):
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
        'permission_type': 'str',
        'inheritance': 'bool',
        'permission_inheritable': 'PermissionInheritable'
    }

    attribute_map = {
        'permission_type': 'permission_type',
        'inheritance': 'inheritance',
        'permission_inheritable': 'permission_inheritable'
    }

    discriminator_value_class_map = {
          'PermissionInheritanceResponse': 'PermissionInheritanceResponse',
'PermissionInheritanceRequest': 'PermissionInheritanceRequest'    }

    def __init__(self, permission_type=None, inheritance=None, permission_inheritable=None):  # noqa: E501
        """PermissionInheritanceBase - a model defined in Swagger"""  # noqa: E501
        self._permission_type = None
        self._inheritance = None
        self._permission_inheritable = None
        self.discriminator = 'permissionInheritanceBaseType'
        if permission_type is not None:
            self.permission_type = permission_type
        if inheritance is not None:
            self.inheritance = inheritance
        if permission_inheritable is not None:
            self.permission_inheritable = permission_inheritable

    @property
    def permission_type(self):
        """Gets the permission_type of this PermissionInheritanceBase.  # noqa: E501

        possible values are: 'can_read', 'can_update', 'can_delete' and 'can_permit'  # noqa: E501

        :return: The permission_type of this PermissionInheritanceBase.  # noqa: E501
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        """Sets the permission_type of this PermissionInheritanceBase.

        possible values are: 'can_read', 'can_update', 'can_delete' and 'can_permit'  # noqa: E501

        :param permission_type: The permission_type of this PermissionInheritanceBase.  # noqa: E501
        :type: str
        """

        self._permission_type = permission_type

    @property
    def inheritance(self):
        """Gets the inheritance of this PermissionInheritanceBase.  # noqa: E501

        define if permission should be inheritated or not  # noqa: E501

        :return: The inheritance of this PermissionInheritanceBase.  # noqa: E501
        :rtype: bool
        """
        return self._inheritance

    @inheritance.setter
    def inheritance(self, inheritance):
        """Sets the inheritance of this PermissionInheritanceBase.

        define if permission should be inheritated or not  # noqa: E501

        :param inheritance: The inheritance of this PermissionInheritanceBase.  # noqa: E501
        :type: bool
        """

        self._inheritance = inheritance

    @property
    def permission_inheritable(self):
        """Gets the permission_inheritable of this PermissionInheritanceBase.  # noqa: E501


        :return: The permission_inheritable of this PermissionInheritanceBase.  # noqa: E501
        :rtype: PermissionInheritable
        """
        return self._permission_inheritable

    @permission_inheritable.setter
    def permission_inheritable(self, permission_inheritable):
        """Sets the permission_inheritable of this PermissionInheritanceBase.


        :param permission_inheritable: The permission_inheritable of this PermissionInheritanceBase.  # noqa: E501
        :type: PermissionInheritable
        """

        self._permission_inheritable = permission_inheritable

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
        if issubclass(PermissionInheritanceBase, dict):
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
        if not isinstance(other, PermissionInheritanceBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

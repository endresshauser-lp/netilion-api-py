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
from netilion_api.models.asset_base import AssetBase  # noqa: F401,E501

class AssetHistoryBase(AssetBase):
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
        'product': 'NestedIDHref',
        'parent': 'NestedIDHref',
        'status': 'NestedIDHref',
        'tenant': 'NestedIDHref'
    }
    if hasattr(AssetBase, "swagger_types"):
        swagger_types.update(AssetBase.swagger_types)

    attribute_map = {
        'id': 'id',
        'product': 'product',
        'parent': 'parent',
        'status': 'status',
        'tenant': 'tenant'
    }
    if hasattr(AssetBase, "attribute_map"):
        attribute_map.update(AssetBase.attribute_map)

    def __init__(self, id=None, product=None, parent=None, status=None, tenant=None, *args, **kwargs):  # noqa: E501
        """AssetHistoryBase - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._product = None
        self._parent = None
        self._status = None
        self._tenant = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if product is not None:
            self.product = product
        if parent is not None:
            self.parent = parent
        if status is not None:
            self.status = status
        if tenant is not None:
            self.tenant = tenant
        AssetBase.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this AssetHistoryBase.  # noqa: E501

        Id of object  # noqa: E501

        :return: The id of this AssetHistoryBase.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetHistoryBase.

        Id of object  # noqa: E501

        :param id: The id of this AssetHistoryBase.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def product(self):
        """Gets the product of this AssetHistoryBase.  # noqa: E501


        :return: The product of this AssetHistoryBase.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this AssetHistoryBase.


        :param product: The product of this AssetHistoryBase.  # noqa: E501
        :type: NestedIDHref
        """

        self._product = product

    @property
    def parent(self):
        """Gets the parent of this AssetHistoryBase.  # noqa: E501


        :return: The parent of this AssetHistoryBase.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this AssetHistoryBase.


        :param parent: The parent of this AssetHistoryBase.  # noqa: E501
        :type: NestedIDHref
        """

        self._parent = parent

    @property
    def status(self):
        """Gets the status of this AssetHistoryBase.  # noqa: E501


        :return: The status of this AssetHistoryBase.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AssetHistoryBase.


        :param status: The status of this AssetHistoryBase.  # noqa: E501
        :type: NestedIDHref
        """

        self._status = status

    @property
    def tenant(self):
        """Gets the tenant of this AssetHistoryBase.  # noqa: E501


        :return: The tenant of this AssetHistoryBase.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this AssetHistoryBase.


        :param tenant: The tenant of this AssetHistoryBase.  # noqa: E501
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
        if issubclass(AssetHistoryBase, dict):
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
        if not isinstance(other, AssetHistoryBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
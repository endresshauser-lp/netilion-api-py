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
from netilion_api.models.product_identifier_base import ProductIdentifierBase  # noqa: F401,E501

class ProductIdentifierRequest(ProductIdentifierBase):
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
        'tenant': 'NestedID',
        'products': 'list[NestedID]'
    }
    if hasattr(ProductIdentifierBase, "swagger_types"):
        swagger_types.update(ProductIdentifierBase.swagger_types)

    attribute_map = {
        'tenant': 'tenant',
        'products': 'products'
    }
    if hasattr(ProductIdentifierBase, "attribute_map"):
        attribute_map.update(ProductIdentifierBase.attribute_map)

    def __init__(self, tenant=None, products=None, *args, **kwargs):  # noqa: E501
        """ProductIdentifierRequest - a model defined in Swagger"""  # noqa: E501
        self._tenant = None
        self._products = None
        self.discriminator = None
        if tenant is not None:
            self.tenant = tenant
        if products is not None:
            self.products = products
        ProductIdentifierBase.__init__(self, *args, **kwargs)

    @property
    def tenant(self):
        """Gets the tenant of this ProductIdentifierRequest.  # noqa: E501


        :return: The tenant of this ProductIdentifierRequest.  # noqa: E501
        :rtype: NestedID
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this ProductIdentifierRequest.


        :param tenant: The tenant of this ProductIdentifierRequest.  # noqa: E501
        :type: NestedID
        """

        self._tenant = tenant

    @property
    def products(self):
        """Gets the products of this ProductIdentifierRequest.  # noqa: E501


        :return: The products of this ProductIdentifierRequest.  # noqa: E501
        :rtype: list[NestedID]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this ProductIdentifierRequest.


        :param products: The products of this ProductIdentifierRequest.  # noqa: E501
        :type: list[NestedID]
        """

        self._products = products

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
        if issubclass(ProductIdentifierRequest, dict):
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
        if not isinstance(other, ProductIdentifierRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
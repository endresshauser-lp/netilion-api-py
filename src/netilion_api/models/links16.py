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

class Links16(object):
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
        'products': 'Link',
        'deliveries': 'Link',
        'documents': 'Link'
    }

    attribute_map = {
        'products': 'products',
        'deliveries': 'deliveries',
        'documents': 'documents'
    }

    def __init__(self, products=None, deliveries=None, documents=None):  # noqa: E501
        """Links16 - a model defined in Swagger"""  # noqa: E501
        self._products = None
        self._deliveries = None
        self._documents = None
        self.discriminator = None
        if products is not None:
            self.products = products
        if deliveries is not None:
            self.deliveries = deliveries
        if documents is not None:
            self.documents = documents

    @property
    def products(self):
        """Gets the products of this Links16.  # noqa: E501


        :return: The products of this Links16.  # noqa: E501
        :rtype: Link
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this Links16.


        :param products: The products of this Links16.  # noqa: E501
        :type: Link
        """

        self._products = products

    @property
    def deliveries(self):
        """Gets the deliveries of this Links16.  # noqa: E501


        :return: The deliveries of this Links16.  # noqa: E501
        :rtype: Link
        """
        return self._deliveries

    @deliveries.setter
    def deliveries(self, deliveries):
        """Sets the deliveries of this Links16.


        :param deliveries: The deliveries of this Links16.  # noqa: E501
        :type: Link
        """

        self._deliveries = deliveries

    @property
    def documents(self):
        """Gets the documents of this Links16.  # noqa: E501


        :return: The documents of this Links16.  # noqa: E501
        :rtype: Link
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this Links16.


        :param documents: The documents of this Links16.  # noqa: E501
        :type: Link
        """

        self._documents = documents

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
        if issubclass(Links16, dict):
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
        if not isinstance(other, Links16):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

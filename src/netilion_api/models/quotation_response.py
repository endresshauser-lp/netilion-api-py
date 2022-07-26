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
from netilion_api.models.quotation_base import QuotationBase  # noqa: F401,E501

class QuotationResponse(QuotationBase):
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
        'status': 'NestedIDHref',
        'sender': 'NestedIDHref',
        'receiver': 'NestedIDHref',
        'line_items': 'list[ProductLineItem]',
        'links': 'Links17'
    }
    if hasattr(QuotationBase, "swagger_types"):
        swagger_types.update(QuotationBase.swagger_types)

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'sender': 'sender',
        'receiver': 'receiver',
        'line_items': 'line_items',
        'links': 'links'
    }
    if hasattr(QuotationBase, "attribute_map"):
        attribute_map.update(QuotationBase.attribute_map)

    def __init__(self, id=None, status=None, sender=None, receiver=None, line_items=None, links=None, *args, **kwargs):  # noqa: E501
        """QuotationResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._sender = None
        self._receiver = None
        self._line_items = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if sender is not None:
            self.sender = sender
        if receiver is not None:
            self.receiver = receiver
        if line_items is not None:
            self.line_items = line_items
        if links is not None:
            self.links = links
        QuotationBase.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this QuotationResponse.  # noqa: E501

        Id of object  # noqa: E501

        :return: The id of this QuotationResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuotationResponse.

        Id of object  # noqa: E501

        :param id: The id of this QuotationResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this QuotationResponse.  # noqa: E501


        :return: The status of this QuotationResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QuotationResponse.


        :param status: The status of this QuotationResponse.  # noqa: E501
        :type: NestedIDHref
        """

        self._status = status

    @property
    def sender(self):
        """Gets the sender of this QuotationResponse.  # noqa: E501


        :return: The sender of this QuotationResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this QuotationResponse.


        :param sender: The sender of this QuotationResponse.  # noqa: E501
        :type: NestedIDHref
        """

        self._sender = sender

    @property
    def receiver(self):
        """Gets the receiver of this QuotationResponse.  # noqa: E501


        :return: The receiver of this QuotationResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this QuotationResponse.


        :param receiver: The receiver of this QuotationResponse.  # noqa: E501
        :type: NestedIDHref
        """

        self._receiver = receiver

    @property
    def line_items(self):
        """Gets the line_items of this QuotationResponse.  # noqa: E501


        :return: The line_items of this QuotationResponse.  # noqa: E501
        :rtype: list[ProductLineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this QuotationResponse.


        :param line_items: The line_items of this QuotationResponse.  # noqa: E501
        :type: list[ProductLineItem]
        """

        self._line_items = line_items

    @property
    def links(self):
        """Gets the links of this QuotationResponse.  # noqa: E501


        :return: The links of this QuotationResponse.  # noqa: E501
        :rtype: Links17
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this QuotationResponse.


        :param links: The links of this QuotationResponse.  # noqa: E501
        :type: Links17
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
        if issubclass(QuotationResponse, dict):
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
        if not isinstance(other, QuotationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

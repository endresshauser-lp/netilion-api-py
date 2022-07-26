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

class RequestForQuotationBase(object):
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
        'number': 'str',
        'name': 'str',
        '_date': 'str',
        'author': 'str',
        'description': 'str',
        'status': 'NestedID',
        'sender': 'NestedID',
        'receiver': 'NestedID'
    }

    attribute_map = {
        'number': 'number',
        'name': 'name',
        '_date': 'date',
        'author': 'author',
        'description': 'description',
        'status': 'status',
        'sender': 'sender',
        'receiver': 'receiver'
    }

    discriminator_value_class_map = {
          'RequestForQuotationResponse': 'RequestForQuotationResponse',
'RequestForQuotationRequest': 'RequestForQuotationRequest'    }

    def __init__(self, number=None, name=None, _date=None, author=None, description=None, status=None, sender=None, receiver=None):  # noqa: E501
        """RequestForQuotationBase - a model defined in Swagger"""  # noqa: E501
        self._number = None
        self._name = None
        self.__date = None
        self._author = None
        self._description = None
        self._status = None
        self._sender = None
        self._receiver = None
        self.discriminator = 'requestForQuotationBaseType'
        if number is not None:
            self.number = number
        if name is not None:
            self.name = name
        if _date is not None:
            self._date = _date
        if author is not None:
            self.author = author
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if sender is not None:
            self.sender = sender
        if receiver is not None:
            self.receiver = receiver

    @property
    def number(self):
        """Gets the number of this RequestForQuotationBase.  # noqa: E501


        :return: The number of this RequestForQuotationBase.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this RequestForQuotationBase.


        :param number: The number of this RequestForQuotationBase.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def name(self):
        """Gets the name of this RequestForQuotationBase.  # noqa: E501


        :return: The name of this RequestForQuotationBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RequestForQuotationBase.


        :param name: The name of this RequestForQuotationBase.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def _date(self):
        """Gets the _date of this RequestForQuotationBase.  # noqa: E501

        Date must be in format '2016-01-01'  # noqa: E501

        :return: The _date of this RequestForQuotationBase.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this RequestForQuotationBase.

        Date must be in format '2016-01-01'  # noqa: E501

        :param _date: The _date of this RequestForQuotationBase.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def author(self):
        """Gets the author of this RequestForQuotationBase.  # noqa: E501

        Author Author who created the request for quotation  # noqa: E501

        :return: The author of this RequestForQuotationBase.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this RequestForQuotationBase.

        Author Author who created the request for quotation  # noqa: E501

        :param author: The author of this RequestForQuotationBase.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def description(self):
        """Gets the description of this RequestForQuotationBase.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this RequestForQuotationBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RequestForQuotationBase.

        Description  # noqa: E501

        :param description: The description of this RequestForQuotationBase.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this RequestForQuotationBase.  # noqa: E501


        :return: The status of this RequestForQuotationBase.  # noqa: E501
        :rtype: NestedID
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RequestForQuotationBase.


        :param status: The status of this RequestForQuotationBase.  # noqa: E501
        :type: NestedID
        """

        self._status = status

    @property
    def sender(self):
        """Gets the sender of this RequestForQuotationBase.  # noqa: E501


        :return: The sender of this RequestForQuotationBase.  # noqa: E501
        :rtype: NestedID
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this RequestForQuotationBase.


        :param sender: The sender of this RequestForQuotationBase.  # noqa: E501
        :type: NestedID
        """

        self._sender = sender

    @property
    def receiver(self):
        """Gets the receiver of this RequestForQuotationBase.  # noqa: E501


        :return: The receiver of this RequestForQuotationBase.  # noqa: E501
        :rtype: NestedID
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this RequestForQuotationBase.


        :param receiver: The receiver of this RequestForQuotationBase.  # noqa: E501
        :type: NestedID
        """

        self._receiver = receiver

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
        if issubclass(RequestForQuotationBase, dict):
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
        if not isinstance(other, RequestForQuotationBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

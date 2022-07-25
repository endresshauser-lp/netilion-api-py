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

from netilion_api.configuration import Configuration


class SubscriptionResponse(object):
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
        'created_at': 'str',
        'updated_at': 'str',
        'user': 'NestedIDHref',
        'client_application': 'NestedIDHrefName',
        'billing_address': 'BillingAddressResponse',
        'shipping_address': 'ShippingAddressResponse',
        'successor': 'NestedIDHref',
        'predecessor': 'NestedIDHref',
        'customer': 'NestedIDHref',
        'usable': 'bool',
        'links': 'Links21'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'user': 'user',
        'client_application': 'client_application',
        'billing_address': 'billing_address',
        'shipping_address': 'shipping_address',
        'successor': 'successor',
        'predecessor': 'predecessor',
        'customer': 'customer',
        'usable': 'usable',
        'links': 'links'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, user=None, client_application=None, billing_address=None, shipping_address=None, successor=None, predecessor=None, customer=None, usable=None, links=None, _configuration=None):  # noqa: E501
        """SubscriptionResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._created_at = None
        self._updated_at = None
        self._user = None
        self._client_application = None
        self._billing_address = None
        self._shipping_address = None
        self._successor = None
        self._predecessor = None
        self._customer = None
        self._usable = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if user is not None:
            self.user = user
        if client_application is not None:
            self.client_application = client_application
        if billing_address is not None:
            self.billing_address = billing_address
        if shipping_address is not None:
            self.shipping_address = shipping_address
        if successor is not None:
            self.successor = successor
        if predecessor is not None:
            self.predecessor = predecessor
        if customer is not None:
            self.customer = customer
        if usable is not None:
            self.usable = usable
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this SubscriptionResponse.  # noqa: E501

        Id of object  # noqa: E501

        :return: The id of this SubscriptionResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionResponse.

        Id of object  # noqa: E501

        :param id: The id of this SubscriptionResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this SubscriptionResponse.  # noqa: E501

        Timestamp at which the subscription was created  # noqa: E501

        :return: The created_at of this SubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SubscriptionResponse.

        Timestamp at which the subscription was created  # noqa: E501

        :param created_at: The created_at of this SubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SubscriptionResponse.  # noqa: E501

        Timestamp at which the subscription was last changed  # noqa: E501

        :return: The updated_at of this SubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SubscriptionResponse.

        Timestamp at which the subscription was last changed  # noqa: E501

        :param updated_at: The updated_at of this SubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this SubscriptionResponse.  # noqa: E501


        :return: The user of this SubscriptionResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SubscriptionResponse.


        :param user: The user of this SubscriptionResponse.  # noqa: E501
        :type: NestedIDHref
        """

        self._user = user

    @property
    def client_application(self):
        """Gets the client_application of this SubscriptionResponse.  # noqa: E501


        :return: The client_application of this SubscriptionResponse.  # noqa: E501
        :rtype: NestedIDHrefName
        """
        return self._client_application

    @client_application.setter
    def client_application(self, client_application):
        """Sets the client_application of this SubscriptionResponse.


        :param client_application: The client_application of this SubscriptionResponse.  # noqa: E501
        :type: NestedIDHrefName
        """

        self._client_application = client_application

    @property
    def billing_address(self):
        """Gets the billing_address of this SubscriptionResponse.  # noqa: E501


        :return: The billing_address of this SubscriptionResponse.  # noqa: E501
        :rtype: BillingAddressResponse
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this SubscriptionResponse.


        :param billing_address: The billing_address of this SubscriptionResponse.  # noqa: E501
        :type: BillingAddressResponse
        """

        self._billing_address = billing_address

    @property
    def shipping_address(self):
        """Gets the shipping_address of this SubscriptionResponse.  # noqa: E501


        :return: The shipping_address of this SubscriptionResponse.  # noqa: E501
        :rtype: ShippingAddressResponse
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this SubscriptionResponse.


        :param shipping_address: The shipping_address of this SubscriptionResponse.  # noqa: E501
        :type: ShippingAddressResponse
        """

        self._shipping_address = shipping_address

    @property
    def successor(self):
        """Gets the successor of this SubscriptionResponse.  # noqa: E501


        :return: The successor of this SubscriptionResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._successor

    @successor.setter
    def successor(self, successor):
        """Sets the successor of this SubscriptionResponse.


        :param successor: The successor of this SubscriptionResponse.  # noqa: E501
        :type: NestedIDHref
        """

        self._successor = successor

    @property
    def predecessor(self):
        """Gets the predecessor of this SubscriptionResponse.  # noqa: E501


        :return: The predecessor of this SubscriptionResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._predecessor

    @predecessor.setter
    def predecessor(self, predecessor):
        """Sets the predecessor of this SubscriptionResponse.


        :param predecessor: The predecessor of this SubscriptionResponse.  # noqa: E501
        :type: NestedIDHref
        """

        self._predecessor = predecessor

    @property
    def customer(self):
        """Gets the customer of this SubscriptionResponse.  # noqa: E501


        :return: The customer of this SubscriptionResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this SubscriptionResponse.


        :param customer: The customer of this SubscriptionResponse.  # noqa: E501
        :type: NestedIDHref
        """

        self._customer = customer

    @property
    def usable(self):
        """Gets the usable of this SubscriptionResponse.  # noqa: E501

        indecates whether the subscription can be used as a user subscription (user is owner or a seat user) in our service applications e.g. Analytics. This information will only be part of the response if scope with value 'USER' is used.  # noqa: E501

        :return: The usable of this SubscriptionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._usable

    @usable.setter
    def usable(self, usable):
        """Sets the usable of this SubscriptionResponse.

        indecates whether the subscription can be used as a user subscription (user is owner or a seat user) in our service applications e.g. Analytics. This information will only be part of the response if scope with value 'USER' is used.  # noqa: E501

        :param usable: The usable of this SubscriptionResponse.  # noqa: E501
        :type: bool
        """

        self._usable = usable

    @property
    def links(self):
        """Gets the links of this SubscriptionResponse.  # noqa: E501


        :return: The links of this SubscriptionResponse.  # noqa: E501
        :rtype: Links21
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SubscriptionResponse.


        :param links: The links of this SubscriptionResponse.  # noqa: E501
        :type: Links21
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
        if issubclass(SubscriptionResponse, dict):
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
        if not isinstance(other, SubscriptionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionResponse):
            return True

        return self.to_dict() != other.to_dict()

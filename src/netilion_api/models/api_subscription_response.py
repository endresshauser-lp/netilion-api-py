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
from netilion_api.models.api_subscription_base import APISubscriptionBase  # noqa: F401,E501

class APISubscriptionResponse(APISubscriptionBase):
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
        'links': 'Links'
    }
    if hasattr(APISubscriptionBase, "swagger_types"):
        swagger_types.update(APISubscriptionBase.swagger_types)

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'user': 'user',
        'client_application': 'client_application',
        'billing_address': 'billing_address',
        'shipping_address': 'shipping_address',
        'links': 'links'
    }
    if hasattr(APISubscriptionBase, "attribute_map"):
        attribute_map.update(APISubscriptionBase.attribute_map)

    def __init__(self, id=None, created_at=None, updated_at=None, user=None, client_application=None, billing_address=None, shipping_address=None, links=None, *args, **kwargs):  # noqa: E501
        """APISubscriptionResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._user = None
        self._client_application = None
        self._billing_address = None
        self._shipping_address = None
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
        if links is not None:
            self.links = links
        APISubscriptionBase.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this APISubscriptionResponse.  # noqa: E501

        Id of object  # noqa: E501

        :return: The id of this APISubscriptionResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this APISubscriptionResponse.

        Id of object  # noqa: E501

        :param id: The id of this APISubscriptionResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this APISubscriptionResponse.  # noqa: E501

        Timestamp at which the api subscription was created  # noqa: E501

        :return: The created_at of this APISubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this APISubscriptionResponse.

        Timestamp at which the api subscription was created  # noqa: E501

        :param created_at: The created_at of this APISubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this APISubscriptionResponse.  # noqa: E501

        Timestamp at which the api subscription was last changed  # noqa: E501

        :return: The updated_at of this APISubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this APISubscriptionResponse.

        Timestamp at which the api subscription was last changed  # noqa: E501

        :param updated_at: The updated_at of this APISubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this APISubscriptionResponse.  # noqa: E501


        :return: The user of this APISubscriptionResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this APISubscriptionResponse.


        :param user: The user of this APISubscriptionResponse.  # noqa: E501
        :type: NestedIDHref
        """

        self._user = user

    @property
    def client_application(self):
        """Gets the client_application of this APISubscriptionResponse.  # noqa: E501


        :return: The client_application of this APISubscriptionResponse.  # noqa: E501
        :rtype: NestedIDHrefName
        """
        return self._client_application

    @client_application.setter
    def client_application(self, client_application):
        """Sets the client_application of this APISubscriptionResponse.


        :param client_application: The client_application of this APISubscriptionResponse.  # noqa: E501
        :type: NestedIDHrefName
        """

        self._client_application = client_application

    @property
    def billing_address(self):
        """Gets the billing_address of this APISubscriptionResponse.  # noqa: E501


        :return: The billing_address of this APISubscriptionResponse.  # noqa: E501
        :rtype: BillingAddressResponse
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this APISubscriptionResponse.


        :param billing_address: The billing_address of this APISubscriptionResponse.  # noqa: E501
        :type: BillingAddressResponse
        """

        self._billing_address = billing_address

    @property
    def shipping_address(self):
        """Gets the shipping_address of this APISubscriptionResponse.  # noqa: E501


        :return: The shipping_address of this APISubscriptionResponse.  # noqa: E501
        :rtype: ShippingAddressResponse
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this APISubscriptionResponse.


        :param shipping_address: The shipping_address of this APISubscriptionResponse.  # noqa: E501
        :type: ShippingAddressResponse
        """

        self._shipping_address = shipping_address

    @property
    def links(self):
        """Gets the links of this APISubscriptionResponse.  # noqa: E501


        :return: The links of this APISubscriptionResponse.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this APISubscriptionResponse.


        :param links: The links of this APISubscriptionResponse.  # noqa: E501
        :type: Links
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
        if issubclass(APISubscriptionResponse, dict):
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
        if not isinstance(other, APISubscriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
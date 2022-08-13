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

class Links6(object):
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
        'attachments': 'Link',
        'categories': 'Link',
        'assets': 'Link',
        'bill_of_materials': 'Link',
        'events': 'Link',
        'deliveries': 'Link',
        'products': 'Link',
        'instrumentations': 'Link',
        'nodes': 'Link',
        'purchase_orders': 'Link',
        'quotations': 'Link',
        'request_for_quotations': 'Link'
    }

    attribute_map = {
        'attachments': 'attachments',
        'categories': 'categories',
        'assets': 'assets',
        'bill_of_materials': 'bill_of_materials',
        'events': 'events',
        'deliveries': 'deliveries',
        'products': 'products',
        'instrumentations': 'instrumentations',
        'nodes': 'nodes',
        'purchase_orders': 'purchase_orders',
        'quotations': 'quotations',
        'request_for_quotations': 'request_for_quotations'
    }

    def __init__(self, attachments=None, categories=None, assets=None, bill_of_materials=None, events=None, deliveries=None, products=None, instrumentations=None, nodes=None, purchase_orders=None, quotations=None, request_for_quotations=None):  # noqa: E501
        """Links6 - a model defined in Swagger"""  # noqa: E501
        self._attachments = None
        self._categories = None
        self._assets = None
        self._bill_of_materials = None
        self._events = None
        self._deliveries = None
        self._products = None
        self._instrumentations = None
        self._nodes = None
        self._purchase_orders = None
        self._quotations = None
        self._request_for_quotations = None
        self.discriminator = None
        if attachments is not None:
            self.attachments = attachments
        if categories is not None:
            self.categories = categories
        if assets is not None:
            self.assets = assets
        if bill_of_materials is not None:
            self.bill_of_materials = bill_of_materials
        if events is not None:
            self.events = events
        if deliveries is not None:
            self.deliveries = deliveries
        if products is not None:
            self.products = products
        if instrumentations is not None:
            self.instrumentations = instrumentations
        if nodes is not None:
            self.nodes = nodes
        if purchase_orders is not None:
            self.purchase_orders = purchase_orders
        if quotations is not None:
            self.quotations = quotations
        if request_for_quotations is not None:
            self.request_for_quotations = request_for_quotations

    @property
    def attachments(self):
        """Gets the attachments of this Links6.  # noqa: E501


        :return: The attachments of this Links6.  # noqa: E501
        :rtype: Link
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Links6.


        :param attachments: The attachments of this Links6.  # noqa: E501
        :type: Link
        """

        self._attachments = attachments

    @property
    def categories(self):
        """Gets the categories of this Links6.  # noqa: E501


        :return: The categories of this Links6.  # noqa: E501
        :rtype: Link
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this Links6.


        :param categories: The categories of this Links6.  # noqa: E501
        :type: Link
        """

        self._categories = categories

    @property
    def assets(self):
        """Gets the assets of this Links6.  # noqa: E501


        :return: The assets of this Links6.  # noqa: E501
        :rtype: Link
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this Links6.


        :param assets: The assets of this Links6.  # noqa: E501
        :type: Link
        """

        self._assets = assets

    @property
    def bill_of_materials(self):
        """Gets the bill_of_materials of this Links6.  # noqa: E501


        :return: The bill_of_materials of this Links6.  # noqa: E501
        :rtype: Link
        """
        return self._bill_of_materials

    @bill_of_materials.setter
    def bill_of_materials(self, bill_of_materials):
        """Sets the bill_of_materials of this Links6.


        :param bill_of_materials: The bill_of_materials of this Links6.  # noqa: E501
        :type: Link
        """

        self._bill_of_materials = bill_of_materials

    @property
    def events(self):
        """Gets the events of this Links6.  # noqa: E501


        :return: The events of this Links6.  # noqa: E501
        :rtype: Link
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this Links6.


        :param events: The events of this Links6.  # noqa: E501
        :type: Link
        """

        self._events = events

    @property
    def deliveries(self):
        """Gets the deliveries of this Links6.  # noqa: E501


        :return: The deliveries of this Links6.  # noqa: E501
        :rtype: Link
        """
        return self._deliveries

    @deliveries.setter
    def deliveries(self, deliveries):
        """Sets the deliveries of this Links6.


        :param deliveries: The deliveries of this Links6.  # noqa: E501
        :type: Link
        """

        self._deliveries = deliveries

    @property
    def products(self):
        """Gets the products of this Links6.  # noqa: E501


        :return: The products of this Links6.  # noqa: E501
        :rtype: Link
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this Links6.


        :param products: The products of this Links6.  # noqa: E501
        :type: Link
        """

        self._products = products

    @property
    def instrumentations(self):
        """Gets the instrumentations of this Links6.  # noqa: E501


        :return: The instrumentations of this Links6.  # noqa: E501
        :rtype: Link
        """
        return self._instrumentations

    @instrumentations.setter
    def instrumentations(self, instrumentations):
        """Sets the instrumentations of this Links6.


        :param instrumentations: The instrumentations of this Links6.  # noqa: E501
        :type: Link
        """

        self._instrumentations = instrumentations

    @property
    def nodes(self):
        """Gets the nodes of this Links6.  # noqa: E501


        :return: The nodes of this Links6.  # noqa: E501
        :rtype: Link
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this Links6.


        :param nodes: The nodes of this Links6.  # noqa: E501
        :type: Link
        """

        self._nodes = nodes

    @property
    def purchase_orders(self):
        """Gets the purchase_orders of this Links6.  # noqa: E501


        :return: The purchase_orders of this Links6.  # noqa: E501
        :rtype: Link
        """
        return self._purchase_orders

    @purchase_orders.setter
    def purchase_orders(self, purchase_orders):
        """Sets the purchase_orders of this Links6.


        :param purchase_orders: The purchase_orders of this Links6.  # noqa: E501
        :type: Link
        """

        self._purchase_orders = purchase_orders

    @property
    def quotations(self):
        """Gets the quotations of this Links6.  # noqa: E501


        :return: The quotations of this Links6.  # noqa: E501
        :rtype: Link
        """
        return self._quotations

    @quotations.setter
    def quotations(self, quotations):
        """Sets the quotations of this Links6.


        :param quotations: The quotations of this Links6.  # noqa: E501
        :type: Link
        """

        self._quotations = quotations

    @property
    def request_for_quotations(self):
        """Gets the request_for_quotations of this Links6.  # noqa: E501


        :return: The request_for_quotations of this Links6.  # noqa: E501
        :rtype: Link
        """
        return self._request_for_quotations

    @request_for_quotations.setter
    def request_for_quotations(self, request_for_quotations):
        """Sets the request_for_quotations of this Links6.


        :param request_for_quotations: The request_for_quotations of this Links6.  # noqa: E501
        :type: Link
        """

        self._request_for_quotations = request_for_quotations

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
        if issubclass(Links6, dict):
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
        if not isinstance(other, Links6):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

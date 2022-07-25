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


class AssetValuesPagination(object):
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
        'total_count': 'int',
        'page_count': 'int',
        'per_page': 'int',
        'page': 'int',
        'prev': 'str',
        'next': 'str',
        'first': 'str',
        'last': 'str'
    }

    attribute_map = {
        'total_count': 'total_count',
        'page_count': 'page_count',
        'per_page': 'per_page',
        'page': 'page',
        'prev': 'prev',
        'next': 'next',
        'first': 'first',
        'last': 'last'
    }

    def __init__(self, total_count=None, page_count=None, per_page=None, page=None, prev=None, next=None, first=None, last=None, _configuration=None):  # noqa: E501
        """AssetValuesPagination - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._total_count = None
        self._page_count = None
        self._per_page = None
        self._page = None
        self._prev = None
        self._next = None
        self._first = None
        self._last = None
        self.discriminator = None

        self.total_count = total_count
        self.page_count = page_count
        self.per_page = per_page
        self.page = page
        if prev is not None:
            self.prev = prev
        if next is not None:
            self.next = next
        if first is not None:
            self.first = first
        if last is not None:
            self.last = last

    @property
    def total_count(self):
        """Gets the total_count of this AssetValuesPagination.  # noqa: E501

        data items in the result  # noqa: E501

        :return: The total_count of this AssetValuesPagination.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this AssetValuesPagination.

        data items in the result  # noqa: E501

        :param total_count: The total_count of this AssetValuesPagination.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

    @property
    def page_count(self):
        """Gets the page_count of this AssetValuesPagination.  # noqa: E501

        number of pages  # noqa: E501

        :return: The page_count of this AssetValuesPagination.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this AssetValuesPagination.

        number of pages  # noqa: E501

        :param page_count: The page_count of this AssetValuesPagination.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_count is None:
            raise ValueError("Invalid value for `page_count`, must not be `None`")  # noqa: E501

        self._page_count = page_count

    @property
    def per_page(self):
        """Gets the per_page of this AssetValuesPagination.  # noqa: E501

        items per page  # noqa: E501

        :return: The per_page of this AssetValuesPagination.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this AssetValuesPagination.

        items per page  # noqa: E501

        :param per_page: The per_page of this AssetValuesPagination.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and per_page is None:
            raise ValueError("Invalid value for `per_page`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                per_page is not None and per_page > 1000):  # noqa: E501
            raise ValueError("Invalid value for `per_page`, must be a value less than or equal to `1000`")  # noqa: E501
        if (self._configuration.client_side_validation and
                per_page is not None and per_page < 1):  # noqa: E501
            raise ValueError("Invalid value for `per_page`, must be a value greater than or equal to `1`")  # noqa: E501

        self._per_page = per_page

    @property
    def page(self):
        """Gets the page of this AssetValuesPagination.  # noqa: E501

        current page  # noqa: E501

        :return: The page of this AssetValuesPagination.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this AssetValuesPagination.

        current page  # noqa: E501

        :param page: The page of this AssetValuesPagination.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page is None:
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def prev(self):
        """Gets the prev of this AssetValuesPagination.  # noqa: E501

        The link for the immediate previous page for the data.  # noqa: E501

        :return: The prev of this AssetValuesPagination.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this AssetValuesPagination.

        The link for the immediate previous page for the data.  # noqa: E501

        :param prev: The prev of this AssetValuesPagination.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def next(self):
        """Gets the next of this AssetValuesPagination.  # noqa: E501

        The link for the immediate next page for the data.  # noqa: E501

        :return: The next of this AssetValuesPagination.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this AssetValuesPagination.

        The link for the immediate next page for the data.  # noqa: E501

        :param next: The next of this AssetValuesPagination.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def first(self):
        """Gets the first of this AssetValuesPagination.  # noqa: E501

        The link for the first page for the data.  # noqa: E501

        :return: The first of this AssetValuesPagination.  # noqa: E501
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this AssetValuesPagination.

        The link for the first page for the data.  # noqa: E501

        :param first: The first of this AssetValuesPagination.  # noqa: E501
        :type: str
        """

        self._first = first

    @property
    def last(self):
        """Gets the last of this AssetValuesPagination.  # noqa: E501

        The link for the last page for the data.  # noqa: E501

        :return: The last of this AssetValuesPagination.  # noqa: E501
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this AssetValuesPagination.

        The link for the last page for the data.  # noqa: E501

        :param last: The last of this AssetValuesPagination.  # noqa: E501
        :type: str
        """

        self._last = last

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
        if issubclass(AssetValuesPagination, dict):
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
        if not isinstance(other, AssetValuesPagination):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetValuesPagination):
            return True

        return self.to_dict() != other.to_dict()

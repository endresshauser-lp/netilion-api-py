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

class RequestUser(object):
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
        'href': 'str',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'email': 'email',
        'first_name': 'first_name',
        'last_name': 'last_name'
    }

    def __init__(self, id=None, href=None, email=None, first_name=None, last_name=None):  # noqa: E501
        """RequestUser - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self.discriminator = None
        self.id = id
        self.href = href
        self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name

    @property
    def id(self):
        """Gets the id of this RequestUser.  # noqa: E501

        id of the request user  # noqa: E501

        :return: The id of this RequestUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RequestUser.

        id of the request user  # noqa: E501

        :param id: The id of this RequestUser.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this RequestUser.  # noqa: E501

        href to the request user  # noqa: E501

        :return: The href of this RequestUser.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this RequestUser.

        href to the request user  # noqa: E501

        :param href: The href of this RequestUser.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def email(self):
        """Gets the email of this RequestUser.  # noqa: E501

        email of the request user  # noqa: E501

        :return: The email of this RequestUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RequestUser.

        email of the request user  # noqa: E501

        :param email: The email of this RequestUser.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this RequestUser.  # noqa: E501

        first_name of the request user  # noqa: E501

        :return: The first_name of this RequestUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this RequestUser.

        first_name of the request user  # noqa: E501

        :param first_name: The first_name of this RequestUser.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this RequestUser.  # noqa: E501

        last_name of the request user  # noqa: E501

        :return: The last_name of this RequestUser.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this RequestUser.

        last_name of the request user  # noqa: E501

        :param last_name: The last_name of this RequestUser.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

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
        if issubclass(RequestUser, dict):
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
        if not isinstance(other, RequestUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
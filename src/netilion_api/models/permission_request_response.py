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

class PermissionRequestResponse(object):
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
        'status': 'str',
        'request_message': 'str',
        'response_message': 'str',
        'permitable': 'Permitable1',
        'request_user': 'RequestUser',
        'response_user': 'ResponseUser'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'request_message': 'request_message',
        'response_message': 'response_message',
        'permitable': 'permitable',
        'request_user': 'request_user',
        'response_user': 'response_user'
    }

    def __init__(self, id=None, status=None, request_message=None, response_message=None, permitable=None, request_user=None, response_user=None):  # noqa: E501
        """PermissionRequestResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._request_message = None
        self._response_message = None
        self._permitable = None
        self._request_user = None
        self._response_user = None
        self.discriminator = None
        self.id = id
        self.status = status
        if request_message is not None:
            self.request_message = request_message
        if response_message is not None:
            self.response_message = response_message
        self.permitable = permitable
        self.request_user = request_user
        if response_user is not None:
            self.response_user = response_user

    @property
    def id(self):
        """Gets the id of this PermissionRequestResponse.  # noqa: E501


        :return: The id of this PermissionRequestResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PermissionRequestResponse.


        :param id: The id of this PermissionRequestResponse.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self):
        """Gets the status of this PermissionRequestResponse.  # noqa: E501

        possible values are: open, accepted, rejected  # noqa: E501

        :return: The status of this PermissionRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PermissionRequestResponse.

        possible values are: open, accepted, rejected  # noqa: E501

        :param status: The status of this PermissionRequestResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def request_message(self):
        """Gets the request_message of this PermissionRequestResponse.  # noqa: E501

        message of the requester to the owner  # noqa: E501

        :return: The request_message of this PermissionRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_message

    @request_message.setter
    def request_message(self, request_message):
        """Sets the request_message of this PermissionRequestResponse.

        message of the requester to the owner  # noqa: E501

        :param request_message: The request_message of this PermissionRequestResponse.  # noqa: E501
        :type: str
        """

        self._request_message = request_message

    @property
    def response_message(self):
        """Gets the response_message of this PermissionRequestResponse.  # noqa: E501

        message of the owner to the requester  # noqa: E501

        :return: The response_message of this PermissionRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._response_message

    @response_message.setter
    def response_message(self, response_message):
        """Sets the response_message of this PermissionRequestResponse.

        message of the owner to the requester  # noqa: E501

        :param response_message: The response_message of this PermissionRequestResponse.  # noqa: E501
        :type: str
        """

        self._response_message = response_message

    @property
    def permitable(self):
        """Gets the permitable of this PermissionRequestResponse.  # noqa: E501


        :return: The permitable of this PermissionRequestResponse.  # noqa: E501
        :rtype: Permitable1
        """
        return self._permitable

    @permitable.setter
    def permitable(self, permitable):
        """Sets the permitable of this PermissionRequestResponse.


        :param permitable: The permitable of this PermissionRequestResponse.  # noqa: E501
        :type: Permitable1
        """
        if permitable is None:
            raise ValueError("Invalid value for `permitable`, must not be `None`")  # noqa: E501

        self._permitable = permitable

    @property
    def request_user(self):
        """Gets the request_user of this PermissionRequestResponse.  # noqa: E501


        :return: The request_user of this PermissionRequestResponse.  # noqa: E501
        :rtype: RequestUser
        """
        return self._request_user

    @request_user.setter
    def request_user(self, request_user):
        """Sets the request_user of this PermissionRequestResponse.


        :param request_user: The request_user of this PermissionRequestResponse.  # noqa: E501
        :type: RequestUser
        """
        if request_user is None:
            raise ValueError("Invalid value for `request_user`, must not be `None`")  # noqa: E501

        self._request_user = request_user

    @property
    def response_user(self):
        """Gets the response_user of this PermissionRequestResponse.  # noqa: E501


        :return: The response_user of this PermissionRequestResponse.  # noqa: E501
        :rtype: ResponseUser
        """
        return self._response_user

    @response_user.setter
    def response_user(self, response_user):
        """Sets the response_user of this PermissionRequestResponse.


        :param response_user: The response_user of this PermissionRequestResponse.  # noqa: E501
        :type: ResponseUser
        """

        self._response_user = response_user

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
        if issubclass(PermissionRequestResponse, dict):
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
        if not isinstance(other, PermissionRequestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

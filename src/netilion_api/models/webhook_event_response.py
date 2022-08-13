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

class WebhookEventResponse(object):
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
        'payload': 'object',
        'last_send_at': 'str',
        'retries': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'payload': 'payload',
        'last_send_at': 'last_send_at',
        'retries': 'retries'
    }

    def __init__(self, id=None, status=None, payload=None, last_send_at=None, retries=None):  # noqa: E501
        """WebhookEventResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._payload = None
        self._last_send_at = None
        self._retries = None
        self.discriminator = None
        self.id = id
        if status is not None:
            self.status = status
        if payload is not None:
            self.payload = payload
        if last_send_at is not None:
            self.last_send_at = last_send_at
        if retries is not None:
            self.retries = retries

    @property
    def id(self):
        """Gets the id of this WebhookEventResponse.  # noqa: E501

        Id of webhook event  # noqa: E501

        :return: The id of this WebhookEventResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookEventResponse.

        Id of webhook event  # noqa: E501

        :param id: The id of this WebhookEventResponse.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self):
        """Gets the status of this WebhookEventResponse.  # noqa: E501

        status of the event, possible values are pending, delivered, cancelled and failed  # noqa: E501

        :return: The status of this WebhookEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebhookEventResponse.

        status of the event, possible values are pending, delivered, cancelled and failed  # noqa: E501

        :param status: The status of this WebhookEventResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def payload(self):
        """Gets the payload of this WebhookEventResponse.  # noqa: E501

        payload of the webhook event  # noqa: E501

        :return: The payload of this WebhookEventResponse.  # noqa: E501
        :rtype: object
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this WebhookEventResponse.

        payload of the webhook event  # noqa: E501

        :param payload: The payload of this WebhookEventResponse.  # noqa: E501
        :type: object
        """

        self._payload = payload

    @property
    def last_send_at(self):
        """Gets the last_send_at of this WebhookEventResponse.  # noqa: E501

        datewhen webhook event was last send  # noqa: E501

        :return: The last_send_at of this WebhookEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_send_at

    @last_send_at.setter
    def last_send_at(self, last_send_at):
        """Sets the last_send_at of this WebhookEventResponse.

        datewhen webhook event was last send  # noqa: E501

        :param last_send_at: The last_send_at of this WebhookEventResponse.  # noqa: E501
        :type: str
        """

        self._last_send_at = last_send_at

    @property
    def retries(self):
        """Gets the retries of this WebhookEventResponse.  # noqa: E501

        number of retries to send the event  # noqa: E501

        :return: The retries of this WebhookEventResponse.  # noqa: E501
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this WebhookEventResponse.

        number of retries to send the event  # noqa: E501

        :param retries: The retries of this WebhookEventResponse.  # noqa: E501
        :type: int
        """

        self._retries = retries

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
        if issubclass(WebhookEventResponse, dict):
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
        if not isinstance(other, WebhookEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
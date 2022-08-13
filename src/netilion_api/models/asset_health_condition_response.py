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
from netilion_api.models.health_condition_base import HealthConditionBase  # noqa: F401,E501

class AssetHealthConditionResponse(HealthConditionBase):
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
        'asset_status': 'NestedIDHref',
        'channel': 'str',
        'module': 'str',
        'links': 'Links1'
    }
    if hasattr(HealthConditionBase, "swagger_types"):
        swagger_types.update(HealthConditionBase.swagger_types)

    attribute_map = {
        'id': 'id',
        'asset_status': 'asset_status',
        'channel': 'channel',
        'module': 'module',
        'links': 'links'
    }
    if hasattr(HealthConditionBase, "attribute_map"):
        attribute_map.update(HealthConditionBase.attribute_map)

    def __init__(self, id=None, asset_status=None, channel=None, module=None, links=None, *args, **kwargs):  # noqa: E501
        """AssetHealthConditionResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._asset_status = None
        self._channel = None
        self._module = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if asset_status is not None:
            self.asset_status = asset_status
        if channel is not None:
            self.channel = channel
        if module is not None:
            self.module = module
        if links is not None:
            self.links = links
        HealthConditionBase.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this AssetHealthConditionResponse.  # noqa: E501

        Id of health condition  # noqa: E501

        :return: The id of this AssetHealthConditionResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetHealthConditionResponse.

        Id of health condition  # noqa: E501

        :param id: The id of this AssetHealthConditionResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def asset_status(self):
        """Gets the asset_status of this AssetHealthConditionResponse.  # noqa: E501


        :return: The asset_status of this AssetHealthConditionResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._asset_status

    @asset_status.setter
    def asset_status(self, asset_status):
        """Sets the asset_status of this AssetHealthConditionResponse.


        :param asset_status: The asset_status of this AssetHealthConditionResponse.  # noqa: E501
        :type: NestedIDHref
        """

        self._asset_status = asset_status

    @property
    def channel(self):
        """Gets the channel of this AssetHealthConditionResponse.  # noqa: E501

        channel for the health condition  # noqa: E501

        :return: The channel of this AssetHealthConditionResponse.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this AssetHealthConditionResponse.

        channel for the health condition  # noqa: E501

        :param channel: The channel of this AssetHealthConditionResponse.  # noqa: E501
        :type: str
        """

        self._channel = channel

    @property
    def module(self):
        """Gets the module of this AssetHealthConditionResponse.  # noqa: E501

        module for the health condition  # noqa: E501

        :return: The module of this AssetHealthConditionResponse.  # noqa: E501
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this AssetHealthConditionResponse.

        module for the health condition  # noqa: E501

        :param module: The module of this AssetHealthConditionResponse.  # noqa: E501
        :type: str
        """

        self._module = module

    @property
    def links(self):
        """Gets the links of this AssetHealthConditionResponse.  # noqa: E501


        :return: The links of this AssetHealthConditionResponse.  # noqa: E501
        :rtype: Links1
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AssetHealthConditionResponse.


        :param links: The links of this AssetHealthConditionResponse.  # noqa: E501
        :type: Links1
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
        if issubclass(AssetHealthConditionResponse, dict):
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
        if not isinstance(other, AssetHealthConditionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

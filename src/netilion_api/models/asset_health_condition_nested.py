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

class AssetHealthConditionNested(object):
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
        'diagnosis_code': 'str',
        'asset_status': 'NestedIDHref',
        'channel': 'str',
        'module': 'str',
        'links': 'Links1'
    }

    attribute_map = {
        'id': 'id',
        'diagnosis_code': 'diagnosis_code',
        'asset_status': 'asset_status',
        'channel': 'channel',
        'module': 'module',
        'links': 'links'
    }

    def __init__(self, id=None, diagnosis_code=None, asset_status=None, channel=None, module=None, links=None):  # noqa: E501
        """AssetHealthConditionNested - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._diagnosis_code = None
        self._asset_status = None
        self._channel = None
        self._module = None
        self._links = None
        self.discriminator = None
        self.id = id
        self.diagnosis_code = diagnosis_code
        self.asset_status = asset_status
        self.channel = channel
        self.module = module
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this AssetHealthConditionNested.  # noqa: E501

        ID of the nested resources  # noqa: E501

        :return: The id of this AssetHealthConditionNested.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetHealthConditionNested.

        ID of the nested resources  # noqa: E501

        :param id: The id of this AssetHealthConditionNested.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def diagnosis_code(self):
        """Gets the diagnosis_code of this AssetHealthConditionNested.  # noqa: E501

        diagnosis_code of the nested resource  # noqa: E501

        :return: The diagnosis_code of this AssetHealthConditionNested.  # noqa: E501
        :rtype: str
        """
        return self._diagnosis_code

    @diagnosis_code.setter
    def diagnosis_code(self, diagnosis_code):
        """Sets the diagnosis_code of this AssetHealthConditionNested.

        diagnosis_code of the nested resource  # noqa: E501

        :param diagnosis_code: The diagnosis_code of this AssetHealthConditionNested.  # noqa: E501
        :type: str
        """
        if diagnosis_code is None:
            raise ValueError("Invalid value for `diagnosis_code`, must not be `None`")  # noqa: E501

        self._diagnosis_code = diagnosis_code

    @property
    def asset_status(self):
        """Gets the asset_status of this AssetHealthConditionNested.  # noqa: E501


        :return: The asset_status of this AssetHealthConditionNested.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._asset_status

    @asset_status.setter
    def asset_status(self, asset_status):
        """Sets the asset_status of this AssetHealthConditionNested.


        :param asset_status: The asset_status of this AssetHealthConditionNested.  # noqa: E501
        :type: NestedIDHref
        """
        if asset_status is None:
            raise ValueError("Invalid value for `asset_status`, must not be `None`")  # noqa: E501

        self._asset_status = asset_status

    @property
    def channel(self):
        """Gets the channel of this AssetHealthConditionNested.  # noqa: E501

        channel of the nested resource  # noqa: E501

        :return: The channel of this AssetHealthConditionNested.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this AssetHealthConditionNested.

        channel of the nested resource  # noqa: E501

        :param channel: The channel of this AssetHealthConditionNested.  # noqa: E501
        :type: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def module(self):
        """Gets the module of this AssetHealthConditionNested.  # noqa: E501

        module of the nested resource  # noqa: E501

        :return: The module of this AssetHealthConditionNested.  # noqa: E501
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this AssetHealthConditionNested.

        module of the nested resource  # noqa: E501

        :param module: The module of this AssetHealthConditionNested.  # noqa: E501
        :type: str
        """
        if module is None:
            raise ValueError("Invalid value for `module`, must not be `None`")  # noqa: E501

        self._module = module

    @property
    def links(self):
        """Gets the links of this AssetHealthConditionNested.  # noqa: E501


        :return: The links of this AssetHealthConditionNested.  # noqa: E501
        :rtype: Links1
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AssetHealthConditionNested.


        :param links: The links of this AssetHealthConditionNested.  # noqa: E501
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
        if issubclass(AssetHealthConditionNested, dict):
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
        if not isinstance(other, AssetHealthConditionNested):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

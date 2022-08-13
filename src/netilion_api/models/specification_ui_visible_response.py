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
from netilion_api.models.specification_base import SpecificationBase  # noqa: F401,E501

class SpecificationUIVisibleResponse(SpecificationBase):
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
        'updated_at': 'str',
        'ui_visible': 'bool'
    }
    if hasattr(SpecificationBase, "swagger_types"):
        swagger_types.update(SpecificationBase.swagger_types)

    attribute_map = {
        'updated_at': 'updated_at',
        'ui_visible': 'ui_visible'
    }
    if hasattr(SpecificationBase, "attribute_map"):
        attribute_map.update(SpecificationBase.attribute_map)

    def __init__(self, updated_at=None, ui_visible=None, *args, **kwargs):  # noqa: E501
        """SpecificationUIVisibleResponse - a model defined in Swagger"""  # noqa: E501
        self._updated_at = None
        self._ui_visible = None
        self.discriminator = None
        if updated_at is not None:
            self.updated_at = updated_at
        if ui_visible is not None:
            self.ui_visible = ui_visible
        SpecificationBase.__init__(self, *args, **kwargs)

    @property
    def updated_at(self):
        """Gets the updated_at of this SpecificationUIVisibleResponse.  # noqa: E501

        date of the last modification  # noqa: E501

        :return: The updated_at of this SpecificationUIVisibleResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SpecificationUIVisibleResponse.

        date of the last modification  # noqa: E501

        :param updated_at: The updated_at of this SpecificationUIVisibleResponse.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def ui_visible(self):
        """Gets the ui_visible of this SpecificationUIVisibleResponse.  # noqa: E501

        specification should be visible in ui  # noqa: E501

        :return: The ui_visible of this SpecificationUIVisibleResponse.  # noqa: E501
        :rtype: bool
        """
        return self._ui_visible

    @ui_visible.setter
    def ui_visible(self, ui_visible):
        """Sets the ui_visible of this SpecificationUIVisibleResponse.

        specification should be visible in ui  # noqa: E501

        :param ui_visible: The ui_visible of this SpecificationUIVisibleResponse.  # noqa: E501
        :type: bool
        """

        self._ui_visible = ui_visible

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
        if issubclass(SpecificationUIVisibleResponse, dict):
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
        if not isinstance(other, SpecificationUIVisibleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

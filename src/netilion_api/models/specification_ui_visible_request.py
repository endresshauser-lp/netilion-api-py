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
from netilion_api.models.specification_request import SpecificationRequest  # noqa: F401,E501

class SpecificationUIVisibleRequest(SpecificationRequest):
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
        'ui_visible': 'bool'
    }
    if hasattr(SpecificationRequest, "swagger_types"):
        swagger_types.update(SpecificationRequest.swagger_types)

    attribute_map = {
        'ui_visible': 'ui_visible'
    }
    if hasattr(SpecificationRequest, "attribute_map"):
        attribute_map.update(SpecificationRequest.attribute_map)

    def __init__(self, ui_visible=False, *args, **kwargs):  # noqa: E501
        """SpecificationUIVisibleRequest - a model defined in Swagger"""  # noqa: E501
        self._ui_visible = None
        self.discriminator = None
        if ui_visible is not None:
            self.ui_visible = ui_visible
        SpecificationRequest.__init__(self, *args, **kwargs)

    @property
    def ui_visible(self):
        """Gets the ui_visible of this SpecificationUIVisibleRequest.  # noqa: E501

        specification should be visible in ui  # noqa: E501

        :return: The ui_visible of this SpecificationUIVisibleRequest.  # noqa: E501
        :rtype: bool
        """
        return self._ui_visible

    @ui_visible.setter
    def ui_visible(self, ui_visible):
        """Sets the ui_visible of this SpecificationUIVisibleRequest.

        specification should be visible in ui  # noqa: E501

        :param ui_visible: The ui_visible of this SpecificationUIVisibleRequest.  # noqa: E501
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
        if issubclass(SpecificationUIVisibleRequest, dict):
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
        if not isinstance(other, SpecificationUIVisibleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

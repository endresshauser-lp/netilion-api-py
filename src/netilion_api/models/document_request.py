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
from netilion_api.models.document_base import DocumentBase  # noqa: F401,E501

class DocumentRequest(DocumentBase):
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
        'classification': 'NestedID',
        'status': 'NestedID',
        'tenant': 'NestedID'
    }
    if hasattr(DocumentBase, "swagger_types"):
        swagger_types.update(DocumentBase.swagger_types)

    attribute_map = {
        'classification': 'classification',
        'status': 'status',
        'tenant': 'tenant'
    }
    if hasattr(DocumentBase, "attribute_map"):
        attribute_map.update(DocumentBase.attribute_map)

    def __init__(self, classification=None, status=None, tenant=None, *args, **kwargs):  # noqa: E501
        """DocumentRequest - a model defined in Swagger"""  # noqa: E501
        self._classification = None
        self._status = None
        self._tenant = None
        self.discriminator = None
        if classification is not None:
            self.classification = classification
        if status is not None:
            self.status = status
        if tenant is not None:
            self.tenant = tenant
        DocumentBase.__init__(self, *args, **kwargs)

    @property
    def classification(self):
        """Gets the classification of this DocumentRequest.  # noqa: E501


        :return: The classification of this DocumentRequest.  # noqa: E501
        :rtype: NestedID
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this DocumentRequest.


        :param classification: The classification of this DocumentRequest.  # noqa: E501
        :type: NestedID
        """

        self._classification = classification

    @property
    def status(self):
        """Gets the status of this DocumentRequest.  # noqa: E501


        :return: The status of this DocumentRequest.  # noqa: E501
        :rtype: NestedID
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DocumentRequest.


        :param status: The status of this DocumentRequest.  # noqa: E501
        :type: NestedID
        """

        self._status = status

    @property
    def tenant(self):
        """Gets the tenant of this DocumentRequest.  # noqa: E501


        :return: The tenant of this DocumentRequest.  # noqa: E501
        :rtype: NestedID
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this DocumentRequest.


        :param tenant: The tenant of this DocumentRequest.  # noqa: E501
        :type: NestedID
        """

        self._tenant = tenant

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
        if issubclass(DocumentRequest, dict):
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
        if not isinstance(other, DocumentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
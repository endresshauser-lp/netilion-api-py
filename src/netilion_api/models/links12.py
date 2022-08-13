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

class Links12(object):
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
        'assets': 'Link',
        'bill_of_materials': 'Link',
        'documents': 'Link',
        'nodes': 'Link',
        'pictures': 'Link',
        'specifications': 'Link',
        'thresholds': 'Link'
    }

    attribute_map = {
        'assets': 'assets',
        'bill_of_materials': 'bill_of_materials',
        'documents': 'documents',
        'nodes': 'nodes',
        'pictures': 'pictures',
        'specifications': 'specifications',
        'thresholds': 'thresholds'
    }

    def __init__(self, assets=None, bill_of_materials=None, documents=None, nodes=None, pictures=None, specifications=None, thresholds=None):  # noqa: E501
        """Links12 - a model defined in Swagger"""  # noqa: E501
        self._assets = None
        self._bill_of_materials = None
        self._documents = None
        self._nodes = None
        self._pictures = None
        self._specifications = None
        self._thresholds = None
        self.discriminator = None
        if assets is not None:
            self.assets = assets
        if bill_of_materials is not None:
            self.bill_of_materials = bill_of_materials
        if documents is not None:
            self.documents = documents
        if nodes is not None:
            self.nodes = nodes
        if pictures is not None:
            self.pictures = pictures
        if specifications is not None:
            self.specifications = specifications
        if thresholds is not None:
            self.thresholds = thresholds

    @property
    def assets(self):
        """Gets the assets of this Links12.  # noqa: E501


        :return: The assets of this Links12.  # noqa: E501
        :rtype: Link
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this Links12.


        :param assets: The assets of this Links12.  # noqa: E501
        :type: Link
        """

        self._assets = assets

    @property
    def bill_of_materials(self):
        """Gets the bill_of_materials of this Links12.  # noqa: E501


        :return: The bill_of_materials of this Links12.  # noqa: E501
        :rtype: Link
        """
        return self._bill_of_materials

    @bill_of_materials.setter
    def bill_of_materials(self, bill_of_materials):
        """Sets the bill_of_materials of this Links12.


        :param bill_of_materials: The bill_of_materials of this Links12.  # noqa: E501
        :type: Link
        """

        self._bill_of_materials = bill_of_materials

    @property
    def documents(self):
        """Gets the documents of this Links12.  # noqa: E501


        :return: The documents of this Links12.  # noqa: E501
        :rtype: Link
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this Links12.


        :param documents: The documents of this Links12.  # noqa: E501
        :type: Link
        """

        self._documents = documents

    @property
    def nodes(self):
        """Gets the nodes of this Links12.  # noqa: E501


        :return: The nodes of this Links12.  # noqa: E501
        :rtype: Link
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this Links12.


        :param nodes: The nodes of this Links12.  # noqa: E501
        :type: Link
        """

        self._nodes = nodes

    @property
    def pictures(self):
        """Gets the pictures of this Links12.  # noqa: E501


        :return: The pictures of this Links12.  # noqa: E501
        :rtype: Link
        """
        return self._pictures

    @pictures.setter
    def pictures(self, pictures):
        """Sets the pictures of this Links12.


        :param pictures: The pictures of this Links12.  # noqa: E501
        :type: Link
        """

        self._pictures = pictures

    @property
    def specifications(self):
        """Gets the specifications of this Links12.  # noqa: E501


        :return: The specifications of this Links12.  # noqa: E501
        :rtype: Link
        """
        return self._specifications

    @specifications.setter
    def specifications(self, specifications):
        """Sets the specifications of this Links12.


        :param specifications: The specifications of this Links12.  # noqa: E501
        :type: Link
        """

        self._specifications = specifications

    @property
    def thresholds(self):
        """Gets the thresholds of this Links12.  # noqa: E501


        :return: The thresholds of this Links12.  # noqa: E501
        :rtype: Link
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this Links12.


        :param thresholds: The thresholds of this Links12.  # noqa: E501
        :type: Link
        """

        self._thresholds = thresholds

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
        if issubclass(Links12, dict):
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
        if not isinstance(other, Links12):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

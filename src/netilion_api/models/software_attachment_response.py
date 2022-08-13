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

class SoftwareAttachmentResponse(object):
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
        'type': 'str',
        'file_name': 'str',
        'fingerprint': 'str',
        'content_date': 'str',
        'remarks': 'str',
        'software': 'NestedIDHref',
        'download_href': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'file_name': 'file_name',
        'fingerprint': 'fingerprint',
        'content_date': 'content_date',
        'remarks': 'remarks',
        'software': 'software',
        'download_href': 'download_href'
    }

    def __init__(self, id=None, type=None, file_name=None, fingerprint=None, content_date=None, remarks=None, software=None, download_href=None):  # noqa: E501
        """SoftwareAttachmentResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._file_name = None
        self._fingerprint = None
        self._content_date = None
        self._remarks = None
        self._software = None
        self._download_href = None
        self.discriminator = None
        self.id = id
        self.type = type
        if file_name is not None:
            self.file_name = file_name
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if content_date is not None:
            self.content_date = content_date
        if remarks is not None:
            self.remarks = remarks
        self.software = software
        self.download_href = download_href

    @property
    def id(self):
        """Gets the id of this SoftwareAttachmentResponse.  # noqa: E501

        Id of object  # noqa: E501

        :return: The id of this SoftwareAttachmentResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SoftwareAttachmentResponse.

        Id of object  # noqa: E501

        :param id: The id of this SoftwareAttachmentResponse.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this SoftwareAttachmentResponse.  # noqa: E501

        type of software attachment, can be 'file' or 'link'  # noqa: E501

        :return: The type of this SoftwareAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SoftwareAttachmentResponse.

        type of software attachment, can be 'file' or 'link'  # noqa: E501

        :param type: The type of this SoftwareAttachmentResponse.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def file_name(self):
        """Gets the file_name of this SoftwareAttachmentResponse.  # noqa: E501

        the original filename of the software attachment  # noqa: E501

        :return: The file_name of this SoftwareAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this SoftwareAttachmentResponse.

        the original filename of the software attachment  # noqa: E501

        :param file_name: The file_name of this SoftwareAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def fingerprint(self):
        """Gets the fingerprint of this SoftwareAttachmentResponse.  # noqa: E501

        SHA256 checksum of the file  # noqa: E501

        :return: The fingerprint of this SoftwareAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this SoftwareAttachmentResponse.

        SHA256 checksum of the file  # noqa: E501

        :param fingerprint: The fingerprint of this SoftwareAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def content_date(self):
        """Gets the content_date of this SoftwareAttachmentResponse.  # noqa: E501

        last edit date of the file  # noqa: E501

        :return: The content_date of this SoftwareAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._content_date

    @content_date.setter
    def content_date(self, content_date):
        """Sets the content_date of this SoftwareAttachmentResponse.

        last edit date of the file  # noqa: E501

        :param content_date: The content_date of this SoftwareAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._content_date = content_date

    @property
    def remarks(self):
        """Gets the remarks of this SoftwareAttachmentResponse.  # noqa: E501

        remarks of the software attachment  # noqa: E501

        :return: The remarks of this SoftwareAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this SoftwareAttachmentResponse.

        remarks of the software attachment  # noqa: E501

        :param remarks: The remarks of this SoftwareAttachmentResponse.  # noqa: E501
        :type: str
        """

        self._remarks = remarks

    @property
    def software(self):
        """Gets the software of this SoftwareAttachmentResponse.  # noqa: E501


        :return: The software of this SoftwareAttachmentResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._software

    @software.setter
    def software(self, software):
        """Sets the software of this SoftwareAttachmentResponse.


        :param software: The software of this SoftwareAttachmentResponse.  # noqa: E501
        :type: NestedIDHref
        """
        if software is None:
            raise ValueError("Invalid value for `software`, must not be `None`")  # noqa: E501

        self._software = software

    @property
    def download_href(self):
        """Gets the download_href of this SoftwareAttachmentResponse.  # noqa: E501

        the download link to the file of the software attachment  # noqa: E501

        :return: The download_href of this SoftwareAttachmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._download_href

    @download_href.setter
    def download_href(self, download_href):
        """Sets the download_href of this SoftwareAttachmentResponse.

        the download link to the file of the software attachment  # noqa: E501

        :param download_href: The download_href of this SoftwareAttachmentResponse.  # noqa: E501
        :type: str
        """
        if download_href is None:
            raise ValueError("Invalid value for `download_href`, must not be `None`")  # noqa: E501

        self._download_href = download_href

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
        if issubclass(SoftwareAttachmentResponse, dict):
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
        if not isinstance(other, SoftwareAttachmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

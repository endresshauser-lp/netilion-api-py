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

class APISubscriptionBase(object):
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
        'display_name': 'str',
        'description': 'str',
        'external_reference': 'str',
        'status': 'str',
        'notification_status': 'str',
        'subscription_type': 'str',
        'customer_purchase_order': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'billed_until': 'str',
        'external_user_reference': 'str',
        'external_plan_variant_reference': 'str',
        'api_call_quota': 'int',
        'storage_quota': 'int',
        'number_assigned_assets': 'int',
        'connected_assets_used': 'int',
        'upload_download_quota': 'int',
        'connected_asset_quota': 'int',
        'api_calls_used': 'int',
        'storage_used': 'int',
        'upload_download_used': 'int'
    }

    attribute_map = {
        'display_name': 'display_name',
        'description': 'description',
        'external_reference': 'external_reference',
        'status': 'status',
        'notification_status': 'notification_status',
        'subscription_type': 'subscription_type',
        'customer_purchase_order': 'customer_purchase_order',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'billed_until': 'billed_until',
        'external_user_reference': 'external_user_reference',
        'external_plan_variant_reference': 'external_plan_variant_reference',
        'api_call_quota': 'api_call_quota',
        'storage_quota': 'storage_quota',
        'number_assigned_assets': 'number_assigned_assets',
        'connected_assets_used': 'connected_assets_used',
        'upload_download_quota': 'upload_download_quota',
        'connected_asset_quota': 'connected_asset_quota',
        'api_calls_used': 'api_calls_used',
        'storage_used': 'storage_used',
        'upload_download_used': 'upload_download_used'
    }

    discriminator_value_class_map = {
          'APISubscriptionResponse': 'APISubscriptionResponse',
'APISubscriptionRequest': 'APISubscriptionRequest'    }

    def __init__(self, display_name=None, description=None, external_reference=None, status=None, notification_status=None, subscription_type=None, customer_purchase_order=None, start_date=None, end_date=None, billed_until=None, external_user_reference=None, external_plan_variant_reference=None, api_call_quota=None, storage_quota=None, number_assigned_assets=None, connected_assets_used=None, upload_download_quota=None, connected_asset_quota=None, api_calls_used=None, storage_used=None, upload_download_used=None):  # noqa: E501
        """APISubscriptionBase - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._description = None
        self._external_reference = None
        self._status = None
        self._notification_status = None
        self._subscription_type = None
        self._customer_purchase_order = None
        self._start_date = None
        self._end_date = None
        self._billed_until = None
        self._external_user_reference = None
        self._external_plan_variant_reference = None
        self._api_call_quota = None
        self._storage_quota = None
        self._number_assigned_assets = None
        self._connected_assets_used = None
        self._upload_download_quota = None
        self._connected_asset_quota = None
        self._api_calls_used = None
        self._storage_used = None
        self._upload_download_used = None
        self.discriminator = 'apiSubscriptionBaseType'
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if external_reference is not None:
            self.external_reference = external_reference
        if status is not None:
            self.status = status
        if notification_status is not None:
            self.notification_status = notification_status
        if subscription_type is not None:
            self.subscription_type = subscription_type
        if customer_purchase_order is not None:
            self.customer_purchase_order = customer_purchase_order
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if billed_until is not None:
            self.billed_until = billed_until
        if external_user_reference is not None:
            self.external_user_reference = external_user_reference
        if external_plan_variant_reference is not None:
            self.external_plan_variant_reference = external_plan_variant_reference
        if api_call_quota is not None:
            self.api_call_quota = api_call_quota
        if storage_quota is not None:
            self.storage_quota = storage_quota
        if number_assigned_assets is not None:
            self.number_assigned_assets = number_assigned_assets
        if connected_assets_used is not None:
            self.connected_assets_used = connected_assets_used
        if upload_download_quota is not None:
            self.upload_download_quota = upload_download_quota
        if connected_asset_quota is not None:
            self.connected_asset_quota = connected_asset_quota
        if api_calls_used is not None:
            self.api_calls_used = api_calls_used
        if storage_used is not None:
            self.storage_used = storage_used
        if upload_download_used is not None:
            self.upload_download_used = upload_download_used

    @property
    def display_name(self):
        """Gets the display_name of this APISubscriptionBase.  # noqa: E501

        Name of the api subscription  # noqa: E501

        :return: The display_name of this APISubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this APISubscriptionBase.

        Name of the api subscription  # noqa: E501

        :param display_name: The display_name of this APISubscriptionBase.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this APISubscriptionBase.  # noqa: E501

        Description of the api subscription  # noqa: E501

        :return: The description of this APISubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this APISubscriptionBase.

        Description of the api subscription  # noqa: E501

        :param description: The description of this APISubscriptionBase.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def external_reference(self):
        """Gets the external_reference of this APISubscriptionBase.  # noqa: E501

        can be used to store id of external api subscription managment system  # noqa: E501

        :return: The external_reference of this APISubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this APISubscriptionBase.

        can be used to store id of external api subscription managment system  # noqa: E501

        :param external_reference: The external_reference of this APISubscriptionBase.  # noqa: E501
        :type: str
        """

        self._external_reference = external_reference

    @property
    def status(self):
        """Gets the status of this APISubscriptionBase.  # noqa: E501

        status of the api subscription, can be  open, payment_required, confirmed, cancelled, scheduled_update and non_renewing  # noqa: E501

        :return: The status of this APISubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this APISubscriptionBase.

        status of the api subscription, can be  open, payment_required, confirmed, cancelled, scheduled_update and non_renewing  # noqa: E501

        :param status: The status of this APISubscriptionBase.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def notification_status(self):
        """Gets the notification_status of this APISubscriptionBase.  # noqa: E501

        status of the mail notification for the api subscription, can be no_notification, first_notification, second_notification or alert_notification  # noqa: E501

        :return: The notification_status of this APISubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._notification_status

    @notification_status.setter
    def notification_status(self, notification_status):
        """Sets the notification_status of this APISubscriptionBase.

        status of the mail notification for the api subscription, can be no_notification, first_notification, second_notification or alert_notification  # noqa: E501

        :param notification_status: The notification_status of this APISubscriptionBase.  # noqa: E501
        :type: str
        """

        self._notification_status = notification_status

    @property
    def subscription_type(self):
        """Gets the subscription_type of this APISubscriptionBase.  # noqa: E501

        type of the api subscription, can be 's' or 'm'  # noqa: E501

        :return: The subscription_type of this APISubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type):
        """Sets the subscription_type of this APISubscriptionBase.

        type of the api subscription, can be 's' or 'm'  # noqa: E501

        :param subscription_type: The subscription_type of this APISubscriptionBase.  # noqa: E501
        :type: str
        """

        self._subscription_type = subscription_type

    @property
    def customer_purchase_order(self):
        """Gets the customer_purchase_order of this APISubscriptionBase.  # noqa: E501

        reference for customer system  # noqa: E501

        :return: The customer_purchase_order of this APISubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._customer_purchase_order

    @customer_purchase_order.setter
    def customer_purchase_order(self, customer_purchase_order):
        """Sets the customer_purchase_order of this APISubscriptionBase.

        reference for customer system  # noqa: E501

        :param customer_purchase_order: The customer_purchase_order of this APISubscriptionBase.  # noqa: E501
        :type: str
        """

        self._customer_purchase_order = customer_purchase_order

    @property
    def start_date(self):
        """Gets the start_date of this APISubscriptionBase.  # noqa: E501

        start date of the api subscription  # noqa: E501

        :return: The start_date of this APISubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this APISubscriptionBase.

        start date of the api subscription  # noqa: E501

        :param start_date: The start_date of this APISubscriptionBase.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this APISubscriptionBase.  # noqa: E501

        end date of the api subscription  # noqa: E501

        :return: The end_date of this APISubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this APISubscriptionBase.

        end date of the api subscription  # noqa: E501

        :param end_date: The end_date of this APISubscriptionBase.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def billed_until(self):
        """Gets the billed_until of this APISubscriptionBase.  # noqa: E501

        end date of the api subscription  # noqa: E501

        :return: The billed_until of this APISubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._billed_until

    @billed_until.setter
    def billed_until(self, billed_until):
        """Sets the billed_until of this APISubscriptionBase.

        end date of the api subscription  # noqa: E501

        :param billed_until: The billed_until of this APISubscriptionBase.  # noqa: E501
        :type: str
        """

        self._billed_until = billed_until

    @property
    def external_user_reference(self):
        """Gets the external_user_reference of this APISubscriptionBase.  # noqa: E501

        can be used to store user id of external api subscription managment system  # noqa: E501

        :return: The external_user_reference of this APISubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._external_user_reference

    @external_user_reference.setter
    def external_user_reference(self, external_user_reference):
        """Sets the external_user_reference of this APISubscriptionBase.

        can be used to store user id of external api subscription managment system  # noqa: E501

        :param external_user_reference: The external_user_reference of this APISubscriptionBase.  # noqa: E501
        :type: str
        """

        self._external_user_reference = external_user_reference

    @property
    def external_plan_variant_reference(self):
        """Gets the external_plan_variant_reference of this APISubscriptionBase.  # noqa: E501

        can be used to store paln variant of external api subscription managment system  # noqa: E501

        :return: The external_plan_variant_reference of this APISubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._external_plan_variant_reference

    @external_plan_variant_reference.setter
    def external_plan_variant_reference(self, external_plan_variant_reference):
        """Sets the external_plan_variant_reference of this APISubscriptionBase.

        can be used to store paln variant of external api subscription managment system  # noqa: E501

        :param external_plan_variant_reference: The external_plan_variant_reference of this APISubscriptionBase.  # noqa: E501
        :type: str
        """

        self._external_plan_variant_reference = external_plan_variant_reference

    @property
    def api_call_quota(self):
        """Gets the api_call_quota of this APISubscriptionBase.  # noqa: E501

        number of bought api calls  # noqa: E501

        :return: The api_call_quota of this APISubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._api_call_quota

    @api_call_quota.setter
    def api_call_quota(self, api_call_quota):
        """Sets the api_call_quota of this APISubscriptionBase.

        number of bought api calls  # noqa: E501

        :param api_call_quota: The api_call_quota of this APISubscriptionBase.  # noqa: E501
        :type: int
        """

        self._api_call_quota = api_call_quota

    @property
    def storage_quota(self):
        """Gets the storage_quota of this APISubscriptionBase.  # noqa: E501

        number of bought storage (in bytes)  # noqa: E501

        :return: The storage_quota of this APISubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._storage_quota

    @storage_quota.setter
    def storage_quota(self, storage_quota):
        """Sets the storage_quota of this APISubscriptionBase.

        number of bought storage (in bytes)  # noqa: E501

        :param storage_quota: The storage_quota of this APISubscriptionBase.  # noqa: E501
        :type: int
        """

        self._storage_quota = storage_quota

    @property
    def number_assigned_assets(self):
        """Gets the number_assigned_assets of this APISubscriptionBase.  # noqa: E501

        number of assigned assets  # noqa: E501

        :return: The number_assigned_assets of this APISubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._number_assigned_assets

    @number_assigned_assets.setter
    def number_assigned_assets(self, number_assigned_assets):
        """Sets the number_assigned_assets of this APISubscriptionBase.

        number of assigned assets  # noqa: E501

        :param number_assigned_assets: The number_assigned_assets of this APISubscriptionBase.  # noqa: E501
        :type: int
        """

        self._number_assigned_assets = number_assigned_assets

    @property
    def connected_assets_used(self):
        """Gets the connected_assets_used of this APISubscriptionBase.  # noqa: E501

        number of connected assets used  # noqa: E501

        :return: The connected_assets_used of this APISubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._connected_assets_used

    @connected_assets_used.setter
    def connected_assets_used(self, connected_assets_used):
        """Sets the connected_assets_used of this APISubscriptionBase.

        number of connected assets used  # noqa: E501

        :param connected_assets_used: The connected_assets_used of this APISubscriptionBase.  # noqa: E501
        :type: int
        """

        self._connected_assets_used = connected_assets_used

    @property
    def upload_download_quota(self):
        """Gets the upload_download_quota of this APISubscriptionBase.  # noqa: E501

        traffic for up- and download of data (in bytes)  # noqa: E501

        :return: The upload_download_quota of this APISubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._upload_download_quota

    @upload_download_quota.setter
    def upload_download_quota(self, upload_download_quota):
        """Sets the upload_download_quota of this APISubscriptionBase.

        traffic for up- and download of data (in bytes)  # noqa: E501

        :param upload_download_quota: The upload_download_quota of this APISubscriptionBase.  # noqa: E501
        :type: int
        """

        self._upload_download_quota = upload_download_quota

    @property
    def connected_asset_quota(self):
        """Gets the connected_asset_quota of this APISubscriptionBase.  # noqa: E501

        number of bought connected asset addons  # noqa: E501

        :return: The connected_asset_quota of this APISubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._connected_asset_quota

    @connected_asset_quota.setter
    def connected_asset_quota(self, connected_asset_quota):
        """Sets the connected_asset_quota of this APISubscriptionBase.

        number of bought connected asset addons  # noqa: E501

        :param connected_asset_quota: The connected_asset_quota of this APISubscriptionBase.  # noqa: E501
        :type: int
        """

        self._connected_asset_quota = connected_asset_quota

    @property
    def api_calls_used(self):
        """Gets the api_calls_used of this APISubscriptionBase.  # noqa: E501

        number of api calls used  # noqa: E501

        :return: The api_calls_used of this APISubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._api_calls_used

    @api_calls_used.setter
    def api_calls_used(self, api_calls_used):
        """Sets the api_calls_used of this APISubscriptionBase.

        number of api calls used  # noqa: E501

        :param api_calls_used: The api_calls_used of this APISubscriptionBase.  # noqa: E501
        :type: int
        """

        self._api_calls_used = api_calls_used

    @property
    def storage_used(self):
        """Gets the storage_used of this APISubscriptionBase.  # noqa: E501

        number of storage used (in bytes)  # noqa: E501

        :return: The storage_used of this APISubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._storage_used

    @storage_used.setter
    def storage_used(self, storage_used):
        """Sets the storage_used of this APISubscriptionBase.

        number of storage used (in bytes)  # noqa: E501

        :param storage_used: The storage_used of this APISubscriptionBase.  # noqa: E501
        :type: int
        """

        self._storage_used = storage_used

    @property
    def upload_download_used(self):
        """Gets the upload_download_used of this APISubscriptionBase.  # noqa: E501

        data up- and download used (in bytes)  # noqa: E501

        :return: The upload_download_used of this APISubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._upload_download_used

    @upload_download_used.setter
    def upload_download_used(self, upload_download_used):
        """Sets the upload_download_used of this APISubscriptionBase.

        data up- and download used (in bytes)  # noqa: E501

        :param upload_download_used: The upload_download_used of this APISubscriptionBase.  # noqa: E501
        :type: int
        """

        self._upload_download_used = upload_download_used

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(APISubscriptionBase, dict):
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
        if not isinstance(other, APISubscriptionBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

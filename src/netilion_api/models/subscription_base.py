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

class SubscriptionBase(object):
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
        'asset_notification_status': 'str',
        'file_storage_notification_status': 'str',
        'data_storage_notification_status': 'str',
        'data_storage_notification_status_updated_at': 'str',
        'file_storage_notification_status_updated_at': 'str',
        'customer_purchase_order': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'billed_until': 'str',
        'trial_end_date': 'str',
        'cancelled_at': 'str',
        'external_user_reference': 'str',
        'external_plan_variant_reference': 'str',
        'number_assigned_assets': 'int',
        'asset_quota': 'int',
        'storage_quota': 'int',
        'data_storage_quota': 'int',
        'seat_quota': 'int',
        'force_mfa': 'bool',
        'reseller_label': 'str'
    }

    attribute_map = {
        'display_name': 'display_name',
        'description': 'description',
        'external_reference': 'external_reference',
        'status': 'status',
        'notification_status': 'notification_status',
        'asset_notification_status': 'asset_notification_status',
        'file_storage_notification_status': 'file_storage_notification_status',
        'data_storage_notification_status': 'data_storage_notification_status',
        'data_storage_notification_status_updated_at': 'data_storage_notification_status_updated_at',
        'file_storage_notification_status_updated_at': 'file_storage_notification_status_updated_at',
        'customer_purchase_order': 'customer_purchase_order',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'billed_until': 'billed_until',
        'trial_end_date': 'trial_end_date',
        'cancelled_at': 'cancelled_at',
        'external_user_reference': 'external_user_reference',
        'external_plan_variant_reference': 'external_plan_variant_reference',
        'number_assigned_assets': 'number_assigned_assets',
        'asset_quota': 'asset_quota',
        'storage_quota': 'storage_quota',
        'data_storage_quota': 'data_storage_quota',
        'seat_quota': 'seat_quota',
        'force_mfa': 'force_mfa',
        'reseller_label': 'reseller_label'
    }

    discriminator_value_class_map = {
          'SubscriptionResponse': 'SubscriptionResponse',
'SubscriptionRequest': 'SubscriptionRequest'    }

    def __init__(self, display_name=None, description=None, external_reference=None, status=None, notification_status=None, asset_notification_status=None, file_storage_notification_status=None, data_storage_notification_status=None, data_storage_notification_status_updated_at=None, file_storage_notification_status_updated_at=None, customer_purchase_order=None, start_date=None, end_date=None, billed_until=None, trial_end_date=None, cancelled_at=None, external_user_reference=None, external_plan_variant_reference=None, number_assigned_assets=None, asset_quota=None, storage_quota=None, data_storage_quota=None, seat_quota=None, force_mfa=None, reseller_label=None):  # noqa: E501
        """SubscriptionBase - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._description = None
        self._external_reference = None
        self._status = None
        self._notification_status = None
        self._asset_notification_status = None
        self._file_storage_notification_status = None
        self._data_storage_notification_status = None
        self._data_storage_notification_status_updated_at = None
        self._file_storage_notification_status_updated_at = None
        self._customer_purchase_order = None
        self._start_date = None
        self._end_date = None
        self._billed_until = None
        self._trial_end_date = None
        self._cancelled_at = None
        self._external_user_reference = None
        self._external_plan_variant_reference = None
        self._number_assigned_assets = None
        self._asset_quota = None
        self._storage_quota = None
        self._data_storage_quota = None
        self._seat_quota = None
        self._force_mfa = None
        self._reseller_label = None
        self.discriminator = 'subscriptionBaseType'
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
        if asset_notification_status is not None:
            self.asset_notification_status = asset_notification_status
        if file_storage_notification_status is not None:
            self.file_storage_notification_status = file_storage_notification_status
        if data_storage_notification_status is not None:
            self.data_storage_notification_status = data_storage_notification_status
        if data_storage_notification_status_updated_at is not None:
            self.data_storage_notification_status_updated_at = data_storage_notification_status_updated_at
        if file_storage_notification_status_updated_at is not None:
            self.file_storage_notification_status_updated_at = file_storage_notification_status_updated_at
        if customer_purchase_order is not None:
            self.customer_purchase_order = customer_purchase_order
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if billed_until is not None:
            self.billed_until = billed_until
        if trial_end_date is not None:
            self.trial_end_date = trial_end_date
        if cancelled_at is not None:
            self.cancelled_at = cancelled_at
        if external_user_reference is not None:
            self.external_user_reference = external_user_reference
        if external_plan_variant_reference is not None:
            self.external_plan_variant_reference = external_plan_variant_reference
        if number_assigned_assets is not None:
            self.number_assigned_assets = number_assigned_assets
        if asset_quota is not None:
            self.asset_quota = asset_quota
        if storage_quota is not None:
            self.storage_quota = storage_quota
        if data_storage_quota is not None:
            self.data_storage_quota = data_storage_quota
        if seat_quota is not None:
            self.seat_quota = seat_quota
        if force_mfa is not None:
            self.force_mfa = force_mfa
        if reseller_label is not None:
            self.reseller_label = reseller_label

    @property
    def display_name(self):
        """Gets the display_name of this SubscriptionBase.  # noqa: E501

        Name of the subscription  # noqa: E501

        :return: The display_name of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this SubscriptionBase.

        Name of the subscription  # noqa: E501

        :param display_name: The display_name of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this SubscriptionBase.  # noqa: E501

        Description of the subscription  # noqa: E501

        :return: The description of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubscriptionBase.

        Description of the subscription  # noqa: E501

        :param description: The description of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def external_reference(self):
        """Gets the external_reference of this SubscriptionBase.  # noqa: E501

        can be used to store id of external subscription management system  # noqa: E501

        :return: The external_reference of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this SubscriptionBase.

        can be used to store id of external subscription management system  # noqa: E501

        :param external_reference: The external_reference of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._external_reference = external_reference

    @property
    def status(self):
        """Gets the status of this SubscriptionBase.  # noqa: E501

        status of the subscription, can be  open, payment_required, confirmed, cancelled, scheduled_update and non_renewing  # noqa: E501

        :return: The status of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubscriptionBase.

        status of the subscription, can be  open, payment_required, confirmed, cancelled, scheduled_update and non_renewing  # noqa: E501

        :param status: The status of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def notification_status(self):
        """Gets the notification_status of this SubscriptionBase.  # noqa: E501

        status of the mail notification for the subscription, can be no_notification, first_notification, second_notification or alert_notification  # noqa: E501

        :return: The notification_status of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._notification_status

    @notification_status.setter
    def notification_status(self, notification_status):
        """Sets the notification_status of this SubscriptionBase.

        status of the mail notification for the subscription, can be no_notification, first_notification, second_notification or alert_notification  # noqa: E501

        :param notification_status: The notification_status of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._notification_status = notification_status

    @property
    def asset_notification_status(self):
        """Gets the asset_notification_status of this SubscriptionBase.  # noqa: E501

        specific status of the mail notification for the asset limitation in the subscription, can be no_notification, first_notification, second_notification or alert_notification  # noqa: E501

        :return: The asset_notification_status of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._asset_notification_status

    @asset_notification_status.setter
    def asset_notification_status(self, asset_notification_status):
        """Sets the asset_notification_status of this SubscriptionBase.

        specific status of the mail notification for the asset limitation in the subscription, can be no_notification, first_notification, second_notification or alert_notification  # noqa: E501

        :param asset_notification_status: The asset_notification_status of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._asset_notification_status = asset_notification_status

    @property
    def file_storage_notification_status(self):
        """Gets the file_storage_notification_status of this SubscriptionBase.  # noqa: E501

        specific status of the mail notification for the file storage limitation in the subscription, can be no_notification, first_notification, second_notification or alert_notification  # noqa: E501

        :return: The file_storage_notification_status of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._file_storage_notification_status

    @file_storage_notification_status.setter
    def file_storage_notification_status(self, file_storage_notification_status):
        """Sets the file_storage_notification_status of this SubscriptionBase.

        specific status of the mail notification for the file storage limitation in the subscription, can be no_notification, first_notification, second_notification or alert_notification  # noqa: E501

        :param file_storage_notification_status: The file_storage_notification_status of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._file_storage_notification_status = file_storage_notification_status

    @property
    def data_storage_notification_status(self):
        """Gets the data_storage_notification_status of this SubscriptionBase.  # noqa: E501

        status of the mail notification for the data storage limitation in the subscription, can be no_notification, first_notification, second_notification or alert_notification  # noqa: E501

        :return: The data_storage_notification_status of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._data_storage_notification_status

    @data_storage_notification_status.setter
    def data_storage_notification_status(self, data_storage_notification_status):
        """Sets the data_storage_notification_status of this SubscriptionBase.

        status of the mail notification for the data storage limitation in the subscription, can be no_notification, first_notification, second_notification or alert_notification  # noqa: E501

        :param data_storage_notification_status: The data_storage_notification_status of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._data_storage_notification_status = data_storage_notification_status

    @property
    def data_storage_notification_status_updated_at(self):
        """Gets the data_storage_notification_status_updated_at of this SubscriptionBase.  # noqa: E501

        last date when data_storage_notification_status was changed  # noqa: E501

        :return: The data_storage_notification_status_updated_at of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._data_storage_notification_status_updated_at

    @data_storage_notification_status_updated_at.setter
    def data_storage_notification_status_updated_at(self, data_storage_notification_status_updated_at):
        """Sets the data_storage_notification_status_updated_at of this SubscriptionBase.

        last date when data_storage_notification_status was changed  # noqa: E501

        :param data_storage_notification_status_updated_at: The data_storage_notification_status_updated_at of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._data_storage_notification_status_updated_at = data_storage_notification_status_updated_at

    @property
    def file_storage_notification_status_updated_at(self):
        """Gets the file_storage_notification_status_updated_at of this SubscriptionBase.  # noqa: E501

        last date when file_storage_notification_status was changed  # noqa: E501

        :return: The file_storage_notification_status_updated_at of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._file_storage_notification_status_updated_at

    @file_storage_notification_status_updated_at.setter
    def file_storage_notification_status_updated_at(self, file_storage_notification_status_updated_at):
        """Sets the file_storage_notification_status_updated_at of this SubscriptionBase.

        last date when file_storage_notification_status was changed  # noqa: E501

        :param file_storage_notification_status_updated_at: The file_storage_notification_status_updated_at of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._file_storage_notification_status_updated_at = file_storage_notification_status_updated_at

    @property
    def customer_purchase_order(self):
        """Gets the customer_purchase_order of this SubscriptionBase.  # noqa: E501

        reference for customer system  # noqa: E501

        :return: The customer_purchase_order of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._customer_purchase_order

    @customer_purchase_order.setter
    def customer_purchase_order(self, customer_purchase_order):
        """Sets the customer_purchase_order of this SubscriptionBase.

        reference for customer system  # noqa: E501

        :param customer_purchase_order: The customer_purchase_order of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._customer_purchase_order = customer_purchase_order

    @property
    def start_date(self):
        """Gets the start_date of this SubscriptionBase.  # noqa: E501

        start date of the subscription  # noqa: E501

        :return: The start_date of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SubscriptionBase.

        start date of the subscription  # noqa: E501

        :param start_date: The start_date of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this SubscriptionBase.  # noqa: E501

        end date of the subscription  # noqa: E501

        :return: The end_date of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SubscriptionBase.

        end date of the subscription  # noqa: E501

        :param end_date: The end_date of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def billed_until(self):
        """Gets the billed_until of this SubscriptionBase.  # noqa: E501

        end date of the subscription  # noqa: E501

        :return: The billed_until of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._billed_until

    @billed_until.setter
    def billed_until(self, billed_until):
        """Sets the billed_until of this SubscriptionBase.

        end date of the subscription  # noqa: E501

        :param billed_until: The billed_until of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._billed_until = billed_until

    @property
    def trial_end_date(self):
        """Gets the trial_end_date of this SubscriptionBase.  # noqa: E501

        end date of the subscription's trial period  # noqa: E501

        :return: The trial_end_date of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._trial_end_date

    @trial_end_date.setter
    def trial_end_date(self, trial_end_date):
        """Sets the trial_end_date of this SubscriptionBase.

        end date of the subscription's trial period  # noqa: E501

        :param trial_end_date: The trial_end_date of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._trial_end_date = trial_end_date

    @property
    def cancelled_at(self):
        """Gets the cancelled_at of this SubscriptionBase.  # noqa: E501

        date when subscription was cancelled  # noqa: E501

        :return: The cancelled_at of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._cancelled_at

    @cancelled_at.setter
    def cancelled_at(self, cancelled_at):
        """Sets the cancelled_at of this SubscriptionBase.

        date when subscription was cancelled  # noqa: E501

        :param cancelled_at: The cancelled_at of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._cancelled_at = cancelled_at

    @property
    def external_user_reference(self):
        """Gets the external_user_reference of this SubscriptionBase.  # noqa: E501

        can be used to store user id of external subscription management system  # noqa: E501

        :return: The external_user_reference of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._external_user_reference

    @external_user_reference.setter
    def external_user_reference(self, external_user_reference):
        """Sets the external_user_reference of this SubscriptionBase.

        can be used to store user id of external subscription management system  # noqa: E501

        :param external_user_reference: The external_user_reference of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._external_user_reference = external_user_reference

    @property
    def external_plan_variant_reference(self):
        """Gets the external_plan_variant_reference of this SubscriptionBase.  # noqa: E501

        can be used to store plan variant of external subscription management system  # noqa: E501

        :return: The external_plan_variant_reference of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._external_plan_variant_reference

    @external_plan_variant_reference.setter
    def external_plan_variant_reference(self, external_plan_variant_reference):
        """Sets the external_plan_variant_reference of this SubscriptionBase.

        can be used to store plan variant of external subscription management system  # noqa: E501

        :param external_plan_variant_reference: The external_plan_variant_reference of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._external_plan_variant_reference = external_plan_variant_reference

    @property
    def number_assigned_assets(self):
        """Gets the number_assigned_assets of this SubscriptionBase.  # noqa: E501

        number of assigned assets  # noqa: E501

        :return: The number_assigned_assets of this SubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._number_assigned_assets

    @number_assigned_assets.setter
    def number_assigned_assets(self, number_assigned_assets):
        """Sets the number_assigned_assets of this SubscriptionBase.

        number of assigned assets  # noqa: E501

        :param number_assigned_assets: The number_assigned_assets of this SubscriptionBase.  # noqa: E501
        :type: int
        """

        self._number_assigned_assets = number_assigned_assets

    @property
    def asset_quota(self):
        """Gets the asset_quota of this SubscriptionBase.  # noqa: E501

        number of bought assets  # noqa: E501

        :return: The asset_quota of this SubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._asset_quota

    @asset_quota.setter
    def asset_quota(self, asset_quota):
        """Sets the asset_quota of this SubscriptionBase.

        number of bought assets  # noqa: E501

        :param asset_quota: The asset_quota of this SubscriptionBase.  # noqa: E501
        :type: int
        """

        self._asset_quota = asset_quota

    @property
    def storage_quota(self):
        """Gets the storage_quota of this SubscriptionBase.  # noqa: E501

        size of bought file storage (in bytes)  # noqa: E501

        :return: The storage_quota of this SubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._storage_quota

    @storage_quota.setter
    def storage_quota(self, storage_quota):
        """Sets the storage_quota of this SubscriptionBase.

        size of bought file storage (in bytes)  # noqa: E501

        :param storage_quota: The storage_quota of this SubscriptionBase.  # noqa: E501
        :type: int
        """

        self._storage_quota = storage_quota

    @property
    def data_storage_quota(self):
        """Gets the data_storage_quota of this SubscriptionBase.  # noqa: E501

        size of bought data storage (in bytes)  # noqa: E501

        :return: The data_storage_quota of this SubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._data_storage_quota

    @data_storage_quota.setter
    def data_storage_quota(self, data_storage_quota):
        """Sets the data_storage_quota of this SubscriptionBase.

        size of bought data storage (in bytes)  # noqa: E501

        :param data_storage_quota: The data_storage_quota of this SubscriptionBase.  # noqa: E501
        :type: int
        """

        self._data_storage_quota = data_storage_quota

    @property
    def seat_quota(self):
        """Gets the seat_quota of this SubscriptionBase.  # noqa: E501

        number of bought seats  # noqa: E501

        :return: The seat_quota of this SubscriptionBase.  # noqa: E501
        :rtype: int
        """
        return self._seat_quota

    @seat_quota.setter
    def seat_quota(self, seat_quota):
        """Sets the seat_quota of this SubscriptionBase.

        number of bought seats  # noqa: E501

        :param seat_quota: The seat_quota of this SubscriptionBase.  # noqa: E501
        :type: int
        """

        self._seat_quota = seat_quota

    @property
    def force_mfa(self):
        """Gets the force_mfa of this SubscriptionBase.  # noqa: E501

        will force MFA for the users using this subscription including owner and seat users  # noqa: E501

        :return: The force_mfa of this SubscriptionBase.  # noqa: E501
        :rtype: bool
        """
        return self._force_mfa

    @force_mfa.setter
    def force_mfa(self, force_mfa):
        """Sets the force_mfa of this SubscriptionBase.

        will force MFA for the users using this subscription including owner and seat users  # noqa: E501

        :param force_mfa: The force_mfa of this SubscriptionBase.  # noqa: E501
        :type: bool
        """

        self._force_mfa = force_mfa

    @property
    def reseller_label(self):
        """Gets the reseller_label of this SubscriptionBase.  # noqa: E501

        Custom label given to the subscription by the reseller user  # noqa: E501

        :return: The reseller_label of this SubscriptionBase.  # noqa: E501
        :rtype: str
        """
        return self._reseller_label

    @reseller_label.setter
    def reseller_label(self, reseller_label):
        """Sets the reseller_label of this SubscriptionBase.

        Custom label given to the subscription by the reseller user  # noqa: E501

        :param reseller_label: The reseller_label of this SubscriptionBase.  # noqa: E501
        :type: str
        """

        self._reseller_label = reseller_label

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
        if issubclass(SubscriptionBase, dict):
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
        if not isinstance(other, SubscriptionBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    Netilion API Documentation

    Welcome to the Netilion API Documentation, which provides interactive access and documentation to our REST API. Please visit our developer portal for further instructions and information: https://developer.netilion.endress.com/   # noqa: E501

    OpenAPI spec version: 01.00.00
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from netilion_api.api_client import ApiClient


class LookupApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def eh_extended_order_code_lookup(self, order_code, **kwargs):  # noqa: E501
        """lookup for the extended order code for Endress+Hauser products  # noqa: E501

        Returns an extended order code for Endress+Hauser products when the given order code is existing  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.eh_extended_order_code_lookup(order_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_code: any Endress+Hauser order code (required)
        :return: ExtendedOrderCode
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.eh_extended_order_code_lookup_with_http_info(order_code, **kwargs)  # noqa: E501
        else:
            (data) = self.eh_extended_order_code_lookup_with_http_info(order_code, **kwargs)  # noqa: E501
            return data

    def eh_extended_order_code_lookup_with_http_info(self, order_code, **kwargs):  # noqa: E501
        """lookup for the extended order code for Endress+Hauser products  # noqa: E501

        Returns an extended order code for Endress+Hauser products when the given order code is existing  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.eh_extended_order_code_lookup_with_http_info(order_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_code: any Endress+Hauser order code (required)
        :return: ExtendedOrderCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method eh_extended_order_code_lookup" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_code' is set
        if ('order_code' not in params or
                params['order_code'] is None):
            raise ValueError("Missing the required parameter `order_code` when calling `eh_extended_order_code_lookup`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_code' in params:
            query_params.append(('order_code', params['order_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key', 'Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/endress/extended_order_code_lookup', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExtendedOrderCode',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def eh_product_lookup(self, serial_number, **kwargs):  # noqa: E501
        """lookup for Endress+Hauser products with asset specific search criteria  # noqa: E501

        Returns an Endress+Hauser product, matching the serial number. The serial number is at least 4 characters long and may include letters, numbers, dashes (-), underscores (_) and backslashes (\\\\).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.eh_product_lookup(serial_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str serial_number: Any Endress+Hauser serial number (required)
        :return: ProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.eh_product_lookup_with_http_info(serial_number, **kwargs)  # noqa: E501
        else:
            (data) = self.eh_product_lookup_with_http_info(serial_number, **kwargs)  # noqa: E501
            return data

    def eh_product_lookup_with_http_info(self, serial_number, **kwargs):  # noqa: E501
        """lookup for Endress+Hauser products with asset specific search criteria  # noqa: E501

        Returns an Endress+Hauser product, matching the serial number. The serial number is at least 4 characters long and may include letters, numbers, dashes (-), underscores (_) and backslashes (\\\\).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.eh_product_lookup_with_http_info(serial_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str serial_number: Any Endress+Hauser serial number (required)
        :return: ProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['serial_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method eh_product_lookup" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'serial_number' is set
        if ('serial_number' not in params or
                params['serial_number'] is None):
            raise ValueError("Missing the required parameter `serial_number` when calling `eh_product_lookup`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'serial_number' in params:
            query_params.append(('serial_number', params['serial_number']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key', 'Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/endress/product_lookup', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProductResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def eh_successor_lookup(self, **kwargs):  # noqa: E501
        """lookup for Endress+Hauser successor products  # noqa: E501

        Returns successor information, if a serial_number or order code was provided, the order code transformer is used, for product_code the successor comes from the Product Status List r Possible include values: ```product, product.pictures,product.status, product.parent``` The serial number is at least 4 characters long and may include letters, numbers, dashes (-), underscores (_) and backslashes (\\\\).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.eh_successor_lookup(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str include: Comma separated list of objects to include in response
        :param str serial_number: Any Endress+Hauser serial number
        :param str order_code: an Endress+Hauser order code
        :param str product_code: an Endress+Hauser product_code
        :return: SuccessorsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.eh_successor_lookup_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.eh_successor_lookup_with_http_info(**kwargs)  # noqa: E501
            return data

    def eh_successor_lookup_with_http_info(self, **kwargs):  # noqa: E501
        """lookup for Endress+Hauser successor products  # noqa: E501

        Returns successor information, if a serial_number or order code was provided, the order code transformer is used, for product_code the successor comes from the Product Status List r Possible include values: ```product, product.pictures,product.status, product.parent``` The serial number is at least 4 characters long and may include letters, numbers, dashes (-), underscores (_) and backslashes (\\\\).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.eh_successor_lookup_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str include: Comma separated list of objects to include in response
        :param str serial_number: Any Endress+Hauser serial number
        :param str order_code: an Endress+Hauser order code
        :param str product_code: an Endress+Hauser product_code
        :return: SuccessorsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include', 'serial_number', 'order_code', 'product_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method eh_successor_lookup" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
        if 'serial_number' in params:
            query_params.append(('serial_number', params['serial_number']))  # noqa: E501
        if 'order_code' in params:
            query_params.append(('order_code', params['order_code']))  # noqa: E501
        if 'product_code' in params:
            query_params.append(('product_code', params['product_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key', 'Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/endress/successor_lookup', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessorsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

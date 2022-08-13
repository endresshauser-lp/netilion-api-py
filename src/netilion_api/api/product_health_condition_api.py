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


class ProductHealthConditionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_health_conditions_to_product(self, body, product_id, **kwargs):  # noqa: E501
        """Add health conditions to an product  # noqa: E501

        Add one or more health conditions to an product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_health_conditions_to_product(body, product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HealthConditionsRequest body: Resources that shall be added. (required)
        :param int product_id: The resource defined in the URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_health_conditions_to_product_with_http_info(body, product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_health_conditions_to_product_with_http_info(body, product_id, **kwargs)  # noqa: E501
            return data

    def add_health_conditions_to_product_with_http_info(self, body, product_id, **kwargs):  # noqa: E501
        """Add health conditions to an product  # noqa: E501

        Add one or more health conditions to an product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_health_conditions_to_product_with_http_info(body, product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HealthConditionsRequest body: Resources that shall be added. (required)
        :param int product_id: The resource defined in the URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'product_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_health_conditions_to_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_health_conditions_to_product`")  # noqa: E501
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `add_health_conditions_to_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key', 'Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/products/{product_id}/health_conditions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_product_health_conditions(self, product_id, **kwargs):  # noqa: E501
        """Get all health conditions assigned to an product  # noqa: E501

        Returns a list of health conditions of an product.  Possible include value: ``asset_status, causes, causes.remedies``  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_health_conditions(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int product_id: The resource defined in the URL (required)
        :param int page: Page number to load
        :param int per_page: Number of items to load per page
        :param str include: Comma separated list of objects to include in response
        :param str health_condition_id: One or multiple ids (comma list). Expected id format is integer
        :param str diagnosis_code: Filter accepts `*` as wildcard
        :param str device_ident: Filter accepts `*` as wildcard
        :param str product_identifier: Filter accepts * as wildcard
        :param str protocol: Filter accepts `PROFIBUS`, `HART`, `ETHERNETIP` and `MODBUS`
        :param str order_by: Order result by attribute value, accepts `id`, `diagnosis_code`, `device_ident`, `product_identifier`, `created_at` or `updated_at`, add `-` as a prefix for descending order. Default value is `id`
        :param str accept_language: The client's accepted languages. One or several (e.g. fr,de,en)
        :return: HealthConditionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_product_health_conditions_with_http_info(product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_product_health_conditions_with_http_info(product_id, **kwargs)  # noqa: E501
            return data

    def get_product_health_conditions_with_http_info(self, product_id, **kwargs):  # noqa: E501
        """Get all health conditions assigned to an product  # noqa: E501

        Returns a list of health conditions of an product.  Possible include value: ``asset_status, causes, causes.remedies``  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_product_health_conditions_with_http_info(product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int product_id: The resource defined in the URL (required)
        :param int page: Page number to load
        :param int per_page: Number of items to load per page
        :param str include: Comma separated list of objects to include in response
        :param str health_condition_id: One or multiple ids (comma list). Expected id format is integer
        :param str diagnosis_code: Filter accepts `*` as wildcard
        :param str device_ident: Filter accepts `*` as wildcard
        :param str product_identifier: Filter accepts * as wildcard
        :param str protocol: Filter accepts `PROFIBUS`, `HART`, `ETHERNETIP` and `MODBUS`
        :param str order_by: Order result by attribute value, accepts `id`, `diagnosis_code`, `device_ident`, `product_identifier`, `created_at` or `updated_at`, add `-` as a prefix for descending order. Default value is `id`
        :param str accept_language: The client's accepted languages. One or several (e.g. fr,de,en)
        :return: HealthConditionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'page', 'per_page', 'include', 'health_condition_id', 'diagnosis_code', 'device_ident', 'product_identifier', 'protocol', 'order_by', 'accept_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_health_conditions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_product_health_conditions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
        if 'health_condition_id' in params:
            query_params.append(('health_condition_id', params['health_condition_id']))  # noqa: E501
        if 'diagnosis_code' in params:
            query_params.append(('diagnosis_code', params['diagnosis_code']))  # noqa: E501
        if 'device_ident' in params:
            query_params.append(('device_ident', params['device_ident']))  # noqa: E501
        if 'product_identifier' in params:
            query_params.append(('product_identifier', params['product_identifier']))  # noqa: E501
        if 'protocol' in params:
            query_params.append(('protocol', params['protocol']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key', 'Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/products/{product_id}/health_conditions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HealthConditionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reaplace_health_conditions_of_product(self, body, product_id, **kwargs):  # noqa: E501
        """Replace health conditions of an product  # noqa: E501

        Replaces all health conditions belonging to an product. You can send a list of resources that will replace all previous values.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reaplace_health_conditions_of_product(body, product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HealthConditionsRequest body: Resources that shall be replaced. (required)
        :param int product_id: The resource defined in the URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reaplace_health_conditions_of_product_with_http_info(body, product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.reaplace_health_conditions_of_product_with_http_info(body, product_id, **kwargs)  # noqa: E501
            return data

    def reaplace_health_conditions_of_product_with_http_info(self, body, product_id, **kwargs):  # noqa: E501
        """Replace health conditions of an product  # noqa: E501

        Replaces all health conditions belonging to an product. You can send a list of resources that will replace all previous values.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reaplace_health_conditions_of_product_with_http_info(body, product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HealthConditionsRequest body: Resources that shall be replaced. (required)
        :param int product_id: The resource defined in the URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'product_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reaplace_health_conditions_of_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `reaplace_health_conditions_of_product`")  # noqa: E501
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `reaplace_health_conditions_of_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key', 'Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/products/{product_id}/health_conditions', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_health_conditions_of_product(self, body, product_id, **kwargs):  # noqa: E501
        """Remove health conditions of an product  # noqa: E501

        Remove one or more health conditions from an product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_health_conditions_of_product(body, product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HealthConditionCauseIDs body: Resources that shall be removed. (required)
        :param int product_id: The resource defined in the URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_health_conditions_of_product_with_http_info(body, product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_health_conditions_of_product_with_http_info(body, product_id, **kwargs)  # noqa: E501
            return data

    def remove_health_conditions_of_product_with_http_info(self, body, product_id, **kwargs):  # noqa: E501
        """Remove health conditions of an product  # noqa: E501

        Remove one or more health conditions from an product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_health_conditions_of_product_with_http_info(body, product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HealthConditionCauseIDs body: Resources that shall be removed. (required)
        :param int product_id: The resource defined in the URL (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'product_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_health_conditions_of_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `remove_health_conditions_of_product`")  # noqa: E501
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `remove_health_conditions_of_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key', 'Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/products/{product_id}/health_conditions', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
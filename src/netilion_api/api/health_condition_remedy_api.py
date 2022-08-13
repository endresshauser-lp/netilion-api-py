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


class HealthConditionRemedyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_health_condition_remedy(self, body, health_condition_id, cause_id, **kwargs):  # noqa: E501
        """Create a remedy  # noqa: E501

        Remedy must have a code and a description scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_health_condition_remedy(body, health_condition_id, cause_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HealthConditionRemedyRequest body: Parameters that shall be updated (required)
        :param int health_condition_id: The resource defined in the URL (required)
        :param int cause_id: The resource defined in the URL (required)
        :return: HealthConditionRemedyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_health_condition_remedy_with_http_info(body, health_condition_id, cause_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_health_condition_remedy_with_http_info(body, health_condition_id, cause_id, **kwargs)  # noqa: E501
            return data

    def create_health_condition_remedy_with_http_info(self, body, health_condition_id, cause_id, **kwargs):  # noqa: E501
        """Create a remedy  # noqa: E501

        Remedy must have a code and a description scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_health_condition_remedy_with_http_info(body, health_condition_id, cause_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HealthConditionRemedyRequest body: Parameters that shall be updated (required)
        :param int health_condition_id: The resource defined in the URL (required)
        :param int cause_id: The resource defined in the URL (required)
        :return: HealthConditionRemedyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'health_condition_id', 'cause_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_health_condition_remedy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_health_condition_remedy`")  # noqa: E501
        # verify the required parameter 'health_condition_id' is set
        if ('health_condition_id' not in params or
                params['health_condition_id'] is None):
            raise ValueError("Missing the required parameter `health_condition_id` when calling `create_health_condition_remedy`")  # noqa: E501
        # verify the required parameter 'cause_id' is set
        if ('cause_id' not in params or
                params['cause_id'] is None):
            raise ValueError("Missing the required parameter `cause_id` when calling `create_health_condition_remedy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'health_condition_id' in params:
            path_params['health_condition_id'] = params['health_condition_id']  # noqa: E501
        if 'cause_id' in params:
            path_params['cause_id'] = params['cause_id']  # noqa: E501

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
            '/health_conditions/{health_condition_id}/causes/{cause_id}/remedies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HealthConditionRemedyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_health_condition_remedy(self, health_condition_id, cause_id, id, **kwargs):  # noqa: E501
        """Delete a remedy  # noqa: E501

        Delete a specific resource identified by the id in the URL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_health_condition_remedy(health_condition_id, cause_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int health_condition_id: The resource defined in the URL (required)
        :param int cause_id: The resource defined in the URL (required)
        :param int id: Id of the remedy to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_health_condition_remedy_with_http_info(health_condition_id, cause_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_health_condition_remedy_with_http_info(health_condition_id, cause_id, id, **kwargs)  # noqa: E501
            return data

    def delete_health_condition_remedy_with_http_info(self, health_condition_id, cause_id, id, **kwargs):  # noqa: E501
        """Delete a remedy  # noqa: E501

        Delete a specific resource identified by the id in the URL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_health_condition_remedy_with_http_info(health_condition_id, cause_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int health_condition_id: The resource defined in the URL (required)
        :param int cause_id: The resource defined in the URL (required)
        :param int id: Id of the remedy to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['health_condition_id', 'cause_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_health_condition_remedy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'health_condition_id' is set
        if ('health_condition_id' not in params or
                params['health_condition_id'] is None):
            raise ValueError("Missing the required parameter `health_condition_id` when calling `delete_health_condition_remedy`")  # noqa: E501
        # verify the required parameter 'cause_id' is set
        if ('cause_id' not in params or
                params['cause_id'] is None):
            raise ValueError("Missing the required parameter `cause_id` when calling `delete_health_condition_remedy`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_health_condition_remedy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'health_condition_id' in params:
            path_params['health_condition_id'] = params['health_condition_id']  # noqa: E501
        if 'cause_id' in params:
            path_params['cause_id'] = params['cause_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/health_conditions/{health_condition_id}/causes/{cause_id}/remedies/{id}', 'DELETE',
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

    def get_health_condition_remedies(self, health_condition_id, cause_id, **kwargs):  # noqa: E501
        """Get all remedies of a cause  # noqa: E501

        Returns a list of remedies for a specific cause. You can apply query parameters in the request to get a filtered list. If the query has no matches, the response will show an empty array.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_health_condition_remedies(health_condition_id, cause_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int health_condition_id: The resource defined in the URL (required)
        :param int cause_id: The resource defined in the URL (required)
        :param int page: Page number to load
        :param int per_page: Number of items to load per page
        :param str code: Filter accepts `*` as wildcard
        :param str description: Filter accepts `*` as wildcard
        :param str order_by: Order result by attribute value, accepts `id`, `code`, `created_at` or `updated_at`, add `-` as a prefix for descending order. Default value is `id`
        :param str accept_language: The client's accepted languages. One or several (e.g. fr,de,en)
        :return: Remedies
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_health_condition_remedies_with_http_info(health_condition_id, cause_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_health_condition_remedies_with_http_info(health_condition_id, cause_id, **kwargs)  # noqa: E501
            return data

    def get_health_condition_remedies_with_http_info(self, health_condition_id, cause_id, **kwargs):  # noqa: E501
        """Get all remedies of a cause  # noqa: E501

        Returns a list of remedies for a specific cause. You can apply query parameters in the request to get a filtered list. If the query has no matches, the response will show an empty array.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_health_condition_remedies_with_http_info(health_condition_id, cause_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int health_condition_id: The resource defined in the URL (required)
        :param int cause_id: The resource defined in the URL (required)
        :param int page: Page number to load
        :param int per_page: Number of items to load per page
        :param str code: Filter accepts `*` as wildcard
        :param str description: Filter accepts `*` as wildcard
        :param str order_by: Order result by attribute value, accepts `id`, `code`, `created_at` or `updated_at`, add `-` as a prefix for descending order. Default value is `id`
        :param str accept_language: The client's accepted languages. One or several (e.g. fr,de,en)
        :return: Remedies
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['health_condition_id', 'cause_id', 'page', 'per_page', 'code', 'description', 'order_by', 'accept_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_health_condition_remedies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'health_condition_id' is set
        if ('health_condition_id' not in params or
                params['health_condition_id'] is None):
            raise ValueError("Missing the required parameter `health_condition_id` when calling `get_health_condition_remedies`")  # noqa: E501
        # verify the required parameter 'cause_id' is set
        if ('cause_id' not in params or
                params['cause_id'] is None):
            raise ValueError("Missing the required parameter `cause_id` when calling `get_health_condition_remedies`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'health_condition_id' in params:
            path_params['health_condition_id'] = params['health_condition_id']  # noqa: E501
        if 'cause_id' in params:
            path_params['cause_id'] = params['cause_id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501
        if 'description' in params:
            query_params.append(('description', params['description']))  # noqa: E501
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
            '/health_conditions/{health_condition_id}/causes/{cause_id}/remedies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Remedies',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_health_condition_remedy_by_id(self, health_condition_id, cause_id, id, **kwargs):  # noqa: E501
        """Get a single remedy  # noqa: E501

        Get a specific remedy identified by the id in the URL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_health_condition_remedy_by_id(health_condition_id, cause_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int health_condition_id: The resource defined in the URL (required)
        :param int cause_id: The resource defined in the URL (required)
        :param int id: Id of the remedy to fetch (required)
        :param str accept_language: The client's accepted languages. One or several (e.g. fr,de,en)
        :return: HealthConditionRemedyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_health_condition_remedy_by_id_with_http_info(health_condition_id, cause_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_health_condition_remedy_by_id_with_http_info(health_condition_id, cause_id, id, **kwargs)  # noqa: E501
            return data

    def get_health_condition_remedy_by_id_with_http_info(self, health_condition_id, cause_id, id, **kwargs):  # noqa: E501
        """Get a single remedy  # noqa: E501

        Get a specific remedy identified by the id in the URL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_health_condition_remedy_by_id_with_http_info(health_condition_id, cause_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int health_condition_id: The resource defined in the URL (required)
        :param int cause_id: The resource defined in the URL (required)
        :param int id: Id of the remedy to fetch (required)
        :param str accept_language: The client's accepted languages. One or several (e.g. fr,de,en)
        :return: HealthConditionRemedyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['health_condition_id', 'cause_id', 'id', 'accept_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_health_condition_remedy_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'health_condition_id' is set
        if ('health_condition_id' not in params or
                params['health_condition_id'] is None):
            raise ValueError("Missing the required parameter `health_condition_id` when calling `get_health_condition_remedy_by_id`")  # noqa: E501
        # verify the required parameter 'cause_id' is set
        if ('cause_id' not in params or
                params['cause_id'] is None):
            raise ValueError("Missing the required parameter `cause_id` when calling `get_health_condition_remedy_by_id`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_health_condition_remedy_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'health_condition_id' in params:
            path_params['health_condition_id'] = params['health_condition_id']  # noqa: E501
        if 'cause_id' in params:
            path_params['cause_id'] = params['cause_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/health_conditions/{health_condition_id}/causes/{cause_id}/remedies/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HealthConditionRemedyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_health_condition_remedy(self, body, health_condition_id, cause_id, id, **kwargs):  # noqa: E501
        """Update a remedy  # noqa: E501

        Update accessible parameters of the requested resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_health_condition_remedy(body, health_condition_id, cause_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HealthConditionRemedyRequest body: Parameters that shall be updated (required)
        :param int health_condition_id: The resource defined in the URL (required)
        :param int cause_id: The resource defined in the URL (required)
        :param int id: Id of the remedy to update (required)
        :param str content_language: language of the content
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_health_condition_remedy_with_http_info(body, health_condition_id, cause_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_health_condition_remedy_with_http_info(body, health_condition_id, cause_id, id, **kwargs)  # noqa: E501
            return data

    def update_health_condition_remedy_with_http_info(self, body, health_condition_id, cause_id, id, **kwargs):  # noqa: E501
        """Update a remedy  # noqa: E501

        Update accessible parameters of the requested resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_health_condition_remedy_with_http_info(body, health_condition_id, cause_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HealthConditionRemedyRequest body: Parameters that shall be updated (required)
        :param int health_condition_id: The resource defined in the URL (required)
        :param int cause_id: The resource defined in the URL (required)
        :param int id: Id of the remedy to update (required)
        :param str content_language: language of the content
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'health_condition_id', 'cause_id', 'id', 'content_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_health_condition_remedy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_health_condition_remedy`")  # noqa: E501
        # verify the required parameter 'health_condition_id' is set
        if ('health_condition_id' not in params or
                params['health_condition_id'] is None):
            raise ValueError("Missing the required parameter `health_condition_id` when calling `update_health_condition_remedy`")  # noqa: E501
        # verify the required parameter 'cause_id' is set
        if ('cause_id' not in params or
                params['cause_id'] is None):
            raise ValueError("Missing the required parameter `cause_id` when calling `update_health_condition_remedy`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_health_condition_remedy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'health_condition_id' in params:
            path_params['health_condition_id'] = params['health_condition_id']  # noqa: E501
        if 'cause_id' in params:
            path_params['cause_id'] = params['cause_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_language' in params:
            header_params['Content-Language'] = params['content_language']  # noqa: E501

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
            '/health_conditions/{health_condition_id}/causes/{cause_id}/remedies/{id}', 'PATCH',
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
# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from influxdb_client.api_client import ApiClient


class DefaultService(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_post(self, delete_predicate_request, **kwargs):  # noqa: E501
        """delete Time series data from InfluxDB  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_post(delete_predicate_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeletePredicateRequest delete_predicate_request: predicate delete request (required)
        :param str zap_trace_span: OpenTracing span context
        :param str org: specifies the destination organization for writes
        :param str bucket: specifies the destination bucket for writes
        :param str org_id: specifies the organization ID of the resource
        :param str bucket_id: specifies the destination bucket ID for writes
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_post_with_http_info(delete_predicate_request, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_post_with_http_info(delete_predicate_request, **kwargs)  # noqa: E501
            return data

    def delete_post_with_http_info(self, delete_predicate_request, **kwargs):  # noqa: E501
        """delete Time series data from InfluxDB  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_post_with_http_info(delete_predicate_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeletePredicateRequest delete_predicate_request: predicate delete request (required)
        :param str zap_trace_span: OpenTracing span context
        :param str org: specifies the destination organization for writes
        :param str bucket: specifies the destination bucket for writes
        :param str org_id: specifies the organization ID of the resource
        :param str bucket_id: specifies the destination bucket ID for writes
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['delete_predicate_request', 'zap_trace_span', 'org', 'bucket', 'org_id', 'bucket_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'delete_predicate_request' is set
        if ('delete_predicate_request' not in local_var_params or
                local_var_params['delete_predicate_request'] is None):
            raise ValueError("Missing the required parameter `delete_predicate_request` when calling `delete_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'org' in local_var_params:
            query_params.append(('org', local_var_params['org']))  # noqa: E501
        if 'bucket' in local_var_params:
            query_params.append(('bucket', local_var_params['bucket']))  # noqa: E501
        if 'org_id' in local_var_params:
            query_params.append(('orgID', local_var_params['org_id']))  # noqa: E501
        if 'bucket_id' in local_var_params:
            query_params.append(('bucketID', local_var_params['bucket_id']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'delete_predicate_request' in local_var_params:
            body_params = local_var_params['delete_predicate_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_routes(self, **kwargs):  # noqa: E501
        """Map of all top level routes available  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_routes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: Routes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_routes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_routes_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_routes_with_http_info(self, **kwargs):  # noqa: E501
        """Map of all top level routes available  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_routes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: Routes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routes" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Routes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_signin(self, **kwargs):  # noqa: E501
        """Exchange basic auth credentials for session  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_signin(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_signin_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_signin_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_signin_with_http_info(self, **kwargs):  # noqa: E501
        """Exchange basic auth credentials for session  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_signin_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_signin" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/signin', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_signout(self, **kwargs):  # noqa: E501
        """Expire the current session  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_signout(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_signout_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_signout_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_signout_with_http_info(self, **kwargs):  # noqa: E501
        """Expire the current session  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_signout_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_signout" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/signout', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
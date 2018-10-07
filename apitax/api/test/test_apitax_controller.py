# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from apitax.api.models.auth_response import AuthResponse  # noqa: E501
from apitax.api.models.create import Create  # noqa: E501
from apitax.api.models.delete import Delete  # noqa: E501
from apitax.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.api.models.response import Response  # noqa: E501
from apitax.api.models.save import Save  # noqa: E501
from apitax.api.models.user_auth import UserAuth  # noqa: E501
from apitax.api.test import BaseTestCase


class TestApitaxController(BaseTestCase):
    """ApitaxController integration test stubs"""

    def test_authenticate(self):
        """Test case for authenticate

        Authenticate
        """
        user = UserAuth()
        response = self.client.open(
            '/apitax/2/apitax/auth',
            method='POST',
            data=json.dumps(user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_user(self):
        """Test case for create_user

        Create a new script
        """
        create = Create()
        response = self.client.open(
            '/apitax/2/drivers/{name}/apitax/users/{user}'.format(user='user_example', name='name_example'),
            method='POST',
            data=json.dumps(create),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        Delete a script
        """
        delete = Delete()
        response = self.client.open(
            '/apitax/2/drivers/{name}/apitax/users/{user}'.format(user='user_example', name='name_example'),
            method='DELETE',
            data=json.dumps(delete),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_config(self):
        """Test case for get_config

        Retrieve the config
        """
        response = self.client.open(
            '/apitax/2/apitax/config',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_log(self):
        """Test case for get_log

        Retrieve the logs
        """
        response = self.client.open(
            '/apitax/2/apitax/logs/{log}'.format(log='log_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        Retrieve a user
        """
        response = self.client.open(
            '/apitax/2/drivers/{name}/apitax/users/{user}'.format(user='user_example', name='name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_list(self):
        """Test case for get_user_list

        Retrieve a list of users
        """
        response = self.client.open(
            '/apitax/2/drivers/{name}/apitax/users'.format(name='name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_refresh_token(self):
        """Test case for refresh_token

        Refreshes login token using refresh token
        """
        response = self.client.open(
            '/apitax/2/apitax/auth/refresh',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_user(self):
        """Test case for save_user

        Save a script
        """
        save = Save()
        response = self.client.open(
            '/apitax/2/drivers/{name}/apitax/users/{user}'.format(user='user_example', name='name_example'),
            method='PUT',
            data=json.dumps(save),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_system_status(self):
        """Test case for system_status

        Retrieve the system status
        """
        response = self.client.open(
            '/apitax/2/apitax/status',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

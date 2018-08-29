# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from apitax.ah.api.models.auth_response import AuthResponse  # noqa: E501
from apitax.ah.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.ah.api.models.user_auth import UserAuth  # noqa: E501
from apitax.ah.api.test import BaseTestCase


class TestAnyController(BaseTestCase):
    """AnyController integration test stubs"""

    def test_authenticate(self):
        """Test case for authenticate

        Authenticate
        """
        user = UserAuth()
        response = self.client.open(
            '/apitax/2/auth',
            method='POST',
            data=json.dumps(user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_display_login(self):
        """Test case for display_login

        Displays the login page
        """
        response = self.client.open(
            '/apitax/2/login',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_asset(self):
        """Test case for get_asset

        Displays the user dashboard page
        """
        response = self.client.open(
            '/apitax/2/assets/{name}'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_refresh_token(self):
        """Test case for refresh_token

        Refreshes login token using refresh token
        """
        response = self.client.open(
            '/apitax/2/token/refresh',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

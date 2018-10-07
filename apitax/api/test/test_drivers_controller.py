# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from apitax.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.api.models.response import Response  # noqa: E501
from apitax.api.test import BaseTestCase


class TestDriversController(BaseTestCase):
    """DriversController integration test stubs"""

    def test_get_driver_blacklist(self):
        """Test case for get_driver_blacklist

        Retrieve the blacklist in the driver
        """
        response = self.client.open(
            '/apitax/2/drivers/{name}/blacklist'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_driver_config(self):
        """Test case for get_driver_config

        Retrieve the config of a loaded driver
        """
        response = self.client.open(
            '/apitax/2/drivers/{name}/config'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_driver_list(self):
        """Test case for get_driver_list

        Retrieve the catalog of drivers
        """
        response = self.client.open(
            '/apitax/2/drivers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_driver_status(self):
        """Test case for get_driver_status

        Retrieve the status of a loaded driver
        """
        response = self.client.open(
            '/apitax/2/drivers/{name}/status'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_driver_whitelist(self):
        """Test case for get_driver_whitelist

        Retrieve the whitelist in the driver
        """
        response = self.client.open(
            '/apitax/2/drivers/{name}/whitelist'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

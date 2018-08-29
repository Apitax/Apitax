# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from apitax.ah.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.ah.api.models.response import Response  # noqa: E501
from apitax.ah.api.test import BaseTestCase


class TestAdminsController(BaseTestCase):
    """AdminsController integration test stubs"""

    def test_display_admin_dashboard(self):
        """Test case for display_admin_dashboard

        Displays the developer admin page
        """
        response = self.client.open(
            '/apitax/2/dashboard/admin',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_driver_status(self):
        """Test case for driver_status

        Retrieve the status of a loaded driver
        """
        response = self.client.open(
            '/apitax/2/system/driver/{name}/status'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_system_status(self):
        """Test case for system_status

        Retrieve the system status
        """
        response = self.client.open(
            '/apitax/2/system/status',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

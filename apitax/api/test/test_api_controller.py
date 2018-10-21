# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from apitax.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.api.models.response import Response  # noqa: E501
from apitax.api.test import BaseTestCase


class TestApiController(BaseTestCase):
    """ApiController integration test stubs"""

    def test_get_driver_api_catalog(self):
        """Test case for get_driver_api_catalog

        Retrieve the api catalog
        """
        response = self.client.open(
            '/apitax/2/drivers/{driver}/api/catalog'.format(driver='driver_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_driver_api_status(self):
        """Test case for get_driver_api_status

        Retrieve the status of an api backing a driver
        """
        response = self.client.open(
            '/apitax/2/drivers/{driver}/api/status'.format(driver='driver_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

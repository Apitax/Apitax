# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from apitax.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.api.models.execute import Execute  # noqa: E501
from apitax.api.models.response import Response  # noqa: E501
from apitax.api.test import BaseTestCase


class TestCommandtaxController(BaseTestCase):
    """CommandtaxController integration test stubs"""

    def test_command(self):
        """Test case for command

        Execute a Command
        """
        execute = Execute()
        response = self.client.open(
            '/apitax/2/drivers/{driver}/commandtax/command'.format(driver='driver_example'),
            method='POST',
            data=json.dumps(execute),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

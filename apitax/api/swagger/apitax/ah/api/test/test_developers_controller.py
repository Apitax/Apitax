# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from apitax.ah.api.models.create import Create  # noqa: E501
from apitax.ah.api.models.delete import Delete  # noqa: E501
from apitax.ah.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.ah.api.models.rename import Rename  # noqa: E501
from apitax.ah.api.models.response import Response  # noqa: E501
from apitax.ah.api.models.save import Save  # noqa: E501
from apitax.ah.api.test import BaseTestCase


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_create_script(self):
        """Test case for create_script

        Create a new script
        """
        create = Create()
        response = self.client.open(
            '/apitax/2/system/script',
            method='POST',
            data=json.dumps(create),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_script(self):
        """Test case for delete_script

        Delete a script
        """
        delete = Delete()
        response = self.client.open(
            '/apitax/2/system/script',
            method='DELETE',
            data=json.dumps(delete),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_display_developer_dashboard(self):
        """Test case for display_developer_dashboard

        Displays the developer dashboard page
        """
        response = self.client.open(
            '/apitax/2/dashboard/developer',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rename_script(self):
        """Test case for rename_script

        Rename a script
        """
        rename = Rename()
        response = self.client.open(
            '/apitax/2/system/script',
            method='PATCH',
            data=json.dumps(rename),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_script(self):
        """Test case for save_script

        Save a script
        """
        save = Save()
        response = self.client.open(
            '/apitax/2/system/script',
            method='PUT',
            data=json.dumps(save),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

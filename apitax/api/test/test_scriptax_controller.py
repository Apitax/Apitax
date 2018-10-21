# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from apitax.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.api.models.response import Response  # noqa: E501
from apitax.api.models.script_create import ScriptCreate  # noqa: E501
from apitax.api.models.script_delete import ScriptDelete  # noqa: E501
from apitax.api.models.script_rename import ScriptRename  # noqa: E501
from apitax.api.models.script_save import ScriptSave  # noqa: E501
from apitax.api.test import BaseTestCase


class TestScriptaxController(BaseTestCase):
    """ScriptaxController integration test stubs"""

    def test_create_driver_script(self):
        """Test case for create_driver_script

        Create a new script
        """
        script_create = ScriptCreate()
        response = self.client.open(
            '/apitax/2/drivers/{driver}/scriptax/scripts'.format(driver='driver_example'),
            method='POST',
            data=json.dumps(script_create),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_driver_script(self):
        """Test case for delete_driver_script

        Delete a script
        """
        script_delete = ScriptDelete()
        response = self.client.open(
            '/apitax/2/drivers/{driver}/scriptax/scripts'.format(driver='driver_example'),
            method='DELETE',
            data=json.dumps(script_delete),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_driver_script(self):
        """Test case for get_driver_script

        Retrieve the contents of a script
        """
        query_string = [('script', 'script_example')]
        response = self.client.open(
            '/apitax/2/drivers/{driver}/scriptax/scripts'.format(driver='driver_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_driver_script_catalog(self):
        """Test case for get_driver_script_catalog

        Retrieve the script catalog
        """
        response = self.client.open(
            '/apitax/2/drivers/{driver}/scriptax/catalog'.format(driver='driver_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rename_driver_script(self):
        """Test case for rename_driver_script

        Rename a script
        """
        script_rename = ScriptRename()
        response = self.client.open(
            '/apitax/2/drivers/{driver}/scriptax/scripts'.format(driver='driver_example'),
            method='PATCH',
            data=json.dumps(script_rename),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_driver_script(self):
        """Test case for save_driver_script

        Save a script
        """
        script_save = ScriptSave()
        response = self.client.open(
            '/apitax/2/drivers/{driver}/scriptax/scripts'.format(driver='driver_example'),
            method='PUT',
            data=json.dumps(script_save),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

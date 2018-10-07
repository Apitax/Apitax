# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from apitax.api.models.create1 import Create1  # noqa: E501
from apitax.api.models.delete1 import Delete1  # noqa: E501
from apitax.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.api.models.rename import Rename  # noqa: E501
from apitax.api.models.response import Response  # noqa: E501
from apitax.api.models.save1 import Save1  # noqa: E501
from apitax.api.test import BaseTestCase


class TestScriptaxController(BaseTestCase):
    """ScriptaxController integration test stubs"""

    def test_create_driver_script(self):
        """Test case for create_driver_script

        Create a new script
        """
        create = Create1()
        response = self.client.open(
            '/apitax/2/drivers/{name}/scriptax/scripts'.format(name='name_example'),
            method='POST',
            data=json.dumps(create),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_driver_script(self):
        """Test case for delete_driver_script

        Delete a script
        """
        delete = Delete1()
        response = self.client.open(
            '/apitax/2/drivers/{name}/scriptax/scripts'.format(name='name_example'),
            method='DELETE',
            data=json.dumps(delete),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_driver_script(self):
        """Test case for get_driver_script

        Retrieve the contents of a script
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/apitax/2/drivers/{name}/scriptax/scripts'.format(name2='name_example'),
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
            '/apitax/2/drivers/{name}/scriptax/catalog'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rename_driver_script(self):
        """Test case for rename_driver_script

        Rename a script
        """
        rename = Rename()
        response = self.client.open(
            '/apitax/2/drivers/{name}/scriptax/scripts'.format(name='name_example'),
            method='PATCH',
            data=json.dumps(rename),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_driver_script(self):
        """Test case for save_driver_script

        Save a script
        """
        save = Save1()
        response = self.client.open(
            '/apitax/2/drivers/{name}/scriptax/scripts'.format(name='name_example'),
            method='PUT',
            data=json.dumps(save),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

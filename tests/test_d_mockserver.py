import unittest
from unittest.mock import patch, MagicMock

from d_mockserver.aws import AWS_Connect
from d_mockserver.query import InfoServer

dummyData = [1,2,3]

def dummyfunc():
    return {'Items':dummyData}

class TestMockServer(unittest.TestCase):
    
    @patch('boto3.client', return_value=MagicMock(id='test_id'))
    def test_get_id(self, mock_boto3_client):
        # Mocking
        aws_connect = AWS_Connect()
        aws_connect.connect_s3()
        # Test
        self.assertEqual('test_id', aws_connect.s3.id)
        
    # @patch('boto3.client', return_value=MagicMock(id='test_id'))
    # @patch('boto3.resource', return_value=MagicMock(scan=dummyfunc))
    # def test_get_table_column(self, mock_boto3_resource, mock_boto3_client):
    #     # Mocking
    #     aws_connect = AWS_Connect()
    #     aws_connect.connect_s3()
    #     # Test
    #     self.assertEqual('test_id', aws_connect.s3.id)
    #     self.assertEqual(dummyData, aws_connect.get_table_data())
        
        
    @patch('requests.get', return_value=MagicMock(status_code=200))
    def test_get_info(self, mock_requests_get):
        # Mocking
        info_server = InfoServer()
        # Test
        self.assertEqual(200, info_server.get_info().status_code)
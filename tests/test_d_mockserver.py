import unittest
from unittest.mock import patch, MagicMock

from d_mockserver.aws import AWS_Connect
from d_mockserver.query import InfoServer

dummyData = [1,2,3]

def dummyfunc():
    return {'Items':dummyData}

class TestMockServer(unittest.TestCase):
    
    #patch는 테스트하고자 하는 함수가 있는 곳을 mock으로 대체하는 것입니다.
    @patch('boto3.client', return_value=MagicMock(id='test_id'))
    def test_get_id(self, mock_boto3_client):
        # Mocking
        aws_connect = AWS_Connect()
        aws_connect.connect_s3()
        # Test
        self.assertEqual('test_id', aws_connect.s3.id)
        
    #위 코드는 아래코드와 완벽히 동일한 코드입니다. 
    @patch('boto3.client')
    def test_get_id2(self, mock_boto3_client):
        mock_boto3_client.return_value = MagicMock(id='test_id')
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
        
        
    @patch('requests.get')
    def test_get_info(self, mock_requests_get):
        mock_requests_get.return_value = MagicMock(status_code=456)
        # Mocking
        info_server = InfoServer()
        # Test
        self.assertEqual(456, info_server.get_info().status_code)
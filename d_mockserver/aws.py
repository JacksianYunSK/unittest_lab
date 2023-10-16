import boto3

class AWS_Connect : 
    def connect_s3(self) :
        # AWS S3 연결
        self.s3 = boto3.client('s3')
        self.table = boto3.resource('dynamodb', region_name='ap-northeast-2')
        
    def get_table_data(self) : 
        # AWS DynamoDB Table Column 정보 가져오기
        response = self.table.scan()
        return response['Items']
    
if __name__ == '__main__' :
    aws_connect = AWS_Connect()
    aws_connect.connect_s3()
    print(aws_connect.s3.id)
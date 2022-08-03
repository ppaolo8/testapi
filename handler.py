import boto3


class usertest:

    def __init__(self):
        client = boto3.resource('dynamodb')
        self.table = client.Table('Test')

    def  Create_data(self , event):
        response = self.table.put_item(
            Item={
                'testId': event['testId'],
                'name': event['name'],
                'surname': event['surname']
            }
        )
        return {
            'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
            'body': 'Record ' + event['testId'] + ' added'
        }    

    def  Read_data(self , event):
        response = self.table.get_item(
            Key={
                'testId': event['testId']
            }
        )
        if 'Item' in response:
            return response['Item']
        else:
            return {
                'statusCode': '404',
                'body': 'Not found'
            }

def lambda_handler(event, context):
    if event:
        user_Object =  usertest()
        if event['tasktype']  == "create":
            create_result =  user_Object.Create_data(event['data'])
            return create_result
        elif event['tasktype']  == "read":
            read_result =  user_Object.Read_data(event['data'])
            return read_result
       
        else :
            return {
                'statusCode': '404',
                'body': 'Not found'
            }
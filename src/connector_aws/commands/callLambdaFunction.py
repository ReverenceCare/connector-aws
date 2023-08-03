"""callLambdaFunction."""
import boto3
import json


class CallLambdaFunction:
    """Call an RCP lambda function."""

    def __init__(self, lambda_name: str):
        """
        :param lambda_name: The name of the lambda function to call
        :return: Json Data structure containing the response from the lambda.
        """
        self.lambda_name = lambda_name

    def execute(self, config, task_data):
        """Execute."""
        client = boto3.client("lambda")
        response = client.invoke(
            FunctionName=self.lambda_name,
            InvocationType="RequestResponse",
            Payload=json.dumps(task_data),
        )
        return json.loads(response["Payload"].read())

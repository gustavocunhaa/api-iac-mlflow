# Imports
from constructs import Construct
from aws_cdk import Stack, Tags
from aws.configs import PROJECT_NAME

# main construct imports
from aws.api_gateway.main.infrastructure import ApiGateway
from aws.lambda_.api.infrastructure      import LambdaApi

class SkeletonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Main Constructs
        lambda_api       = LambdaApi(self, "LambdaApi")
        api_gateway      = ApiGateway(self, "ApiGw", lambda_api.function)

        Tags.of(self).add("projeto", PROJECT_NAME)


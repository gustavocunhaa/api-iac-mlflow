# ------------------------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------------------------

from constructs import Construct
from aws_cdk import Duration, aws_apigateway, aws_lambda

from aws.configs import (
    PROJECT_NAME, VERSION_MAJOR, API_USERS, ENV
)


# ------------------------------------------------------------------------------------------------
# Lambda Construct
# ------------------------------------------------------------------------------------------------

class ApiGateway(Construct):

    def __init__(self, scope: Construct, construct_id: str, lambda_function: aws_lambda.Function, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Deployment Variables
        proj_ver = f"{PROJECT_NAME}_v{VERSION_MAJOR}"

        # Define the API Gateway
        api = aws_apigateway.RestApi(self, "PublicApi",
            rest_api_name = proj_ver,
            description = f"Public API for {proj_ver}",
            endpoint_configuration = aws_apigateway.EndpointConfiguration(
                types=[aws_apigateway.EndpointType.REGIONAL]
            ),
            deploy_options = {
                "stage_name": ENV
            }
        )

        # Integrate lambda backend with the API

        lambda_integration = aws_apigateway.LambdaIntegration(
            handler = lambda_function,
            timeout = Duration.seconds(29),
            allow_test_invoke = True,
            proxy = True
        )

        # Define the request model for input validation

        request_model = aws_apigateway.CfnModel(self, "RequestModel",
            name = "Request",
            description = f"Request model for {proj_ver} API",
            rest_api_id = api.rest_api_id,
            content_type = "application/json"
        )

        request_validator = aws_apigateway.CfnRequestValidator(self, "Validator",
            name = "ValidateRequestBody",
            rest_api_id = api.rest_api_id,
            validate_request_body = True
        )

        # Add a resource and method to the API

        resource = api.root.add_resource(proj_ver)
        method = resource.add_method(
            http_method = "POST",
            integration = lambda_integration,
            api_key_required = True,
            request_models = {"application/json": request_model},
            request_validator = request_validator
        )

        # Create a usage plan

        usage_plan = api.add_usage_plan("UsagePlan",
            name = f"{proj_ver}-usage_plan",
            description = f"Default usage plan for {proj_ver} API"
        )

        # Associate the stage with the usage plan

        usage_plan.add_api_stage(
            stage = api.deployment_stage
        )

        # Create API keys and associate them with the usage plan
        
        for user in API_USERS:
            api_key = api.add_api_key(f"ApiKey{user['name'].capitalize()}",
                api_key_name = f"{proj_ver}-{user['name'].lower()}",
                description = f"API {proj_ver} Key for {user['name'].capitalize()}"
            )
            usage_plan.add_api_key(api_key)

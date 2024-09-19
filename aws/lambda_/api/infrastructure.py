from constructs import Construct
from aws_cdk import Duration, aws_lambda, aws_events, aws_events_targets, aws_logs
from aws.configs import VERSION_PYTHON, LAMBDA_WARMUP, LAMBDA_MEMORY
from aws.iam.skeleton.infrastructure import IAMPolicies


class LambdaApi(Construct):
    
        def __init__(self, scope: Construct, construct_id: str, iam_policies: IAMPolicies, **kwargs) -> None:
            super().__init__(scope, construct_id, **kwargs)
            
            # Lambda code and function creation

            code_image = aws_lambda.DockerImageCode.from_image_asset(
                directory = ".",
                file = f"aws/lambda_/api/Dockerfile",
                build_args = {"VERSION_PYTHON": VERSION_PYTHON}
            )

            self.function = aws_lambda.DockerImageFunction(self, 'Function',
                code = code_image,
                timeout = Duration.seconds(30),
                memory_size = LAMBDA_MEMORY
            )

            # Lambda log group explicit creation
            log_group = aws_logs.LogGroup(self, 'LogGroup',
                log_group_name = f"/aws/lambda/{self.function.function_name}"
            )

            # Lambda warmup based on configs
            parameter   = LAMBDA_WARMUP["parameter"]
            rule = aws_events.Rule(self, 'Rule', schedule=aws_events.Schedule.expression(parameter))
            rule.add_target(aws_events_targets.LambdaFunction(
                handler = self.function,
                event = aws_events.RuleTargetInput.from_object({"warmup": True})
            ))

            # Lambda policies for resources
            all_policies = [
                  *iam_policies.policies_s3_main
            ]
            for policy in all_policies:
                self.function.add_to_role_policy(policy)

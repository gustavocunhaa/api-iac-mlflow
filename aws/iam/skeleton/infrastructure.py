from constructs import Construct
from aws_cdk import aws_iam

class IAMPolicies(Construct):
    
        def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
            super().__init__(scope, construct_id, **kwargs)

            s3_bucket = "s3://a3data-mlflow-storage"
            s3_folder = "mlflow"

            # Policies for accessing main S3 bucket
            self.policies_s3_main = [
                  aws_iam.PolicyStatement(
                    sid = 'S3Main',
                    actions = [
                        "s3:ListBucket",
                        "s3:GetBucketLocation",
                        "s3:GetObject",
                        "s3:PutObject",
                        "s3:DeleteObject",
                        "s3:AbortMultipartUpload",
                    ],
                    resources = [
                        f"arn:aws:s3:::{s3_bucket}",
                        f"arn:aws:s3:::{s3_bucket}/{s3_folder}/*"
                    ]
                )
            ]
            
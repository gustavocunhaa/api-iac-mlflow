import aws_cdk as cdk

from aws.configs import PROJECT_NAME, VERSION_MAJOR, ACCOUNT, REGION
from aws.stack import SkeletonStack

app = cdk.App()
SkeletonStack(
    app, f"{PROJECT_NAME}-v{VERSION_MAJOR}", 
    env=cdk.Environment(account=ACCOUNT, region=REGION)
)

app.synth()

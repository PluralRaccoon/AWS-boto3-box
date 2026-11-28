import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def verify_identity() -> None: 
    """Confirms active AWS identity before executing any infrastructure changes."""
    session = boto3.Session()
    sts_client = session.client("sts")

    try:
        identity = sts_client.get_caller_identity()
        print(f"Account ID : {identity['Account']}")
        print(f"User/Role  : {identity['Arn']}")
    except NoCredentialsError:
        print(f"STOP: Boto3 found no vvalid AWS credentials in the provider chain.")
    except ClientError as exc:
        print(f"AWS API Error: {exc.response['Error']['Message']}")

if __name__ == "__main__":
    verify_identity()
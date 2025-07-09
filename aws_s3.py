import boto3

s3=boto3.resource('s3')
bucket_name="tejas-python"
try:
    bucky=s3.create_bucket(
        Bucket=bucket_name, 
        CreateBucketConfiguration={'LocationConstraint':'ap-south-1'})
    print(bucky)
except Exception as error:
    print(error)
# -------------------------
delete=bucket_name.delete()
print(delete)
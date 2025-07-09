import boto3

ec2=boto3.resource('ec2')

instance=ec2.create_instances (
    ImageId='ami-0dee22c13ea7a9a67',
    MinCount=1,
    MaxCount=1,
    instanceType='t2.micro'
)

print(instance[0].id)

# termination

instance_id=''
instance=ec2.Instance(instance_id)
terminate=instance.terminate()
print(terminate)
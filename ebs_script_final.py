import boto3
import os
if os.path.exists("ebs_volumes.txt"):
  os.remove("ebs_volumes.txt")
else:
  print("The file does not exist") 
f = open("ebs_volumes.txt", "w")
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.volumes
#https://stackoverflow.com/questions/34002826/list-ec2-volumes-in-boto
ec2 = boto3.resource('ec2', region_name='us-west-2')
volume_iterator = ec2.volumes.all()
for volume_iterator in ec2.volumes.all():
    #print(ec2.Volume())
    # https://www.w3schools.com/python/python_file_write.asp
    f = open("ebs_volumes.txt", "a")
    f.write(str(volume_iterator) + '\n')
    f.close()
    print(volume_iterator)

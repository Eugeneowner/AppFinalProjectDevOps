# AWS account config
region      = "eu-central-1"
iam_profile = "mfa"

# General for all infrastructure
# This is the name prefix for all infra components
name = "eugene"

vpc_id      = "vpc-06df0f1ed4e799adb"
subnets_ids = ["subnet-0f77887c9e69fc162", "subnet-07bea859869364a5e", "subnet-0c31f62635097ce22"]


tags = {
  Environment = "test-eugene"
  TfControl   = "true"
}

zone_name = "devops7.test-danit.com"

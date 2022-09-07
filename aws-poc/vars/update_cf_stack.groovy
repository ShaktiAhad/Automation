def call(){
        return (command_functn("aws cloudformation update-stack --region ap-northeast-1 --stack-name s3-bucket-cf --use-previous-template --parameters ParameterKey=BucketPrefix,ParameterValue=${params.bucket_name} ParameterKey=Environment,ParameterValue=test --capabilities CAPABILITY_NAMED_IAM"))
}
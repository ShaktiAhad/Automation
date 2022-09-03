def call(){
    println (command_functn("aws cloudformation update-stack --stack-name s3-bucket-cf --use-previous-template --parameters ParameterKey=BucketPrefix,ParameterValue=${params.bucket_name} ParameterKey=Environment,ParameterValue=test --capabilities CAPABILITY_NAMED_IAM"))
}
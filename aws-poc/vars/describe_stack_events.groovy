def call(){
    withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-cred', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]){
        stack_events = command_functn("aws cloudformation describe-stack-events --region ap-northeast-1 --stack-name ${params.cf_stack_name}")["StackEvents"]
        return stack_events[0]
    }
}
def call(){
    stack_events = command_functn("aws cloudformation describe-stack-events --region ap-northeast-1 --stack-name ${params.cf_stack_name}")["StackEvents"]
    return stack_events
}
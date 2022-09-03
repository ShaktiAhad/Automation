#!/usr/bin/env groovy

def call(){
    stack_events = command_functn("aws cloudformation describe-stack-events --stack-name ${params.cf_stack_name}")["StackEvents"]
    return stack_events[0]
}
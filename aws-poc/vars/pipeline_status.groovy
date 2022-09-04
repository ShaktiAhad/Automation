def call(){
    withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-cred', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]){
        get_exec_id = command_functn("aws codepipeline list-pipeline-executions --region ap-northeast-1 --pipeline-name ${params.code_pipeline_name}")["pipelineExecutionSummaries"]["pipelineExecutionId"][0]
        pipeline_status = command_functn("aws codepipeline get-pipeline-execution --region ap-northeast-1 --pipeline-execution-id ${params.get_exec_id} --pipeline-name ${params.code_pipeline_name}")
        return pipeline_status["pipelineExecution"]["status"]
    }
}
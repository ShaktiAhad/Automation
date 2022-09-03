def call(){
    get_exec_id = command_functn("aws codepipeline list-pipeline-executions --pipeline-name ${params.code_pipeline_name}")["pipelineExecutionSummaries"]["pipelineExecutionId"][0]
    pipeline_status = command_functn("aws codepipeline  get-pipeline-execution --pipeline-execution-id ${get_exec_id} --pipeline-name ${params.code_pipeline_name}")
    return pipeline_status["pipelineExecution"]["status"]
}
def call(){
    get_pipeline_state = command_functn("aws codepipeline get-pipeline-state --region ap-northeast-1 --name ${params.code_pipeline_name}")
    return get_pipeline_state
}
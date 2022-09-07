def call(){
    return (command_functn("aws codepipeline start-pipeline-execution --region ap-northeast-1 --name ${params.code_pipeline_name}"))
}
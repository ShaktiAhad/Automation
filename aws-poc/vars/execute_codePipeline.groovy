def call(){
    println(command_functn("aws codepipeline start-pipeline-execution --name ${params.code_pipeline_name}"))
}
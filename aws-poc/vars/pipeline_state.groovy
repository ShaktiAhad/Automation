def call(){
    get_pipeline_state = command_functn("aws codepipeline get-pipeline-state --name ${params.code_pipeline_name}")
    for (stage in get_pipeline_state["stageStates"]){
        for (action in stage["actionStates"]){
            if (action.containsKey('latestExecution')){
            println("stageName: "+stage["stageName"]+ ", status: "+action['latestExecution']["status"])
            }
            else{
                println("stageName: "+stage["stageName"]+ ", status: null")
            }
        }
    }
}
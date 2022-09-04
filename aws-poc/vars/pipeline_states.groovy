def call(){
    withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-cred', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]){
        get_pipeline_state = command_functn("aws codepipeline get-pipeline-state --region ap-northeast-1 --name ${params.code_pipeline_name}")
        return get_pipeline_state

        // for (stage in get_pipeline_state["stageStates"]){
        //     for (action in stage["actionStates"]){
        //         if (action.containsKey('latestExecution')){
        //         println("stageName: "+stage["stageName"]+ ", status: "+action['latestExecution']["status"])
        //         }
        //         else{
        //             println("stageName: "+stage["stageName"]+ ", status: null")
        //         }
        //     }
        // }
    }
}
def call(){
    withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-cred', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]){
        get_pipeline_state = command_functn("aws codepipeline get-pipeline-state --region ap-northeast-1 --name ${params.code_pipeline_name}")
        return get_pipeline_state
    }
}
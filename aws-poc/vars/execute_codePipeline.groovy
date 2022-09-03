def call(){
    withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-cred', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]){
        println(command_functn("aws codepipeline start-pipeline-execution --region ap-northeast-1 --name ${params.code_pipeline_name}"))
    }
}
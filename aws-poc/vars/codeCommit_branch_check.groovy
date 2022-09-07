def call(){
    // withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-cred', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]){
    return (command_functn("aws codecommit get-branch --region ap-northeast-1 --repository-name ${params.code_commit_repo_name} --branch-name ${params.version}"))
    // }
}
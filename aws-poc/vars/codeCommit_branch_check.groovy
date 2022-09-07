def call(){
    return (command_functn("aws codecommit get-branch --region ap-northeast-1 --repository-name ${params.code_commit_repo_name} --branch-name ${params.version}"))
}
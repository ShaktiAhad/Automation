def call(){
    println (command_functn("aws codecommit get-branch --region ${AWS_DEFAULT_REGION}--repository-name ${params.code_commit_repo_name} --branch-name ${params.version}"))
}
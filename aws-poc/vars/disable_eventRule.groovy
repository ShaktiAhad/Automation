def call(){
    return (sh(script:"aws events disable-rule --region ap-northeast-1 --name ${params.event_rule_name}"))
}
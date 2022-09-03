import groovy.json.JsonSlurperClassic

def call(aws_command){
    def result = sh(script: "${aws_command}", returnStdout: true).trim()
    def parser = new JsonSlurperClassic()
    def json = parser.parseText(result)
    return json
}
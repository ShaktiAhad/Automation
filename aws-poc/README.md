## Change Event rule status, Update CF stack and execute CodePipeline by Jenkin

### Instantiate Jenkin 
I have created a custom docker image for this POC as the Jenkin must contain AWS CLI to execute the AWS command

* To buid the image - `docker build --no-cache -t gcp .` 

* To start the docker container - `docker run --name jenkin -v /Users/ahadnoor.shakti/jenkin_home:/var/jenkins_home -p $(ipconfig getifaddr en0):8080:8080 <image_id>`


Necessary commands
* [get-codeCommit-branch](https://docs.aws.amazon.com/cli/latest/reference/codecommit/get-branch.html)
* [update-CF-stack](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/update-stack.html)
* [describe-CF-stack-events](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stack-events.html)
* [start-Codepipeline-execution](https://docs.aws.amazon.com/cli/latest/reference/codepipeline/start-pipeline-execution.html)
* [get-pipeline-state](https://docs.aws.amazon.com/cli/latest/reference/codepipeline/get-pipeline-state.html)
* [get-pipeline-execution](https://docs.aws.amazon.com/cli/latest/reference/codepipeline/get-pipeline-execution.html)
* [list-pipeline-executions](https://docs.aws.amazon.com/cli/latest/reference/codepipeline/list-pipeline-executions.html)
* [enable-event-rule](https://docs.aws.amazon.com/cli/latest/reference/events/enable-rule.html)
* [disable-event-rule](https://docs.aws.amazon.com/cli/latest/reference/events/disable-rule.html)
* [describe-event-rule](https://docs.aws.amazon.com/cli/latest/reference/events/describe-rule.html)
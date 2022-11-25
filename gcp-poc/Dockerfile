FROM jenkins/jenkins:latest
USER root
RUN apt-get update && apt-get upgrade -y
RUN apt-get install vim -y
RUN apt-get install python3 -y 
RUN apt-get install python3-pip -y --ignore-missing

RUN curl -o /tmp/google-cloud-sdk.tar.gz https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-387.0.0-linux-x86_64.tar.gz
RUN tar -xvf /tmp/google-cloud-sdk.tar.gz -C /tmp/
RUN sh /tmp/google-cloud-sdk/install.sh -q
ENV PATH="/tmp/google-cloud-sdk/bin:${PATH}"
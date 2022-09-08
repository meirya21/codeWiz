# Jenkins Configuration as Code #

The Jenkins Configuration as Code (JCasC) feature defines Jenkins configuration parameters in a human-readable YAML file that can be stored as source code. This essentially captures the configuration parameters and values that are used when configuring Jenkins from the web UI. The configuration can then be modified by editing this file and then applying it.

This repo contains these files:

Dockerfile & docker-compose - builds Jenkins with docker
config.yaml - contains the configoration for jenkins
plugins.txt - the plugins that will be installed in jenkins when it builds
users.env - contain the user names and passwords for jenkins 

# create
    docker volume create --name=jenkins_home

    docker-compose up --build

Enter gui via http://localhost:8080


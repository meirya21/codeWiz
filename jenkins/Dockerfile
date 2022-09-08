FROM jenkins/jenkins:lts

# Taking control on jenkins configurtion:
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
COPY ./config.yml /var/jenkins_home/config.yml
ENV JENKINS_CONFIG /var/jenkins_home/config.yml

# installing plugins from file
COPY ./plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --clean-download-directory --list --view-security-warnings -f /usr/share/jenkins/ref/plugins.txt
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {

                git 'https://github.com/kodekloudhub/go-webapp-sample.git'
            }
        }

        stage('build') {
            steps {
                script {

                    sh 'go test ./...'

                }
            }

        }
    }
}

pipeline {
    agent {
        label {
            label 'master'
            customWorkspace "${JENKINS_HOME}/${BUILD_NUMBER}/"
        }
    }
    environment {
        Go111MODULE='on'
    }
    stages {
        stage('Checkout') {
            steps {

                git 'https://github.com/kodekloudhub/go-webapp-sample.git'
            }
        }

        stage('docker') {
            steps {
                script {

                   sh 'docker tag adminturneddevops/go-webapp-sample'

                }
            }

        }
    }
}
pipeline{
    agent any

    stages{
        stage('Cloning github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning github repo to Jenkins.................'
                    checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/bhavith1993/Hotel_Reservation.git']])
                }
            }
        }
    }
}
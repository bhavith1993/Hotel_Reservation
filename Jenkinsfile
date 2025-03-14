pipeline{
    agent any

    environment{
        VENV_DIR = 'venv'
    }

    stages{
        stage('Cloning github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning github repo to Jenkins.................'
                    checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/bhavith1993/Hotel_Reservation.git']])
                }
            }
        }

        stage('Setting up virtual enviornment and installing dependencies'){
            steps{
                script{
                    echo 'Setting up virtual enviornment and installing dependencies.................'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                     '''
                }
            }
        }
    }
}
pipeline{
    agent any

    environment{
        VENV_DIR = 'venv'
        GCP_PROJECT = "my-project-pdf-422714"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"

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

        stage('Builder and pushing docker image to GCR'){
            steps{ 
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script{
                        echo 'Builder and pushing docker image to GCR.................'
                        sh ''' 
                        export PATH = $PATH:$(GCLOUD_PATH)

                        gcloud auth activate-service-account --key-file ${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/hotel-reservation:latest .

                        docker push gcr.io/${GCP_PROJECT}/hotel-reservation:latest

                        '''
                    }  
                }
                
            }
        }
    }
}
pipeline {
    agent any
    environment {
        // Properly escaped Python path
        PYTHON_PATH = 'C:\\Program Files\\Python313;C:\\Program Files\\Python313\\Scripts'
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    echo 'Starting the Build Stage...'
                    if (fileExists('requirements.txt')) {
                        bat '''
                        set PATH=%PYTHON_PATH%;%PATH%
                        pip install -r requirements.txt
                        '''
                    } else {
                        error "requirements.txt not found in the workspace."
                    }
                }
            }
        }
        stage('SonarQube Analysis') {
            environment {
                // Sonar token retrieved securely using Jenkins credentials
                SONAR_TOKEN = credentials('sonar-token')
            }
            steps {
                echo 'Running SonarQube analysis...'
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner -Dsonar.projectKey=sonartest101 ^
                              -Dsonar.sources=./factorial.py ^
                              -Dsonar.host.url=http://localhost:9000 ^
                              -Dsonar.token=%SONAR_TOKEN%
                '''
            }
        }
    }
    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}

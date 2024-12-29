pipeline {
    agent any
    environment {
        PYTHON_PATH = 'C:\Program Files\Python313;C:\Program Files\Python313\Scripts'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip install -r requirements.txt
                '''
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonarqube-token')  // Retrieve SonarQube token from Jenkins credentials
            }
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner.bat -Dsonar.projectKey=sonartest101 ^
                                  -Dsonar.sources=. ^
                                  -Dsonar. host.url=http://localhost:9000 ^
                                  -Dsonar.token=%SONAR_TOKEN%
                '''
            }
        }
    }
    post {
        success {
            echo "Went well and good"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}

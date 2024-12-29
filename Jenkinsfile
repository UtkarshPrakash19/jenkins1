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
                                  -Dsonar.token=sqp_4ce1b003bba5b39a95b0e2d9ffd80d8256a24667
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

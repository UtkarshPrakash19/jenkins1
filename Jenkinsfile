pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "I am building"
            }
        }
        stage('Test') {
            steps {
                echo "I am testing"
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying"
            }
        }
    }
    post {
        success {
            echo 'Your pipeline is successful'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}

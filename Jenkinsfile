pipeline {
    agent any
    environment {
        // Correctly escaped Python path
        PYTHON_PATH = 'C:\\Program Files\\Python313;C:\\Program Files\\Python313\\Scripts'
    }
    stages {
        stage('Environment Setup') {
            steps {
                echo "Setting up the environment..."
                echo "Python Path is set to: ${env.PYTHON_PATH}"
            }
        }
        stage('Build') {
            steps {
                echo "Running the build stage..."
                // Add your build steps here
            }
        }
        stage('Test') {
            steps {
                echo "Running tests..."
                // Add your test commands here
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying the application..."
                // Add your deployment steps here
            }
        }
    }
    post {
        always {
            echo "Pipeline finished."
        }
        success {
            echo "Pipeline succeeded!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}

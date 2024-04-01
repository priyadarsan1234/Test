
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'python', url: 'https://github.com/priyadarsan1234/Test.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
        
        stage('Build') {
            steps {
                sh 'python setup.py build'
            }
        }
        
        
    }
    
    post {
        success {
            echo 'Pipeline succeeded! Project deployed.'
        }
        failure {
            echo 'Pipeline failed! Deployment aborted.'
        }
    }
}

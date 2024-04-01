pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/python']], extensions: [], userRemoteConfigs: [[credentialsId: '0a4c6aa9-a304-4dad-adfd-16fcf4d12e3b', url: 'https://github.com/priyadarsan1234/Test.git']])
            }
        }
        
        stage('Build') {
            steps {
                git branch: 'python', credentialsId: '0a4c6aa9-a304-4dad-adfd-16fcf4d12e3b', url: 'https://github.com/priyadarsan1234/Test.git'
            }
        }
        
        stage('Test') {
            steps {
                // Run the Test.py script and capture its output
                def output = bat script: 'python Test.py', returnStdout: true
                
                // Print the output to the Jenkins console
                echo "Test Output: $output"
            }
        }
    }
}

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
                script {
                    def pythonExecutable = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
                    def output = bat(script: "${pythonExecutable} Test.py", returnStdout: true).trim()

                    echo "Test Output: $output"
                }
            }
        }
    }
}


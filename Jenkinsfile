pipeline {
    agent any
    stages {
        stage('test'){
            steps {
                bat 'echo "Hello world"'
            }
        }
        stage('build') {
            steps {
                bat 'py --version'
            }
        }
    }
}

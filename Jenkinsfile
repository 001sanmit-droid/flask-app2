pipeline {
    agent any

    stages {
        stage('Install Packages') {
            steps {
                script {
                    sh 'pip install flask flask_sqlalchemy'
                    sh 'echo "done flask install sqlalchemy!!!"'
                }
            }
        }

        stage('Run the App') {
            steps {
                script {
                    sh 'python3 app.py &'
                    sh 'echo "done running app!!!"'
                    sleep 5
                }
            }
        }

        stage('Visit /') {
            steps {
                script {
                    sh 'curl http://localhost:5000/'
                    sh 'echo "rendering app on port 5000!!!"'
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh 'echo "done test!!!"'
                }
            }
        }
    }
}

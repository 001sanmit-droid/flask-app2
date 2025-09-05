pipeline {
    agent any
    stages {
        stage('Run the App') {
            steps {
                sh 'python3 app.py &'
                echo "done running app!!!"
                sleep 5
            }
        }

        stage('Visit /') {
            steps {
                sh 'curl http://localhost:5000/'
                echo "rendering app on port 5000!!!"
            }
        }

        stage('Cleanup') {
            steps {
                echo "done test!!!"
            }
        }
    }
}

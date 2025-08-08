pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/dwijavyas/playwright-pythonMain.git'
            }
        }

        stage('Setup Python venv') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest --headed --disable-warnings -q
                '''
            }
        }
    }

    post {
        always {
            junit '**/reports/*.xml' // If you generate JUnit XML reports
        }
    }
}

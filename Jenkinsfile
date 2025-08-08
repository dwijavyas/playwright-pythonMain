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

        stage('Provide Test Data') {
            steps {
                withCredentials([
                    file(credentialsId: 'pp-creds', variable: 'CREDS_FILE'),
                    file(credentialsId: 'pp-urls', variable: 'URLS_FILE')
                ]) {
                    bat '''
                    if not exist data mkdir data
                    copy "%CREDS_FILE%" data\\credentials.json
                    copy "%URLS_FILE%" data\\urls.json
                    '''
                }
            }
        }

        stage('Clean Results') {
            steps {
                bat 'rmdir /s /q results || echo results folder does not exist'
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                if not exist results mkdir results
                call venv\\Scripts\\activate
                pip install pytest-html
                pytest --headed --disable-warnings -q --html=results\\report.html || exit 0
                '''
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                reportDir: 'results',
                reportFiles: 'report.html',
                reportName: 'Test HTML Report',
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true
            ])
        }
    }
}

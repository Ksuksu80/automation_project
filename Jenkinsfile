pipeline{
    agent any // it can be replaced by Docker {image 'python:3.12'}

    triggers{
    // auto tests starts every day at 3 am
    cron('H 3 * * *')
    }

    stages{
        stage('Checkout'){
            steps{
                checkout scm
                }
            }
        stage('Install dependencies'){
            steps{
                sh'''
                    python3 -m venv venv
                    . venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install allure-pytest
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    mkdir -p reports
                    mkdir -p allure-results
                    pytest -q \
                        --junitxml=reports/junit.xml \
                        --html=reports/report.html \
                        --self-contained-html \
                        --alluredir=allure-results
                '''
            }
        }

        stage('Publish reports') {
            steps {
                junit 'reports/junit.xml'
                archiveArtifacts artifacts: 'reports/**', fingerprint: true
            }
        }
            // creates report under the build
            stage('Publish HTML Report') {
                steps {
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Pytest HTML Report'
                ])
            }
        }
        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            echo 'Build finished!'
        }
    }
}

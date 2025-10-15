pipeline{
    agent any // it can be replaced by Docker {image 'python:3.12'}

    triggers{
    // auto tests starts every day at 3 am
    cron('H3***')
    }

    stages{
        stage('Checkout'){
            steps{
                checkout scm
                }
            }
        stage('Install depensancies'){
            steps{
                sh'''
                    python3 -m venv venv
                    .venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    mkdir -p reports
                    pytest -q --junitxml=reports/junit.xml --html=reports/report.html --self-contained-html
                '''
            }
        }

        stage('Publish reports') {
            steps {
                junit 'reports/junit.xml'
                archiveArtifacts artifacts: 'reports/**', fingerprint: true
            }
        }
    }
}
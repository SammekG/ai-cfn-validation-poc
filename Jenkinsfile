pipeline {
    agent any

    stages {
        stage('AI CloudFormation Validation') {
            steps {
                sh 'ls -l'
                sh 'python3 validate_cfn.py templates/template.yaml'
            }
        }

        stage('Deploy (Optional)') {
            when {
                expression { false }
            }
            steps {
                echo 'Deployment skipped'
            }
        }
    }
}

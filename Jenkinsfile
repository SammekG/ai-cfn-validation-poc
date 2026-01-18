pipeline {
    agent any

    stages {
        stage('AI CloudFormation Validation') {
            steps {
                sh 'ls -l'
                sh 'python3 ai_validator.py ecs-stack.yaml'
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

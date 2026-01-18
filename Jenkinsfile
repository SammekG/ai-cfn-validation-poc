pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/SammekG/ai-cfn-validation-poc.git'
            }
        }

        stage('AI CloudFormation Validation') {
            steps {
                sh 'python3 ai_validator.py ecs-stack.yaml'
            }
        }

        stage('Deploy (Optional)') {
            steps {
                echo "Deployment stage"
            }
        }
    }
}

# 🧠 AI-Based CloudFormation Validation – POC

## 📌 Overview
This Proof of Concept (POC) demonstrates how AI-style validation can be integrated into a Jenkins CI/CD pipeline to detect security risks and cost inefficiencies in AWS CloudFormation templates before deployment.

## 🎯 Problem Statement
- Manual CloudFormation reviews
- Security misconfigurations
- Costly ECS sizing issues
- Late pipeline failures

## ✅ Solution
Integrate an AI-based validation step in Jenkins to analyze CloudFormation templates and fail early with actionable insights.

## 🏗️ Architecture Flow
Developer Commit → Git → Jenkins → AI Validator → Pass/Fail → CloudFormation Deploy

## 🔍 Validations
- Open security groups (0.0.0.0/0)
- Over-provisioned ECS CPU/Memory

## 🛠️ Prerequisites
- Ubuntu / EC2
- Jenkins
- Python 3
- Git

## 🚀 How to Run
1. Clone repo
2. Install dependencies
3. Configure Jenkins
4. Run pipeline

## 🧠 Why Needed
AWS services work post-deployment; this solution works pre-deployment.

## 🛣️ Future Enhancements
- Bedrock/OpenAI
- Cost prediction
- Auto remediation


# Event Driven Reporting System

## Project Overview
This project implements an event-driven data processing and automated reporting system using AWS cloud services and modern DevOps practices.

The system is designed to automatically provision infrastructure, process incoming data, and generate reports with minimal manual intervention.

## Architecture Summary
The solution follows an event-driven architecture where infrastructure and application workflows are triggered automatically by events such as code commits or data uploads.

## Technologies Used
- AWS (S3, EC2, Lambda – optional)
- Terraform (Infrastructure as Code)
- GitHub Actions (CI/CD automation)
- Python (Data processing and reporting)
- YAML (Pipeline and configuration files)

## Automation Flow
1. Code is pushed to the GitHub repository.
2. GitHub Actions pipeline is triggered automatically.
3. Terraform provisions AWS infrastructure.
4. Python scripts process data and generate reports.
5. Logs and outputs are monitored through pipeline execution.

## Fault Tolerance and Scalability
- AWS managed services ensure high availability and scalability.
- Terraform enables repeatable and consistent deployments.
- Event-driven design minimizes system downtime and manual errors.

## Conclusion
This project demonstrates how cloud infrastructure automation and event-driven processing can be combined to build scalable and reliable reporting systems.

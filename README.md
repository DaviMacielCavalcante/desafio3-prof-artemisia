# CI/CD Data Pipeline Challenge 🚀

## Overview

This repository is dedicated to a CI/CD challenge in analytical architecture, focusing on building a robust and automated data ingestion pipeline. The goal is to develop a data ingestion platform in a development environment and establish a deployment process to move pipelines to production efficiently.

## Key Objectives

- Automated Data Pipeline Deployment: Set up CI/CD workflows to deploy ingestion pipelines.

- Reliable Data Processing: Ensure clean and structured data flows into analytical environments.

- Unit Testing with Pytest: Implement automated tests to validate pipeline transformations.

## Technology Stack

- Programming Language: Python 🐍

- Testing Framework: Pytest 

- CI/CD Tools: GitHub Actions

- Containerization: Docker

## Getting Started

1. Clone the Repository:
```
git clone https://github.com/yourusername/cicd-data-pipeline.git
cd cicd-data-pipeline
```
2. Set Up Virtual Environment & Dependencies:
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Running Unit Tests:

Run tests to validate transformations and pipeline integrity:
```
pytest tests/
```
4. Push changes to trigger the CI/CD workflow and deploy the pipeline:

The workflow will try to deploy the new docker image in render.

```
git add .
git commit -m "Deploying ingestion pipeline"
git push origin main
```

5. Don't stray from the path to the dark side:

<div align="center">  
<img src="https://i.imgur.com/bdWG6NS.gif" width="500"/>  
</div>  

## Contribution Guidelines

We welcome contributions! Follow these steps:

1. Fork the repository.

2. Create a branch (git checkout -b feature-branch).

3. Implement changes and commit with meaningful messages (git commit -m 'Feature update').

4. Push your branch (git push origin feature-branch).

5. Open a pull request for review.

## **Contact:**  
If you have any questions or issues, feel free to contact:  
📧 Email: **davicc@outlook.com.br**  

## **Sith Lords Responsible for the Project:**  
- **Darth Davi** ⚔️😡  

## **Mentor Who Proposed the Challenge:**  
[Prof. Artemisia Weyl](https://www.linkedin.com/in/arteweyl/)  

👩‍💻 Mentor’s GitHub: [https://github.com/arteweyl](https://github.com/arteweyl)  

*Through victory, my chains are broken.  
The Force shall free me.*

# Secure REST API

A security-focused REST API project designed to demonstrate backend development, secure software engineering, and DevSecOps practices in a small cloud-deployed application.

The API will provide a simple **security findings management service** where authenticated users can create, view, and update security findings, while administrator-level users have broader management permissions. The project emphasizes building security controls directly into the application rather than treating security as a separate step after development.

## Project Goals

- Build a RESTful backend using **Python and FastAPI**
- Implement secure user authentication and authorization
- Apply **role-based access control (RBAC)** for analyst and administrator roles
- Protect passwords using secure password hashing
- Use token-based authentication for protected API endpoints
- Validate and sanitize incoming API data
- Store application data in a relational database
- Keep secrets and credentials outside of source code
- Containerize the application with **Docker**
- Add automated testing and security checks through **GitHub Actions**
- Deploy the API to a cloud platform such as **Microsoft Azure**
- Add logging and basic application monitoring

## Planned Security Controls

- Password hashing
- JWT-based authentication
- Role-based authorization
- Input validation
- Least-privilege access
- Secure secrets management
- Dependency and static-analysis scanning
- Automated tests in CI/CD
- Security-focused logging
- Error handling that avoids exposing sensitive information

## Planned Technology Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Security Scanning:** Semgrep and dependency/secret scanning
- **Cloud:** Microsoft Azure
- **Secrets Management:** Azure Key Vault
- **Monitoring:** Azure Application Insights

## Portfolio Focus

This project is intended as a compact demonstration of skills relevant to **Software Engineering, Backend Development, Application Security, Security Engineering, and DevSecOps**. It combines application development with practical security controls, automated security testing, containerization, and cloud deployment.

> **Status:** In development — weekend portfolio project.

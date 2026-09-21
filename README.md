# Secure REST API

I am building this project to practice how secure software development can be integrated directly into the development process. The goal is to create a small REST API that combines backend development, application security, cloud deployment, and DevSecOps practices in one project.

The API will provide a simple **security findings management service**. Authenticated users will be able to create, view, and update security findings. Administrator users will have additional permissions for managing findings and users. I want the project to focus on applying security controls from the beginning instead of treating security as something added after the application is already built.

## Project Goals

* Build a RESTful backend using **Python and FastAPI**
* Implement secure user authentication and authorization
* Apply **role based access control (RBAC)** for analyst and administrator roles
* Protect passwords using secure password hashing
* Use token based authentication for protected API endpoints
* Validate and sanitize incoming API data
* Store application data in a relational database
* Keep secrets and credentials outside of source code
* Containerize the application with **Docker**
* Add automated testing and security checks through **GitHub Actions**
* Deploy the API to **Microsoft Azure**
* Add logging and basic application monitoring

## Planned Security Controls

* Password hashing
* JWT based authentication
* Role based authorization
* Input validation
* Least privilege access
* Secure secrets management
* Dependency scanning
* Static analysis
* Secret scanning
* Automated tests in CI/CD
* Security focused logging
* Error handling that avoids exposing sensitive information

## Planned Technology Stack

* **Backend:** Python and FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Authentication:** JWT
* **Containerization:** Docker
* **CI/CD:** GitHub Actions
* **Security Scanning:** Semgrep, dependency scanning, and secret scanning
* **Cloud:** Microsoft Azure
* **Secrets Management:** Azure Key Vault
* **Monitoring:** Azure Application Insights

## Portfolio Focus

I want this project to show how I approach software engineering with security in mind. It brings together backend development, authentication, authorization, secure coding, automated security testing, containerization, cloud deployment, and CI/CD in one small application.

# AWS Python API DevOps Project

## Project Overview
This project focuses on building, containerising, testing, and deploying a Python REST API on AWS EC2.

## Technologies
- Python
- Docker
- Git and GitHub
- GitHub Actions
- AWS EC2
- AWS IAM
- OpenID Connect (OIDC)
- AWS Systems Manager

## Project Objectives
1. Build a Python REST API.
2. Maintain a local Git repository.
3. Write and update project documentation.
4. Containerise the application using Docker.
5. Implement automated tests and CI/CD.
6. Deploy to AWS EC2 using SSH initially. IAM roles, OIDC, and Systems Manager deployment are postponed until AWS account access restrictions are resolved.

## Project Status
A minimal Python API is implemented in app.py and has been manually tested on EC2.
It uses only the Python standard library, with no external dependencies.
Docker, automated tests, and CI/CD remain planned work.

## Run the API
From the project directory on the EC2 instance, run:

```bash
python3 app.py
```

The server listens only on 127.0.0.1:8000. It is accessible from the same
EC2 instance, not directly from other machines.
Keep this terminal open while testing.

## Test the API
Open another terminal on the same EC2 instance while the server is running.
Use curl with -i to display the HTTP status, response headers, and JSON body.

Check the health endpoint:

```bash
curl -i http://127.0.0.1:8000/health
```

Expected HTTP status: 200 OK
Expected JSON body: {"status": "ok"}

Check an unknown route:

```bash
curl -i http://127.0.0.1:8000/missing
```

Expected HTTP status: 404 Not Found
Expected JSON body: {"error": "not found"}

Both routes have been manually verified on the EC2 instance.

## Stop the API
Press Ctrl+C in the terminal running python3 app.py to stop the server.

## AWS Region
eu-north-1 (Stockholm)

# AWS Cloud Text Analysis (Tasks A1, A2, A3)

This project implements a cloud-based text analysis system using an event-driven architecture on AWS. A Flask web application allows users to upload one or multiple text files, which are processed using AWS Lambda via API Gateway. The solution supports parallel processing to improve scalability and performance.

---

## Overview

The system analyses uploaded text files and produces structured insights. It demonstrates key cloud computing concepts such as serverless execution, event-driven design, and parallel processing using managed AWS services.

---

## Architecture

The application follows the workflow below:

User → Flask Web Application (Local or EC2)  
→ Amazon S3 (Input Bucket)  
→ API Gateway (HTTP POST Endpoint)  
→ AWS Lambda (Text Analysis)  
→ JSON Results Returned to Flask UI  

For multiple file uploads, Lambda is invoked concurrently using parallel API requests.

---

## Task Mapping

###  A1 – Text Analysis Functions
The Lambda function implements three text analytics tasks:
- Word frequency analysis (Top 20 words, stop words removed)
- Sentence start word frequency analysis (Top 10 words)
- Sentence length statistics (mean, median, standard deviation)

Text is cleaned using regular expressions and a custom stop-word list.

---

### A2 – Event-Driven Cloud Deployment
- Users upload `.txt` files via a Flask web interface
- Files are stored in an Amazon S3 input bucket
- Processing is triggered via API Gateway
- AWS Lambda reads files from S3 and returns analysis results
- Flask renders results dynamically in the browser

This demonstrates an event-driven, serverless architecture.

---

###  A3 – Parallel Multi-File Processing
- Multiple text files can be uploaded simultaneously
- Unique S3 object keys are generated using UUIDs to avoid filename collisions
- The Flask application invokes Lambda concurrently using `ThreadPoolExecutor`
- Each file is processed independently with fault isolation

---

## Project Structure

```text
Cloud-text-analysis/
├─ flask-app/
│  ├─ app.py
│  ├─ templates/
│  │  ├─ upload.html
│  │  └─ data.html
│  └─ static/
│     └─ styles.css
├─ lambda/
│  └─ lambda_function.py
└─ README.md

```


### Running on AWS (Cloud Deployment)

In the deployed environment, the Flask web application runs on an Amazon EC2 instance, while all core processing components remain serverless and managed by AWS.

When running on AWS:
- The Flask application is hosted on an EC2 instance
- Uploaded files are stored in an Amazon S3 input bucket
- API Gateway exposes an HTTP endpoint
- AWS Lambda performs the text analysis and returns results
- The Flask application displays the results to the user

To access the application when deployed on EC2, open a browser and navigate to:
```text
http://<EC2_PUBLIC_IP>:8080

# sam-gardner.com

Personal portfolio and IT resume site. Built as an adaptation of the 
[Cloud Resume Challenge](https://cloudresumechallenge.dev/).

## Stack

- **Frontend:** HTML, CSS, Bootstrap 5 — hosted on Hostinger
- **Backend:** AWS Lambda + API Gateway + DynamoDB — serverless visitor counter
- **IaC:** AWS SAM
- **DNS:** Cloudflare
- **CI/CD:** GitHub Actions (coming soon)

## How it works

Static frontend calls an AWS API Gateway endpoint on page load. A Python 
Lambda function increments a visitor counter in DynamoDB and returns the 
current count. That's it.

## Built with

AI assistance. Infrastructure decisions, content, and architecture by Sam Gardner. 
Code by Claude. Reviewed by a human and a very opinionated Golden Retriever.
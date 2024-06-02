# AWS S3 Bucket Operations with Boto3

This project demonstrates basic operations on AWS S3 buckets using Python and Boto3, the AWS SDK for Python. The script interacts with AWS S3 to list existing buckets, create a new bucket, and delete a bucket.

## Prerequisites

Before you begin, ensure you have the following installed and configured:

1. **Python and pip**: Ensure Python 3.x is installed. Install pip if not already installed.
   
   ```bash
   # Check Python version
   python --version

   # Install pip if not installed
   python -m ensurepip --upgrade
   
   # Upgrade pip
   python -m pip install --upgrade pip
   ```

2. **Boto3**: Install Boto3, the AWS SDK for Python.

   ```bash
   pip install boto3
   ```

3. **AWS CLI**: Install and configure AWS CLI. This is required to set up AWS credentials and configure your AWS environment.

   ```bash
   # Install AWS CLI
   pip install awscli --upgrade --user

   # Configure AWS CLI with your credentials
   aws configure
   ```

   Follow the prompts to enter your AWS Access Key ID, Secret Access Key, default region name, and default output format. This sets up your AWS credentials and configures them in your local environment.

## Script Overview

The Python script (`boto3_script.py`) in this project performs the following operations:

- **List existing S3 buckets**: Retrieves a list of existing S3 buckets in your AWS account.
- **Create a new S3 bucket**: Creates a new S3 bucket with a specified name.
- **Delete an S3 bucket**: Deletes an existing S3 bucket by name.

## Script Usage

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install dependencies**:

   ```bash
   pip install boto3
   ```

3. **Configure AWS credentials**:

   Ensure your AWS credentials are configured properly using AWS CLI.

   ```bash
   aws configure
   ```

   Follow the prompts to enter your AWS Access Key ID, Secret Access Key, default region name, and default output format.

4. **Run the script**:

   Execute the Python script to perform AWS S3 operations.

   ```bash
   python boto3_script.py
   ```

   This script will:
   - List existing S3 buckets.
   - Create a new S3 bucket named `my-new-bucket-example`.
   - List existing S3 buckets again to confirm creation.
   - Delete the `my-new-bucket-example` bucket.
   - List existing S3 buckets once more to confirm deletion.

## Notes

- Ensure your AWS IAM user has the necessary permissions to perform S3 operations.
- Modify the bucket name (`my-new-bucket-example`) in the script as needed.
- Handle exceptions and errors that may occur during script execution.
- Always follow AWS best practices and security guidelines.

---

Save this content to a file named `README.md` in your project directory. This README provides clear instructions for setting up and using your script to manage S3 buckets using Boto3 and AWS CLI. Adjust any specific details or paths as per your actual project structure and requirements.

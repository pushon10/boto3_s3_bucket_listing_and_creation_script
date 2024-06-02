import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Function to list existing S3 buckets
def list_s3_buckets():
    try:
        # Lists buckets and stores them in the variable 'response'.
        response = s3.list_buckets()
        # Extract the list of buckets
        buckets = response['Buckets']
        # Print names of existing buckets and catch any errors.
        print("Existing S3 Buckets:")
        for bucket in buckets:
            print(f"- {bucket['Name']}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to create a new S3 bucket
def create_s3_bucket(bucket_name):
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully!")
    except Exception as e:
        print(f"An error occurred while creating the bucket: {str(e)}")

# Main function
def main():
    print("AWS S3 Bucket Operations")

    # List existing S3 buckets
    list_s3_buckets()

    # Create a new S3 bucket. Replace the name with one of your choosing.
    new_bucket_name = 'my-new-bucket-example'
    create_s3_bucket(new_bucket_name)

# Check if the script is being run directly by the Python interpreter
if __name__ == '__main__':
    main()

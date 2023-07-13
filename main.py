from file_upload_sample import upload_file

try:
    # Usage:
    file_type = "enrollment"  # Replace with the desired file type
    file_path = "sample.csv"  # Replace with the path to your file
    file_name = "sample.csv"  # Replace with the desired file name

    upload_file(file_type, file_path, file_name)

except Exception as e:
    print(f"Error: {str(e)}")

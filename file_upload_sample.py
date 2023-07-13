import requests

USERNAME = ""
PASSWORD = ""
ORGANIZATION_UID = ""
URL = ""


def authenticate():
    auth_url = f"{URL}/login"
    auth_payload = {
        "userName": USERNAME,
        "password": PASSWORD,
        "acceptedTerms": True
    }

    auth_response = requests.post(auth_url, json=auth_payload)

    if auth_response.status_code == 200:
        return auth_response.json()["sessionToken"]
    else:
        raise Exception("Authentication failed.")


def get_pre_signed_data(auth_token, file_type, file_name):
    upload_url = f"{URL}/files/upload"
    upload_headers = {
        "Authorization": f"JWT {auth_token}",
        "Organization": ORGANIZATION_UID
    }
    upload_payload = {
        "fileName": file_name,
        "productType": file_type,
    }

    upload_details = requests.post(upload_url, headers=upload_headers, json=upload_payload)

    if upload_details.status_code == 200:
        return upload_details.json()
    else:
        raise Exception("Failed to get upload details.")


def upload_file(file_type, file_path, file_name):
    try:
        # geta an authentication token by providing credentials
        auth_token = authenticate()

        # get pre-signed data to upload file to AWS s3
        pre_signed_data = get_pre_signed_data(auth_token, file_type, file_name)

        # Extract url and fields from the pre-signed data response
        url = pre_signed_data['url']
        fields = pre_signed_data['fields']

        # upload file
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(url, data=fields, files=files)

        if response.status_code == 204:
            print("File uploaded successfully.")
        else:
            print("Failed to upload file. Status code:", response.status_code)
    except Exception as e:
        print("Error:", str(e))

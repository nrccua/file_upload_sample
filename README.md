* Using python 3.7.2
* pip install -r requirements.txt
* Set required variables at the top of [file_upload_sample.py](file_upload_sample.py)
    * URL
    * ORGANIZATION_UID
    * USERNAME
    * PASSWORD
* Update example usage parameters [main.py](main.py)
    * file_type = "enrollment"  # Replace with the desired file type
    * file_path = "sample.csv"  # Replace with the path to your file
    * file_name = "sample.csv"  # Replace with the desired file name
    * file_description = "Some description for this file"  # Option file description
    * original_fileName = "testFile.csv" #File name from the original file uploaded. Signed URL will be generated to save file with this name.


* Run `python main.py`
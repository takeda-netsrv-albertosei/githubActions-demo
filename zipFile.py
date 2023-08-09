import zipfile

def compress_file(source_file, zip_file):
    with zipfile.ZipFile(zip_file, 'w') as zipf:
        zipf.write(source_file, arcname=source_file)

if __name__ == "__main__":
    source_file = "requirements.txt"  
    zip_file = "Requirementstxt.zip"  

    compress_file(source_file, zip_file)
    print(f"{source_file} compressed and saved as {zip_file}")

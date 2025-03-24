import requests
import os

def create_required_output_folder(path: str):
    if not os.path.exists(path):
        os.makedirs(path)

def download_image_request(img_src, headers, output_dir, filename):
    img = requests.get(img_src, headers=headers)

    if img.status_code != 200:
        return False
    else:
        with open(os.path.join(output_dir, filename), 'wb') as f:
            f.write(img.content)
        return True
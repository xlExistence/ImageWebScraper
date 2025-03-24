import os
import requests
from bs4 import BeautifulSoup
from utils.utils import (
    create_required_output_folder,
    download_image_request
)

OUTPUT_DIR = "output"

class ImageWebScraper:
    def __init__(self, output_dir_name: str = "IWS_Results"):
        self.output_dir_name = output_dir_name
        self.output_dir_path = os.path.join(OUTPUT_DIR, output_dir_name)
        create_required_output_folder(self.output_dir_path)

    def getFromURL(self, URL, imgs_limit = 3):
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"}
        r = requests.get(url=URL, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        container = soup.find(class_ = "stores-page")
        
        if container:
            # Method: Get all images within each row
            rows = container.find_all(
                "div",
                class_=lambda c: c and 'stores-row' in c 
            )
            print(f"Total product rows found: {len(rows)}\n")
            
            imgs_count = 0
            for row in rows:
                # Find IPhone image in each row
                # images = row.find_all('img', class_='EditorialTileProduct__image__M1rM1')

                # Find ALL images in each row
                images = row.find_all('img')
                if images:
                    for img in images:
                        if 'src' in img.attrs:
                            img_src = img['src']
                            filename = img_src.split('/')[-1]
                            
                            success = download_image_request(img_src, headers, self.output_dir_path, filename)
                            if success:
                                print(f"Success! '{filename}' downloaded!")
                                imgs_count += 1
                            else:
                                print(f"Failed! Error downloading image '{filename}'")
                        if imgs_count == imgs_limit: break

                if imgs_count == imgs_limit: break
            
            print(f"\nTotal images found: {imgs_count}")
from IWS import ImageWebScraper

if __name__ == "__main__":
    iws = ImageWebScraper(output_dir_name = "IWS_Results")
    iws.getFromURL(
        URL = "https://www.amazon.com.mx/stores/page/ACDAAFC2-EE98-4FD0-9123-B65C03276326",
        imgs_limit = 3
    )
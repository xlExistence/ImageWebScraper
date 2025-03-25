# ImageWebScraper
[ImageWebScraper](#imagewebscraper) is a tool that will be used to perform web scraping to an Amazon site, from which we can take the images and save them in our device.

As a base, we have the [Amazon IPhone Store](https://www.amazon.com.mx/stores/page/ACDAAFC2-EE98-4FD0-9123-B65C03276326) site, where we will get the search and collection of images of the available products to save them locally.

# Usage
First of all, we download the project with:

```
git clone https://github.com/xlExistence/ImageWebScraper.git
```

After getting the repo, to synchronize the executable environment and obtain the necessary libraries, inside the main folder, a terminal is opened from which we will execute:

```
uv sync
```

Then, to execute and obtain the results of the project, through the command line, we simply run:

```
python main.py
```

**Note** that it is possible to modify the following parameter values as needed from `main.py`:

* `output_dir_name`
* `imgs_limit`

# Considerations
If you do not modify the values or delete the following parameters, by default, you will get the following results:

* `output_dir_name = "IWS_Results"`
* `imgs_limit = 3`

# References and credits
## Videos
* [How to Scrape Images from a Website with Python (beautiful soup tutorial)](https://www.youtube.com/watch?v=NcsiXa_74jM&ab_channel=TonyTeachesTech)
    * From [Tony Teaches Tech](https://www.youtube.com/@TonyTeachesTech)
## Websites
* [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find)
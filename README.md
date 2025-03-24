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

After syncthing, it is necessary to place the execution interpreter into the `.venv` environment, either by **selecting it** from our preferred code editor (Visual Studio Code) or by **activating it** through the terminal with `.venv\Scripts\activate`

Then, to execute and obtain the results of the project, through the command line, we simply run:

```
python main.py iws --output-dir=x --imgs-limit=x
```

**Note** that it is possible to assign the parameter values as needed from the command execution by replacing `x`:

* `--output-dir` : Output directory name.
* `--imgs-limit` : Total limit of images to download.

# Considerations
If you do not assign parameter values, by default, you will get the following results:

* `--output-dir = IWS_Results`
* `--imgs-limit = 3`

# References and credits
## v0.1.0
### Videos
* [How to Scrape Images from a Website with Python (beautiful soup tutorial)](https://www.youtube.com/watch?v=NcsiXa_74jM&ab_channel=TonyTeachesTech)
    * From [Tony Teaches Tech](https://www.youtube.com/@TonyTeachesTech)
### Websites
* [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find)
## v0.2.0
### Videos
* [Write powerful CLIs in Python with Typer - Design Patterns](https://www.youtube.com/watch?v=qynsLmCEwhs&ab_channel=Patternite)
    * From [Patternite](https://www.youtube.com/@patternite538)
### Websites
* [Typer Documentation](https://typer.tiangolo.com/)
* [Typer One Command Help](https://github.com/fastapi/typer/discussions/937#discussioncomment-10376326)
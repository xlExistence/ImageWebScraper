import typer

from IWS import ImageWebScraper

cli = typer.Typer(
    help="ImageWebScraper is a tool that performs web scraping to an Amazon site, from which we can take the images and save them in our device. As a base, we have the Amazon IPhone Store site, where we will get the search and collection of images of the available products to save them locally."
)

@cli.command()
def iws(
    output_dir: str = typer.Option("IWS_Results", help="Output directory name."),
    imgs_limit: int = typer.Option(3, help="Total limit of images to download.")
):
    """
    ImageWebScraper URL based.
    """
    website_url = "https://www.amazon.com.mx/stores/page/ACDAAFC2-EE98-4FD0-9123-B65C03276326"
    iws = ImageWebScraper(output_dir_name=output_dir)
    iws.getFromURL(URL=website_url, imgs_limit=imgs_limit)

@cli.callback()
def callback():
    pass

if __name__ == "__main__":
    cli()
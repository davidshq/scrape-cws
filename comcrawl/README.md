# Comcrawl

Michael Harms wrote a small Python utility for downloading Common Crawl data. Unfortunately it was last updated in July of 2020 and doesn't work as-is. Rokas Ramanauskas made a few minor tweaks to the application which allow it to function again, you can grab Rokas fork here: https://github.com/rokasramas/comcrawl

It seems to work for very small crawls (e.g. I could pull down a page, the results of which are in the results.csv file), however it doesn't seem to work for larger crawls (e.g. I attempted to pull chrome.google.com/webstore/*). 

The common error I see thrown when making a larger request is:
> File "/home/someuser/miniconda3/lib/python3.10/gzip.py", line 436, in _read_gzip_header
>    raise BadGzipFile('Not a gzipped file (%r)' % magic)
> gzip.BadGzipFile: Not a gzipped file (b'<?')

This may be a nice app if you are just trying to see the absolute basics of how CC data can be retrieved, but I would recommend looking for something more robust for any other purpose.

## Installation
The package on PyPI for comcrawl is for Harms' original application and doesn't work so you can't easily use it. Instead of doing `pip install comcrawl` you will need to clone Rokas' fork and install it locally, e.g. from within scrape-cws/comcrawl run:

`git clone https://github.com/rokasramas/comcrawl.git`

Once this is done you can install the package locally by running:

`pipenv install ./comcrawl`

## Usage
- Open `main.py`
- Change the data variable that selects the desired crawl to the desired crawl.
- Change the URL in `client.search` to the desired URL.
- Run `python main.py`
- It make take a few minutes and if the server is overloaded you may have to try again.
- If it runs successfully you should see the output in `results.csv`
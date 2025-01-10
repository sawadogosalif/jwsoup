# JW SOUP

`jwsoup` is a simple Python package that scrapes Bible data from the JW.org website. The package provides functionality for scraping Bible verses and saving them in a structured format. It supports scraping data from one or multiple pages, handling paginated content, and storing the results in a Parquet file.

## Features

- Scrape Bible verses from individual or multiple pages.
- Clean the scraped verse text to remove unwanted characters.
- Store the scraped data in a Parquet file for further analysis.
- Simple interface with reusable functions.

## Installation

To install `jwsoup`, you can use pip from PyPI:

```bash
pip install jwsoup
```

Alternatively, if you want to install it locally from the source, clone the repository and run the following commands:

```bash
git clone https://github.com/sawadogosalif/jwsoup.git
cd jwsoup
pip install .
```

## Usage

### Scrape text - Single Page

You can scrape a single page of Bible verses using the `scrape_single_page` function. This function returns a list of verses and the URL for the next page (if available).

```python
jwsoup.text import scrape_single_page
url = "https://www.jw.org/fr/biblioth%C3%A8que/bible/bible-d-etude/livres/Gen%C3%A8se/1/"
verses, next_url = scrape_single_page(url)

# Print the scraped verses
for verse in verses:
    print(f"{verse[0]}: {verse[1]}")

# Print the next URL
print(f"Next page URL: {next_url}")
```

### Scrape text - Multiple Pages

To scrape multiple pages starting from a given URL, use the `scrape_multi_page` function. This function will follow pagination and save the scraped data in a Parquet file.

```python
from jwsoup.text import scrape_multi_page

start_url = "https://www.jw.org/mos/d-s%E1%BA%BDn-yiisi/biible/nwt/books/S%C9%A9ngre/1/"
output_dir = "bible_data_moore.parquet"
res = scrape_multi_page(start_url, output_dir=output_dir, max_pages=5, page_sep="books")
```

### Save Data to Parquet

The scraped data is stored in a Parquet file for efficient storage and querying. You can specify the output file and partition the data by page.

```python
import pandas as pd
pd.read_parque(output_dir).head()
```
![alt text](https://raw.githubusercontent.com/sawadogosalif/jwsoup/main/assets/output_multi_page.png)


### Downloads audios

```python

start_url = "https://www.jw.org/mos/d-s%E1%BA%BDn-yiisi/biible/nwt/books/yikri"
output_dir = "audio_files"
download_audios(start_url, output_dir,max_pages=3)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Salif Sawadogopro**  
  Email: [salif.sawadogopro@gmail.com](mailto:salif.sawadogopro@gmail.com)

## Acknowledgments

- Thanks to the `requests`, `beautifulsoup4`, `pandas`, `loguru`, and `pyarrow` libraries for making scraping and data handling easier.
- Thanks to [JW](https://www.jw.org/) for providing an accessible and rich resource of Bible texts in multiple langages
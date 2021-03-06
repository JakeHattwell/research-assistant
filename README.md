# Research Assistant
[![PyPI version](https://badge.fury.io/py/research-assistant.svg)](https://badge.fury.io/py/research-assistant)

Research Assistant is a Python 3 library featuring small utilities that make life easier.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Research Assistant. This needs elevated permissions (sudo or admin), or install into a virtualenv. The permissions are needed to add the scripts to path.

```bash
pip install research-assistant
```

## Scripts and Usage
To use a utility, simply call it from the command line. For example:

```bash
paper-scraper.py
```
will run the paper-scraper utility

| Script      | Description | Requirements |
| ----------- | ----------- | ------------ |
| paper-scraper.py | Run on a folder of PDF files to rename files in a AUTHOR_DATE_TITLE format. For example: `jourABC_article_184505.pdf` → `Hattwell_2020_Research Assistant.pdf`. Quality of renaming is highly dependent on metadata of PDFs. Double check before deleting anything. | PyPDF2 |


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Thanks
Thanks to Luke Husdell for feedback

# Mushoku Tensei Manga Downloader

Welcome to this github repository. This is a python-based mushoku tensei manga downloader written to download the manga from [MushokuTenseiScan](https://mushokutenseiscan.com/) and convert it to PDF file. I hope you’ll enjoy it!

## Installation

To install the downloader, first download/clone this repository:

```bash
git clone https://github.com/artinZareie/mushoku_tensei_manga
```

### (Optional) Vitrual Environment

If you’d like to, you can first enable python’s virtual environment. To do so, you’ll need to first install `venv` package from pip:

```bash
pip install virtualenv
```

Next, you need to enable the virtual env.
#### For Windows

```
.\bin\activate
```

#### For Linux/Unix/Mac

```bash
source ./bin/activate
```


### Installing Requirements

The requirements are listed in `requirements.txt` and can be installed using the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the application, `cd` to the root directory of the repository, and use one of the following options:

#### Interactive

To use the application interactively, just open the program, it will ask and explain, and helps you to download and list the manga.

```bash
python src/main.py
```

#### Flags

You can use flags instead to access the program:

1. List `-l` or `--list`

Gets the information from the website and lists all manga titles together with their lists:

```bash
python src/main.py -l
```

2. Download `-d` or `--download`

Asks for a link and downloads and converts the manga to pdf.

```bash
python src/main.py -d
Enter the manga link: <some link>
```

3. Download all `-a` or `--all`

Downloads the whole manga lists and converts all of them to pdf.


## Outputs

From wherever you run the program and the terminal is opened in, this program creates an `outputs/` directory and an `imgs/` directory. You can easily access PDFs from `outputs/` and images from `imgs/`.


# By Artin Zarei

from re import match
"""
Project Mushoku Tensei Manga Downloader
by github.com/artinZareie

This project uses beautifulsoup and requests
to download and save the manga from the source
https://mushokutenseiscan.com .

This project formats the manga in pdf format.
"""

from argparse import ArgumentParser

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from classes.PostRec import Post
from helpers.utils import *


URL_SOURCE = "https://mushokutenseiscan.com"  # For sake of simplicity.


def list_manga():
    print("Downloading the list of posts...")
    posts = get_posts_list(URL_SOURCE)
    print("Done.")
    print("The list of manga chapters is:")
    for post in posts:
        print(f"{post.title}: {post.link}")


def download_manga():
    link = input("Enter the manga link: ")
    title = get_entry_title(link)

    print("Downloading the manga...")
    download_single_post(Post(title, link))


def download_all():
    print("Downloading the list of posts...")
    posts = get_posts_list(URL_SOURCE)

    print("Downloading each post and saving it as pdf...")
    for post in tqdm(posts):
        download_single_post(post)

    print("Done. You can access your pdf files from `./outputs` folder and the individual images from `./imgs`. Good luck!")


def main():
    """
        Main function will handle the request.
        Three types of requests are accepted:
        1) List all manga posts available from website.
        2) Download one or more selected manga posts.
        3) Download all posts all together.
    """

    parser = ArgumentParser()
    parser.add_argument(
        "-l",
        "--list",
        help="List all manga posts available from website.",
        action="store_true",
    )
    parser.add_argument(
        "-d",
        "--download",
        help="Download one or more selected manga posts.",
        action="store_true",
    )
    parser.add_argument(
        "-a",
        "--all",
        help="Download all manga posts all together.",
        action="store_true",
    )

    # Parse the arguments
    args = parser.parse_args()

    if args.list:
        list_manga()
    elif args.download:
        download_manga()
    elif args.all:
        download_all()
    else:
        while True:
            print("""
Please select one of options below:
1) List all manga posts available from website.
2) Download one or more selected manga posts.
3) Download all posts all together.
4) Exit
                  """)
            choice = int(input("I choose: "))

            match choice:
                case 1:
                    list_manga()
                case 2:
                    download_manga()
                case 3:
                    download_all()
                case 4:
                    exit(0)
                case _:
                    print("Invalid choice.")


if __name__ == "__main__":
    main()

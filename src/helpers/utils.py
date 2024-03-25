"""
This file contains some functions that I use while creating the project.
"""
import os
import shutil

import requests
from pathlib import Path
from bs4 import BeautifulSoup
from tqdm import tqdm
from PIL import Image
from borb.pdf.canvas.layout.image.image import Image as BorbImage
from borb.pdf import SingleColumnLayout

from classes.PostRec import Post


def get_posts_list(source):
    try:
        response = requests.get(source)
        soup = BeautifulSoup(response.text, "html.parser")
        recent_posts = soup.find('li', id='recent-posts-3')
        post_list = []
        if recent_posts:
            for post in recent_posts.find_all('a'):
                title = post.text.strip()
                link = post['href']
                post_list.append(Post(title, link))

        post_list = post_list[::-1]  # Invert the order of list.
        return post_list
    except Exception:
        print("Program exited with an error.")
        exit(1)


def get_entry_title(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    entry_title = soup.find('h1', class_='entry-title')
    if entry_title:
        return entry_title.text.strip()
    else:
        return None


def images_to_pdf(images_list, output_pdf):
    if not os.path.exists(os.path.dirname(output_pdf)):
        os.makedirs(os.path.dirname(output_pdf))

    pil_images = [Image.open(image) for image in images_list]
    pil_images[0].save(output_pdf, "PDF", save_all=True,
                       append_images=pil_images[1:])

    print("PDF created successfully!")


def download_single_post(post):
    folder_name = os.path.join(os.path.join(os.getcwd(), 'imgs'), post.title)
    os.makedirs(folder_name, exist_ok=True)

    response = requests.get(post.link)

    soup = BeautifulSoup(response.text, "html.parser")
    image_tags = soup.find_all("div", class_="separator")
    images_list = []

    if len(image_tags) == 0:
        print("No image to process, continue...")
        return

    with tqdm(total=len(image_tags),
              desc=f"Downloading Images for '{post.title}'") as pbar:
        for idx, image_tag in enumerate(image_tags, 1):
            img_url = image_tag.find('img')['src']
            img_name = f"{idx}.jpg"
            img_path = os.path.join(folder_name, img_name)
            images_list.append(img_path)

            if os.path.exists(img_path):
                pbar.update(1)
                continue

            img_response = requests.get(img_url)
            with open(img_path, 'wb') as f:
                f.write(img_response.content)

            pbar.update(1)

    print("Post downloaded successfully!")

    print("Converting images to pdf...")
    output_pdf = os.path.join(
        os.path.join(os.getcwd(), 'outputs'),
        f"{post.title}.pdf"
    )
    images_to_pdf(images_list, output_pdf)
    print("Done!")

    return folder_name

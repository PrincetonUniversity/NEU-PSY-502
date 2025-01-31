import subprocess
import sys

import jinja2
from jinja2 import Template
import yaml
import json
import os
import shutil
import filecmp
import nbformat
import re

# Directory paths
SOURCE_DIR = "./website/_build/html/content"



skip_dirs = ["_build"]


def replace_colab_link(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        pattern = r"https://colab\.research\.google\.com/github/([^/]+)/([^/]+)/blob/master/website/(.+)"
        replacement = r"https://colab.research.google.com/github/\1/\2/blob/gh-pages/_sources/\3"
        replaced = re.sub(pattern, replacement, content)
    with open(file_path, "w") as f:
        f.write(replaced)


def build():
    # copy_if_changed(SOURCE_DIR, BUILD_DIR)
    #
    # _d = None
    # with open(f"{BUILD_DIR}/_config.yml") as f:
    #     _d = yaml.safe_load(f)
    #     _d["repository"]["path_to_book"] = "_book_build"
    #
    # yaml.safe_dump(_d, open(f"{BUILD_DIR}/_config.yml", "w"))

    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith(".html"):
                print('replace colab link in', os.path.join(root, file))
                replace_colab_link(os.path.join(root, file))


            # if file.endswith(".ipynb"):
            #     build_notebook(os.path.join(root, file))
            #     process_notebook(os.path.join(root, file))
            # elif file.endswith(".md"):
            #     build_markdown(os.path.join(root, file))





def main():

    build()



if __name__ == '__main__':
    main()

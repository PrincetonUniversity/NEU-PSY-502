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

# Directory paths
SOURCE_DIR = "./website"
BUILD_DIR = "./website"
JUPYTER_BOOK_BUILD_CMD = ["jupyter-book", "build", "_website_build"]
PUBLISH_CMD = "ghp-import -n -p -f _website_build/_build/html"

skip_dirs = ["_build"]

exercise_template = Template(
"""
<h{{ title_level }} style="background: #256ca2; color: #e9e9e9">🎯 {{ title }}</h{{ title_level}}>
    
{{ content }}
    
"""
)

hint_template = Template(
"""
<details><summary style="background: #d6c89d; color: #e9e9e9">💡 {{ title }}</summary>
    
{{ content }}
    
</details>
    
"""
)

solution_template = Template(
"""
<details><summary style='background: #22ae6a; color:#e9e9e9'>✅ {{ title }}</summary>
    
{{ content }}
    
</details>
    
""")

pdf_template = Template(
"""
<iframe src="{{ path }}" width="100%" height="600px"></iframe>

""")


def copy_if_changed(src_dir, dest_dir):
    """
    Recursively copy files from src_dir to dest_dir, only if the file has changed.
    """
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)

    # Walk through the source directory
    for root, dirs, files in os.walk(src_dir):
        # Compute relative path to maintain directory structure
        relative_path = os.path.relpath(root, src_dir)

        if any(relative_path == d or relative_path.startswith(d + os.sep) for d in skip_dirs):
            continue

        # if the current directory is in skip list, pass

        current_dest_dir = os.path.join(dest_dir, relative_path)

        # Ensure the current destination subdirectory exists
        os.makedirs(current_dest_dir, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(current_dest_dir, file)

            # Copy only if the file doesn't exist in destination or content differs
            if not os.path.exists(dest_file) or not filecmp.cmp(src_file, dest_file, shallow=False):
                shutil.copy2(src_file, dest_file)
                # print(f"Copied: {src_file} -> {dest_file}")
            # else:
            # print(f"Skipped (unchanged): {src_file}")


def build_notebook(path=BUILD_DIR, yaml_path=f"{BUILD_DIR}/_config.yml"):
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(searchpath="."),
        autoescape=False
    )
    # Load yaml file
    with open(yaml_path) as f:
        variables = yaml.safe_load(f)["parse"]["myst_substitutions"]

    template = env.get_template(path)

    rendered_notebook_str = template.render(**variables)

    rendered_nbjson = json.loads(rendered_notebook_str)
    rendered_notebook_str = json.dumps(rendered_nbjson, indent=1)
    # Write out the final notebook with the same name but with _colab appended
    with open(path, "w") as f:
        f.write(rendered_notebook_str)


def process_notebook(path=BUILD_DIR):
    def _process_title(title, rep):
        title = title.replace(rep, '')
        # count how many # are in the title
        count = 0
        for char in title:
            if char == '#':
                count += 1
        title = title.replace('#', '')
        return title, count

    with open(path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=nbformat.NO_CONVERT)
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            title = cell['source'].split('\n')[0]
            if '{exercise}' in title:
                title, count = _process_title(title, '{exercise}')
                content = '\n'.join(cell['source'].split('\n')[1:]) if len(cell['source'].split('\n')) > 1 else ''
                cell['source'] = exercise_template.render(title=title, content=content, title_level=count)
            if '{hint}' in title:
                title, _ = _process_title(title, '{hint}')
                content = '\n'.join(cell['source'].split('\n')[1:]) if len(cell['source'].split('\n')) > 1 else ''
                cell['source'] = hint_template.render(title=title, content=content)
            if '{solution}' in title:
                title, _ = _process_title(title, '{solution}')
                content = '\n'.join(cell['source'].split('\n')[1:]) if len(cell['source'].split('\n')) > 1 else ''
                cell['source'] = solution_template.render(title=title, content=content)
    with open(path, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)


def build_markdown(path=BUILD_DIR, yaml_path=f"{BUILD_DIR}/_config.yml"):
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(searchpath="."),
        autoescape=False
    )
    # Load yaml file
    with open(yaml_path) as f:
        variables = yaml.safe_load(f)["parse"]["myst_substitutions"]

    template = env.get_template(path)

    rendered_notebook_str = template.render(**variables)
    with open(path, "w", encoding="utf-8") as f:
        f.write(rendered_notebook_str)


def build():
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith(".ipynb"):
                build_notebook(os.path.join(root, file))
                process_notebook(os.path.join(root, file))
            elif file.endswith(".md"):
                build_markdown(os.path.join(root, file))


if __name__ == '__main__':
    build()

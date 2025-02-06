# CONTRIBUTING

## How to add a new page

1. Create a new markdown or jupyter notebook file in the `website/content` folder.
2. Add the file to the `website/_toc.yml` file to make it appear in the sidebar.
3. There might are three places, where you also might want to add a link to the new page:
    - `website/intro.md` for the main page
    - `website/content/502A/syllabus.md` (for 502A)
    - `website/content/502B/syllabus.md` (for 502B)

## Adding static files (e.g., images, pdfs)

To make files accessible everywhere (e.g., when using the notebooks in google colab), we use static files:

### Add an image

1. add the image to the `web_static/images` folder
2. Use the following code snippet to display the image. (Replace `/<file-name>` with the name of the image file.)
```markdown
![alt-text](https://princetonuniversity.github.io/NEU-PSY-502/_static/images/<file-name>)
```

### Add a pdf file

1. Add the pdf file to the `_static/pdf` folder.
2. Add the following code snippet to the markdown file where you want to display the pdf file. (Replace `<file-name>` with the name of the pdf file.)
```markdown
<iframe src="https://princetonuniversity.github.io/NEU-PSY-502/_static/pdf/<path-to-file>" width="100%" height="600px"></iframe>
```

## Automatic build and deployment

The website is automatically built and deployed using GitHub Actions. 
The build process is triggered whenever a new commit is pushed to the `main` branch. 
The website is deployed to the `gh-pages` branch.

### How to preview the website locally

To preview the website locally, you can use the following steps:

Change to the `website` directory:
```bash
cd website
```

Install the required packages:
```bash
pip install jupyter-book
pip install psyneulink
```

Build the website:
```bash
jupyter-book build .
```

There now should be a build directory. You can preview the website by looking at the `index.html` file in the `_build/html` directory.

### How can I temporarily disable the automatic build and deployment?

If you want to make changes to the website without executing all the notebooks, you can disable this by changing the `_config.yml` file in the `website` directory.

Change the following line:
```
execute:
  execute_notebooks: force
```

to:
```
execute:
  execute_notebooks: off
```

## Pre and Postprocessing

The notebooks are processed before uploading to the website. For the development of the notebooks, 
this has one main implications:

There are three "magic" tags that will render differently on the website than in the local jupyter notebook:

- {exercise}
- {hint}
- {solution}

If you add these to the end of the first line of a cell (for example after the title), these will be rendered with special colors and the hints and solutions will be hidden by default.






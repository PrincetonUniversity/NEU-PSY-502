# CONTRIBUTING

## How to add a new page

1. Create a new markdown or jupyter notebook file in the `website/content` folder.
2. Add the file to the `website/_toc.yml` file to make it appear in the sidebar.

## Adding static files (e.g., images, pdfs)

To make files accesible everywhere (e.g., when openinig the website in google colab), we use static files:

## Add an image

1. add the image to the `web_static/images` folder
2. Use the following code snippet to display the image. (Replace `/<file-name>` with the name of the image file.)
```markdown
![alt-text](https://princetonuniversity.github.io/NEU-PSY-502/_static/images/<file-name>)
```

## Add a pdf file

1. Add the pdf file to the `_static/pdf` folder.
2. Add the following code snippet to the markdown file where you want to display the pdf file. (Replace `<file-name>` with the name of the pdf file.)
```markdown
<iframe src="https://princetonuniversity.github.io/NEU-PSY-502/_static/pdf/<file-name>" width="100%" height="600px"></iframe>
```

## How to build the website

The website is 



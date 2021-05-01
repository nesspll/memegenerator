###**Project: Meme Generator**

This small application generates memes based on the images and quotes you provide.

<hr>

#####**Functionality and Architecture**

It has two core modules:
- **Meme Engine Module:**
    - It uses Pillow(PIL) to load and manipulate images
    - It recieves a path where the images will be saved as memes
    - It's method 'meme()' recieves the image, width, and quote
    - Finally it returns the image as a path location.
- **Quote Engine Module:**
    - It has 4 Ingestor classes: csv, pdf, docx, txt
    - The 4 Ingestors inherit for base/common functionality from IngestorInterface(an Abstract class)
    - And, finally it has an Ingestor class which selects the appropriate Ingestory based on the file extension.
    
<hr>

#####**Requirements**

- flask
- request
- python-docx
- pillow
- pandas

<hr>


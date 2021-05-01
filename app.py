import random
import os
import requests
from flask import Flask, render_template, abort, request
from urllib.parse import urlparse

# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    images = []
    for root, dirs, files in os.walk(images_path):
        images = [os.path.join(root, name) for name in files]


    static_path = './static'
    if not os.path.exists(static_path):
        os.mkdir(static_path)

    return quotes, images


quotes, images = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """


    img = random.choice(images)
    quote = random.choice(quotes)
    path = meme.meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    if request.method == 'POST':
        imageUrl = request.form.get('image_url', default=None)
        body = request.form.get('body', default=None)
        author = request.form.get('author', default=None)

        if imageUrl is not None:
            response = requests.get(imageUrl)
            temp_file = os.path.basename(urlparse(imageUrl).path)
            temp_file = os.path.join('./static', temp_file)
            print(temp_file)
            with open(temp_file, 'wb') as fp:
                fp.write(response.content)

        path = ""
        meme = MemeEngine('./static')
        try:
            path = meme.meme(temp_file, body, author)
            os.remove(temp_file)
        except Exception as e:
            print(e)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()

#!/usr/bin/python3
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='')

@app.route('/show/<uuid>')
def index(uuid):
  # get uuid
  return render_template('ad.html', handle="veggiegrill", logo='/logo.jpg', name="Veggie Grill", images=['/img1.jpg','/img2.jpg','/img3.jpg','/img4.jpg','/img5.jpg','/img6.jpg'])

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
   return send_from_directory('.', path)

if __name__ == '__main__':
  app.run(debug=True)

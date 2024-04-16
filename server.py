from flask import Flask, render_template, request, jsonify, Markup, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home_page.html')   

if __name__ == '__main__':
   app.run(debug = True)
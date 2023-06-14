from app import app
from flask import render_template, request, redirect, url_for
from app.utils import get_element, selectors
import requests
import json
import os
from bs4 import BeautifulSoup


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/extract')
def extract():
    return render_template('extract.html')
    

@app.route('/products_list')
def products_list():
    return render_template('products_list.html')

@app.route('/product')
def product():
    return render_template('product.html')

    
@app.route('/author')
def author():
    return render_template('author.html')
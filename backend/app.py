import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from models import *
import json
from utilities import *
from flask_cors import CORS
from flask import Flask, request
from math import floor
import time
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

engine = create_engine(f'sqlite:///{BASE_DIR}/database.db')
Session = sessionmaker(bind=engine)



@app.route('/item/<sku>', methods=['POST', 'GET'])
def item(sku):
    new_session = Session()
    for x in sectionList:
        q = new_session.query(x).filter_by(sku = sku).one_or_none()
        if q != None:
            return serialize_object(q)
    return {'message': 'There is no items any more.'}

@app.route('/shippingoptions/<int:qtd>')
def shipping_options(qtd):
    base_price = 9.99
    subprice   = floor(qtd/10)*base_price
    current_date = datetime(
        year=time.localtime().tm_year,
        month=time.localtime().tm_mon,
        day=time.localtime().tm_mday
    )
    return (json.dumps([
        {'type':'Normal', 'price': subprice, 'arrives': f'{(current_date+timedelta(days=20)).day}/{(current_date+timedelta(days=20)).month}'},
        {'type':'Fast', 'price': subprice*2, 'arrives': f'{(current_date+timedelta(days=5)).day}/{(current_date+timedelta(days=5)).month}'},
        {'type':'Real fast', 'price': subprice*5, 'arrives': f'{(current_date+timedelta(days=1)).day}/{(current_date+timedelta(days=1)).month}'},
    ]))


@app.route('/men', methods=['POST', 'GET'])
def men_items_view():
    # Here I initiate a session
    new_session = Session()
    try:
        if request.args['filter'] == 'lowest price':
            # Here I make the query using order by price asc
            items = new_session.query(MenClothes).order_by(MenClothes.price.asc()).all()
            new_session.close()
            return serialize_objects(items)
        elif request.args['filter'] == 'highest price':
            # Here I make the query using order by price desc
            items = new_session.query(MenClothes).order_by(MenClothes.price.desc()).all()
            new_session.close()
            return serialize_objects(items)
        else:
            # Here I make the default query
            items = new_session.query(MenClothes).all()
            new_session.close()
            return serialize_objects(items)
            # Note that after each query the session is closed
    except:
        items = new_session.query(MenClothes).all()
        new_session.close()
        return serialize_objects(items)

@app.route('/women')
def women_items_view():
    # Here I initiate a session
    new_session = Session()
    try:
        if request.args['filter'] == 'lowest price':
            # Here I make the query using order by price asc
            items = new_session.query(WomenClothes).order_by(WomenClothes.price.asc()).all()
            new_session.close()
            return serialize_objects(items)
        elif request.args['filter'] == 'highest price':
            # Here I make the query using order by price desc
            items = new_session.query(WomenClothes).order_by(WomenClothes.price.desc()).all()
            new_session.close()
            return serialize_objects(items)
        else:
            # Here I make the default query
            items = new_session.query(WomenClothes).all()
            new_session.close()
            return serialize_objects(items)
            # Note that after each query the session is closed
    except:
        items = new_session.query(WomenClothes).all()
        new_session.close()
        return serialize_objects(items)

@app.route('/acessories')
def acessories_items_view():
    # Here I initiate a session
    new_session = Session()
    try:
        if request.args['filter'] == 'lowest price':
            # Here I make the query using order by price asc
            items = new_session.query(Acessories).order_by(Acessories.price.asc()).all()
            new_session.close()
            return serialize_objects(items)
        elif request.args['filter'] == 'highest price':
            # Here I make the query using order by price desc
            items = new_session.query(Acessories).order_by(Acessories.price.desc()).all()
            new_session.close()
            return serialize_objects(items)
        else:
            # Here I make the default query
            items = new_session.query(Acessories).all()
            new_session.close()
            return serialize_objects(items)
            # Note that after each query the session is closed
    except:
        items = new_session.query(Acessories).all()
        new_session.close()
        return serialize_objects(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)

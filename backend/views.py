from models import *
from models import sectionList

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


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f'sqlite:///{BASE_DIR}/database.db')
Session = sessionmaker(bind=engine)

@app.route('/api/products/<section>/<sku>', methods=['GET'])
def find_one_item(section, sku):
    new_session = Session()
    if section in sectionList:
        section = eval( section )
        query = (
            new_session.query(section)
            .filter_by(sku = sku)
            .one_or_none()
        )
        if query != None:
            return serialize_object(query)
    return {'message': 'Item not found.'}

# @app.route('/shippingoptions/<int:qtd>')
# def shipping_options(qtd):
#     base_price = 9.99
#     subprice   = floor(qtd/10)*base_price
#     current_date = datetime(
#         year=time.localtime().tm_year,
#         month=time.localtime().tm_mon,
#         day=time.localtime().tm_mday
#     )
#     return (json.dumps([
#         {'type':'Normal', 'price': subprice, 'arrives': f'{(current_date+timedelta(days=20)).day}/{(current_date+timedelta(days=20)).month}'},
#         {'type':'Fast', 'price': subprice*2, 'arrives': f'{(current_date+timedelta(days=5)).day}/{(current_date+timedelta(days=5)).month}'},
#         {'type':'Real fast', 'price': subprice*5, 'arrives': f'{(current_date+timedelta(days=1)).day}/{(current_date+timedelta(days=1)).month}'},
#     ]))


@app.route('/api/products', methods=['GET'])
def get_products():
    # Here I initiate a session
    new_session = Session()
    try:
        # Received section is the name of the table. This is filtered for security.
        section      = request.args['section']
        used_filter  = request.args['filter']
        qtd_per_page = request.args['qtd_per_page']
        current_page = int( request.args['page'] )

        # First and last item to be shown
        fshown = current_page - 1
        lshown = current_page * 10

        # This is for security
        if section not in sectionList:
            return {'message': 'Bad Request.'}

        if used_filter == 'lowest_price':
            # Here I make the query using order by price asc
            query = new_session.query( eval(section) )
            .order_by(
                MenClothes
                .price
                .asc()
            )
            .all()[ fshown : lshown ]
            new_session.close()
            return serialize_objects(query)

        elif request.args['filter'] == 'highest_price':
            # Here I make the query using order by price desc
            query = new_session.query( eval(section) )
            .order_by(
                MenClothes
                .price
                .desc()
            )
            .all()[ fshown : lshown ]
            new_session.close()
            return serialize_objects(query)
            
        else:
            # Here I make the default query
            query = new_session.query( eval(section) )
            .all()[ fshown : lshown ]
            new_session.close()
            return serialize_objects(query)
            # Note that after each query the session is closed
    except:
        return {'message': 'Bad Request.'}

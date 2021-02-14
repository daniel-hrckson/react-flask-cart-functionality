from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import sectionList
from unittest import TestCase
from flask import jsonify
from app import BASE_DIR, host, port
import requests
from utilities import serialize_objects, serialize_object
from models import *
import unittest

class Test_Api(TestCase):
    def setUp(self):
        self.BASE_DIR = BASE_DIR
        self.engine = create_engine(f'sqlite:///{self.BASE_DIR}/database.db')
        self.Session = sessionmaker(bind=self.engine)
        self.baseUrl = 'http://{}:{}'.format(host, port)
        self.new_session = self.Session()


    def test_get_menClothes_by_lowest_price(self, page=1, qtd_per_page=10):
        fshown = (page - 1) * qtd_per_page
        lshown = page * qtd_per_page
        query = (self.new_session.query( MenClothes ).order_by(
                MenClothes
                .price
                .asc()
            )
            .all()[ fshown : lshown ]
        )
        self.new_session.close()
        res = requests.get(
            '{}/api/products?section={}&filter={}&qtd_per_page={}&page={}'.format(
                self.baseUrl, 'MenClothes', 'lowest_price', qtd_per_page, page
            ) 
        )

        self.assertEqual( res.status_code, 200 )
        self.assertEqual( res.json()['products']['0'], serialize_objects(query)[0] )
        self.assertEqual( len(res.json()['products']), qtd_per_page )
        

    def test_get_menClothes_by_highest_price(self, page=1, qtd_per_page=10):
        fshown = (page - 1) * qtd_per_page
        lshown = page * qtd_per_page
        query = (self.new_session.query( MenClothes ).order_by(
                MenClothes
                .price
                .desc()
            )
            .all()[ fshown : lshown ]
        )
        self.new_session.close()
        res = requests.get(
            '{}/api/products?section={}&filter={}&qtd_per_page={}&page={}'.format(
                self.baseUrl, 'MenClothes', 'highest_price', qtd_per_page, page
            ) 
        )

        self.assertEqual( res.status_code, 200 )
        self.assertEqual( res.json()['products']['0'], serialize_objects(query)[0] )
        self.assertEqual( len(res.json()['products']), qtd_per_page )

    def test_get_menClothes_pagination(self, page=1, qtd_per_page=[5,10,20]):
        for x in qtd_per_page:
            fshown = (page - 1) * x
            lshown = page * x

            query = self.new_session.query( MenClothes ).all()[ fshown : lshown ]
            
            res = requests.get(
                '{}/api/products?section={}&filter={}&qtd_per_page={}&page={}'.format(
                    self.baseUrl, 'MenClothes', 'relevance', x, page
                ) 
            )

            self.assertEqual(res.status_code, 200)
            self.assertEqual(len(res.json()['products']), x)

        self.new_session.close()


    def test_get_womenClothes_by_lowest_price(self, page=1, qtd_per_page=10):
        fshown = (page - 1) * qtd_per_page
        lshown = page * qtd_per_page
        query = (self.new_session.query( WomenClothes ).order_by(
                WomenClothes
                .price
                .asc()
            )
            .all()[ fshown : lshown ]
        )
        self.new_session.close()
        res = requests.get(
            '{}/api/products?section={}&filter={}&qtd_per_page={}&page={}'.format(
                self.baseUrl, 'WomenClothes', 'lowest_price', qtd_per_page, page
            ) 
        )

        self.assertEqual( res.status_code, 200 )
        self.assertEqual( res.json()['products']['0'], serialize_objects(query)[0] )
        self.assertEqual( len(res.json()['products']), qtd_per_page )

    def test_get_womenClothes_by_highest_price(self, page=1, qtd_per_page=10):
        fshown = (page - 1) * qtd_per_page
        lshown = page * qtd_per_page
        query = (self.new_session.query( WomenClothes ).order_by(
                WomenClothes
                .price
                .desc()
            )
            .all()[ fshown : lshown ]
        )
        self.new_session.close()
        res = requests.get(
            '{}/api/products?section={}&filter={}&qtd_per_page={}&page={}'.format(
                self.baseUrl, 'WomenClothes', 'highest_price', qtd_per_page, page
            ) 
        )

        self.assertEqual( res.status_code, 200 )
        self.assertEqual( res.json()['products']['0'], serialize_objects(query)[0] )
        self.assertEqual( len(res.json()['products']), qtd_per_page )

    def test_get_womenClothes_pagination(self, page=1, qtd_per_page=[5,10,20]):
        for x in qtd_per_page:
            fshown = (page - 1) * x
            lshown = page * x

            query = self.new_session.query( WomenClothes ).all()[ fshown : lshown ]
            
            res = requests.get(
                '{}/api/products?section={}&filter={}&qtd_per_page={}&page={}'.format(
                    self.baseUrl, 'WomenClothes', 'relevance', x, page
                ) 
            )

            self.assertEqual(res.status_code, 200)
            self.assertEqual(len(res.json()['products']), x)

        self.new_session.close()

    def test_get_specific_product(self):
        items_to_find = [
            (WomenClothes, 12664693),
            (WomenClothes, 13874454),
            (MenClothes, 13404539),
            (Acessories, 13888978001),
        ]
        for x in items_to_find:
            query = (
                self.new_session.query(x[0])
                .filter_by(sku = x[1])
                .one_or_none()
            )
            res = requests.get(
                '{}/api/products/{}/{}'.format(
                        self.baseUrl, x[0].__name__, x[1]
                    ) 
                )
            self.assertEqual(res.status_code, 200)
            self.assertEqual(serialize_object(query), res.json())
        self.new_session.close()


    def test_get_Acessories_by_lowest_price(self, page=1, qtd_per_page=10):
        fshown = (page - 1) * qtd_per_page
        lshown = page * qtd_per_page
        query = (self.new_session.query( Acessories ).order_by(
                Acessories
                .price
                .asc()
            )
            .all()[ fshown : lshown ]
        )
        self.new_session.close()
        res = requests.get(
            '{}/api/products?section={}&filter={}&qtd_per_page={}&page={}'.format(
                self.baseUrl, 'Acessories', 'lowest_price', qtd_per_page, page
            ) 
        )
        self.assertEqual( res.status_code, 200 )
        self.assertEqual( res.json()['products']['0'], serialize_objects(query)[0] )
        self.assertEqual( len(res.json()['products']), qtd_per_page )

    def test_get_Acessories_by_highest_price(self, page=1, qtd_per_page=10):
        fshown = (page - 1) * qtd_per_page
        lshown = page * qtd_per_page
        query = (self.new_session.query( Acessories ).order_by(
                Acessories
                .price
                .desc()
            )
            .all()[ fshown : lshown ]
        )
        self.new_session.close()
        res = requests.get(
            '{}/api/products?section={}&filter={}&qtd_per_page={}&page={}'.format(
                self.baseUrl, 'Acessories', 'highest_price', qtd_per_page, page
            ) 
        )
        self.assertEqual( res.status_code, 200 )
        self.assertEqual( res.json()['products']['0'], serialize_objects(query)[0] )
        self.assertEqual( len(res.json()['products']), qtd_per_page )

    def test_get_womenClothes_pagination(self, page=1, qtd_per_page=[5,10,20]):
        for x in qtd_per_page:
            fshown = (page - 1) * x
            lshown = page * x
            query = self.new_session.query( Acessories ).all()[ fshown : lshown ]
            self.new_session.close()
            res = requests.get(
                '{}/api/products?section={}&filter={}&qtd_per_page={}&page={}'.format(
                    self.baseUrl, 'Acessories', 'relevance', x, page
                ) 
            )
            self.assertEqual(res.status_code, 200)
            self.assertEqual(len(res.json()['products']), x)

if __name__ == '__main__':
    unittest.main()

    
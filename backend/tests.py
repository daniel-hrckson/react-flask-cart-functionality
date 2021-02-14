from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import sectionList
from unittest import TestCase
from flask import jsonify
from app import BASE_DIR
import utilities
from models import *
import unittest

class Test_Api(TestCase):
    def setUp(self):
        self.BASE_DIR = BASE_DIR
        self.engine = create_engine(f'sqlite:///{self.BASE_DIR}/database.db')
        self.Session = sessionmaker(bind=self.engine)


    def test_get_menClothes_by_lowest_price_asc(self):
        new_session = self.Session()
        query = utilities.serialize_objects(
            new_session.query(MenClothes)
            .order_by(MenClothes.price.asc())
            .limit(10).all()
        )  
        total_query_results = len(query)
        self.assertEqual(11, total_query_results)
        

    def test_get_menClothes_by_lowest_price_dsc(self):
        pass

    def test_get_menClothes_5_10_20_items_per_page(self):
        pass

    def test_get_womenClothes_by_lowest_price_asc(self):
        pass

    def test_get_womenClothes_by_lowest_price_dsc(self):
        pass

    def test_get_womenClothes_5_10_20_items_per_page(self):
        pass

    def test_get_specific_product(self):
        pass

if __name__ == '__main__':
    unittest.main()

    
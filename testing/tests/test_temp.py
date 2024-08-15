from unittest import TestCase

from apptree.prefetch_filter import prefetch_and_filter
from testing.tests.test_load_db import Load_Tree_TestCase


class Temp_TestCase(TestCase):
    '''    python manage.py test testing.tests.test_temp '''

    def setUp(self):
        print("setup test.... ")
        load = Load_Tree_TestCase()
        load.test_load_test_db()

    def test_temp(self):
        prefetch_and_filter("tree2", 230)

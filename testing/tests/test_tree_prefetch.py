from django.test import TestCase

from apptree.models import Tree
from testing.tests.test_load_db import Load_Tree_TestCase


#   to Run:::: - >  python manage.py test testing.tests.test_tree_prefetch
# cle
# sys.stdout = open('C:/Users/Public/py_dev/django/muks/others/output_files/outx.txt', 'w')
class Tree_list_TestCase(TestCase):
    def setUp(self):
        load = Load_Tree_TestCase()
        load.test_load_test_db()

    def test_tree_list(self):
        print("start testing")
        # tree_qs = Tree.objects.filter(name="name2").prefetch_related('branchesfrk__branchleafgroupfrk__groupleafs')
        tree_qs = (Tree.objects.filter(name="tree1")
                   .prefetch_related('branchesfrk__branchleafgroupfrk__groupleafs'))
        tree_qs = Tree.objects.filter(name="tree2").prefetch_related('branchesfrk__branchleafgroupfrk__groupleafs')
        # print("tree_qs:", tree_qs)
        for tree in tree_qs:
            print("tree-name:", tree.name)
            print("tree-orgination:", tree.orgination)
            print("tree.branchesfrk.name:", tree.branchesfrk.name)
            print("tree.branchesfrk.length:", tree.branchesfrk.length)

            # print("tree.branchesfrk.branchleafgroupfrk.prefetch_related for 'leafs_set====", tree.branchesfrk.branchleafgroupfrk.prefetch_related('leafs_set'))
            print("tree.branchesfrk.branchleafgroupfrk.group_leafs_name====",
                  tree.branchesfrk.branchleafgroupfrk.groupLeafsName,
                  "tree.branchesfrk.branchleafgroupfrk.Description====",  # prefetch_related('leafs_set')
                  tree.branchesfrk.branchleafgroupfrk.Description)
            lis = [("leafName:", leaf.name, "leafNoOfpaper:", leaf.noOfpaper) for leaf in
                   tree.branchesfrk.branchleafgroupfrk.groupleafs.all() if leaf.noOfpaper > 100]
            print("lis\n", lis)
            '''
            for leaf in tree.branchesfrk.branchleafgroupfrk.groupleafs.all(): #this is related name to get leafs from group_leaf
                print("leafName:", leaf.name, "leafNoOfpaper:",leaf.noOfpaper)
            '''

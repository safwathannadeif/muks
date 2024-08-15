from pprint import pprint

from django.test import TestCase
from apptree.models import Tree
from testing.tests.test_load_db import Load_Tree_TestCase


# Run::  ++++>  python manage.py test testing.tests.test_prefetch2_filter2
# from  Stack Overflow
# https://stackoverflow.com/questions/12973929/why-does-djangos-prefetch-related-only-work-with-all-and-not-filter/12974801#12974801
class Tree_list_leaf_TestCase(TestCase):
    def setUp(self):
        load = Load_Tree_TestCase()
        load.test_load_test_db()

    def test_tree_list(self):
        tree_qs = Tree.objects.filter(name="tree2").prefetch_related('branchesfrk__branchleafgroupfrk__groupleafs')
        for tree in tree_qs:
            # out =  [ (tree.name,tree.branchesfrk.name, tree.branchesfrk.branchleafgroupfrk,tree.branchesfrk.branchleafgroupfrk.groupleafs.all())  for l in tree.branchesfrk.branchleafgroupfrk.groupleafs.all() if l.noOfpaper > 150]
            # out = [(tree.name,tree.orgination, tree.branchesfrk.name, tree.branchesfrk.branchleafgroupfrk.groupLeafsName,
            #        tree.branchesfrk.branchleafgroupfrk.groupleafs.all()[:]) for l in tree.branchesfrk.branchleafgroupfrk.groupleafs.all() if l.noOfpaper >22]

            out = [
                (tree.name, tree.orgination, tree.branchesfrk.name, tree.branchesfrk.branchleafgroupfrk.groupLeafsName)
                for l in tree.branchesfrk.branchleafgroupfrk.groupleafs.all() if l.noOfpaper == 174]

        pprint(out)

        '''
        someAlbums = PhotoAlbum.objects.filter(author="Davey Jones").prefetch_related("photo_set")
        for a in someAlbums:
        somePhotos = [p for p in a.photo_set.all() if p.format == 1]
	----------------------------------------------------------------------------------------------
        
        
        This one works only for one prefetch entity ie "branchesfrk" works
        but composed "branchesfrk__branchleafgroupfrk__groupleafs" NOT worked
        https: // stackoverflow.com / questions / 12973929 / why - does - djangos - prefetch - related - only - work -
        with-all - and -not -filter / 12974801  # 12974801

        filterBranch = Branch.objects.filter(length__gt=30)

        prefetch2 = Prefetch("branchesfrk__branchleafgroupfrk__groupleafs", queryset=filterBranch,
                             to_attr="filterBranchAttr")




        Tree.objects.prefetch_related(prefetch2).get().filterBranchAttr


        qs2 = Tree.objects.filter(name="tree2").prefetch_related(
            prefetch2).get().branchesfrk__branchleafgroupfrk__groupleafs.all()
        '''

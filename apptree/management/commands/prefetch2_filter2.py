from pprint import pprint

from django.core.management.base import BaseCommand

from apptree.json4tree import MkTreeJson
from apptree.models import GrpLeafs,Leafs,Branch,Tree
'''
Run:::   ->>>  python manage.py prefetch2_filter2
'''

class Command(BaseCommand):
      def handle(self, *args, **options):
          mkTreeJson = MkTreeJson()
          # straight forward
          print("start testing")
          out_all= []
          tree_qs = (Tree.objects.filter(name="tree2")
                     .prefetch_related('branchesfrk__branchleafgroupfrk__groupleafs'))
          #tree_qs = Tree.objects.prefetch_related('branchesfrk__branchleafgroupfrk__groupleafs')
          for tree in tree_qs:
              # out =  [ (tree.name,tree.branchesfrk.name, tree.branchesfrk.branchleafgroupfrk,tree.branchesfrk.branchleafgroupfrk.groupleafs.all())  for l in tree.branchesfrk.branchleafgroupfrk.groupleafs.all() if l.noOfpaper > 150]
              # out = [(tree.name,tree.orgination, tree.branchesfrk.name, tree.branchesfrk.branchleafgroupfrk.groupLeafsName,
              #        tree.branchesfrk.branchleafgroupfrk.groupleafs.all()[:]) for l in tree.branchesfrk.branchleafgroupfrk.groupleafs.all() if l.noOfpaper >22]

              out = (tree.name, tree.orgination, tree.branchesfrk.name,
                      tree.branchesfrk.branchleafgroupfrk.groupLeafsName)

              mkTreeJson.add_barnch(tree.name,tree.orgination,tree.branchesfrk.name,tree.branchesfrk.length)
                      #tree.branchesfrk.branchleafgroupfrk.groupleafs.all()[0:] )
                      #for b in tree.branchesfrk.all() if b.length > 30
                     #for l in tree.branchesfrk.branchleafgroupfrk.groupleafs.all() if l.noOfpaper >200

              out_leaf_lis= [({"name":leaf.name,"noOfpaper":leaf.noOfpaper}) for leaf in
               tree.branchesfrk.branchleafgroupfrk.groupleafs.all() if leaf.noOfpaper > 230 ]
              mkTreeJson.add_leaf_grp(out_leaf_lis,tree.branchesfrk.branchleafgroupfrk.groupLeafsName,
                                                   tree.branchesfrk.branchleafgroupfrk.Description)
              #####                 out_all.append(out)
              # pprint(out)
              #print("Outleaflis:", out_leaf_lis)
          mkTreeJson.end_json()
from django.core.management.base import BaseCommand
from apptree.models import GrpLeafs,Leafs,Branch,Tree
'''
Run:::   ->>>  python manage.py reverse_grp_leaf
'''

class Command(BaseCommand):
      def handle(self, *args, **options):
          # straight forward
          print("start testing")
          leaf_with_frkey = Leafs.objects.all()     #SELECT "apptree_grpleafs"."id", "apptree_grpleafs"."groupLeafsName", "apptree_grpleafs"."Description" FROM "apptree_grpleafs"


          for lf in leaf_with_frkey:
              ## print("ForwardFromFkey:",  lf.leafgroupfrk,lf.noOfpaper)
              # #### forward group attributes from Leaf Foreign key #### #
              ## Pass it it works
              pass

          grp_Of_leaf_qs = GrpLeafs.objects.prefetch_related('groupleafs')
          '''
            SELECT "apptree_leafs"."id", "apptree_leafs"."name", "apptree_leafs"."noOfpaper", "apptree_leafs"."leafgroupfrk_id" FROM "apptree_leafs" WHERE "apptree_leafs"."leafgroupfrk_id" = 65 
          '''
          print(grp_Of_leaf_qs.query)
          for grp in grp_Of_leaf_qs:
              grpName = grp.groupLeafsName
              print("Group====>", grpName)
              leaf_from_one_grp_qs = grp.groupleafs.all()  # prefetch_related to make reverse:
              print(leaf_from_one_grp_qs.query)
              ### the main purpose of related_name is the reverse FRKEY
              #### # reverse Django here means get the leafs attributes from Group table using group related_namewithout any hit for the database
              #### # forward Django means from frkey get the attributes from the primary table/GrpLeafs

              for lf in leaf_from_one_grp_qs:
                  print("Leaf====>", lf.name, "->", lf.noOfpaper)

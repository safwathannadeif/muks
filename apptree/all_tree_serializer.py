from apptree.models import GrpLeafs,Leafs,Branch,Tree

from rest_framework import serializers

'''
name with "-" casue a problem no_of_paper
'''
class LeafsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leafs
        fields = ("name","noOfpaper")           ## ,"noOfpaper"

class Grp_LeafsSerializer(serializers.ModelSerializer):
    groupleafs=LeafsSerializer(many=True)
    class Meta:
        model = GrpLeafs
        fields = ('groupLeafsName', 'Description','groupleafs', )

class BranchSerializer(serializers.ModelSerializer):
    #selections = SelectionSerializer(many=True)
    branchleafgroupfrk=Grp_LeafsSerializer()
    class Meta:
        model = Branch
        fields = ('id','name','length','branchleafgroupfrk')

class TreeSerializer(serializers.ModelSerializer):
    branchesfrk  = BranchSerializer()
    #market = MarketSerializer()
    class Meta:
        model = Tree
        fields = ( 'name', 'orgination','branchesfrk')
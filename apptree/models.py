from django.db import models


class GrpLeafs(models.Model):
    groupLeafsName = models.CharField(max_length=27)
    Description = models.CharField(max_length=37)

    class Meta:
        indexes = [
            models.Index(fields=["groupLeafsName"])
        ]

    def __str__(self):
        return self.groupLeafsName


class Leafs(models.Model):
    name = models.CharField(max_length=27)
    noOfpaper = models.IntegerField()
    leafgroupfrk = models.ForeignKey(GrpLeafs, related_name="groupleafs",
                                     null=True, blank=True,
                                     on_delete=models.CASCADE)  # leaf to grp leafs

    class Meta:
        indexes = [
            models.Index(fields=["name"])
        ]

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=27)
    length = models.IntegerField()
    branchleafgroupfrk = models.ForeignKey(GrpLeafs, on_delete=models.CASCADE)  # branch to grp leafs

    class Meta:
        indexes = [
            models.Index(fields=["name"])
        ]

    def __str__(self):
        return self.name


class Tree(models.Model):
    name = models.CharField(max_length=27)
    orgination = models.CharField(max_length=37)
    branchesfrk = models.ForeignKey(Branch, on_delete=models.CASCADE)  # tree to branches

    class Meta:
        indexes = [
            models.Index(fields=["name"])
        ]

    def __str__(self):
        return self.name

# branchesfrk__branchleafgroupfrk__groupleafs

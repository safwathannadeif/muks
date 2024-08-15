import json


class MkTreeJson():
    all = []
    cur_tree_name = ""
    cur_branch_name = ""
    cur_tree = {}
    lis_of_branches = []

    def add_barnch(self, tree_name, orgination, branch_name, branch_length):
        if tree_name != self.cur_tree_name:
            self.cur_tree_name = tree_name
            self.cur_tree = {}  ## new tree
            self.cur_tree["name"] = tree_name
            self.cur_tree["orgination"] = orgination
            self.cur_tree["branchesfrk"] = self.lis_of_branches
            self.all.append(self.cur_tree)

        if branch_name != self.cur_branch_name:
            self.cur_branch_name = branch_name
            self.cur_branch = {}  ## new branch
        self.cur_branch["name"] = branch_name
        self.cur_branch["length"] = branch_length
        self.lis_of_branches.append(self.cur_branch)

    def add_leaf_grp(self, lis_of_leafs, grpleaf_name, grp_description):
        # lis_of_leafs.append({"grp_name:",grpleaf_name})
        self.cur_branch["groupLeafsName"] = grpleaf_name
        self.cur_branch["Description"] = grp_description
        self.cur_branch["groupleafs"] = lis_of_leafs

    def end_json(self):
        print(json.dumps(self.all, indent=2))

    def get_all(self):
        return self.all

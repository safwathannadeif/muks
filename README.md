Django multiple-forgined keys CRUD Models:

A tree is a natural one to many relationship chains. One Tree >>Many Branches>> One Branch, Many Group Of Leafs >> One Group Many Leafs.
Of curses, there are many trees. Tree Visual Model: https://github.com/user-attachments/assets/e5345295-8740-4d7d-ab45-65b5389bc867
Django Model: Classes:  

  
GrpLeafs,
  
Leafs with ForeignKey=GrpLeafs and related_name=groupleafs,
  
Branch with ForeignKey=GrpLeafs, 
  
Tree with ForeignKey=Branch
  
Please refer to the model classes to see the details. 

Prefetch is used such that one hit to the database makes the query for all the hierarchy. 

Creating a tree requires a specific order to handle the dependencies. e.g., creating a leaf requires the foreign key for the group, and creating a tree requires the foreign key for the branch. 
The API to create a tree with its associated elements utilizes the Django special parser to facilitate the creation with the proper dependency.
 
Views and Urls:

tree_api/create_tree/				create_tree_view2.Create_tree_B64.as_view() ,

tree_api/all_tree/				all_tree_viewset.Tree_ALL_View.as_view({"get":"get_all"})) ,

tree_api/filter_tree/ 				all_tree_viewset.Tree_ALL_View.as_view({"get":"get_with_filter"})) ,

tree_api/del_leafs				all_tree_viewset.Tree_ALL_View.as_view({"post":"do_del_leafs"})) ,

tree_api/upd_branch/				all_tree_viewset.Tree_ALL_View.as_view({"post":"do_upd_branch"}))

Client APIs side: https://github.com/safwathannadeif/httpxcli

from circle_test import *
from params import params

root_data = "/mnt/c/Users/bennm/Documents/UNI/Year3/Modelling Tissues Project/data"
project_name = "pyABP_delta_tests"
folder_name = f"{root_data}/{project_name}"
search_grid = pickle.load(open(f"{root_data}/{project_name}/search_grid.p","rb"))
simulation(folder_name,search_grid,params)

# k2s = [0.4]
# epsilons = [0.05] 
# params["inter_type"] = 1
# # k2s = [0.4,0.8,1.2,1.6,2]
# # epsilons = [0.05,0.1,0.15,0.2,0.25,0.3] 
# for k2 in k2s:
# 	for epsilon in epsilons:
# 		params["k2"] = k2
# 		params["epsilon"] = epsilon
# 		folder_name = f"./data/pyABP_k2_{k2}_ep_{epsilon}"
# 		circle_test(params,folder_name)
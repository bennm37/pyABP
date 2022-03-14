from interaction_test import interaction_test
from circle_test import *
n_delta,n_ep = 2,2
delta_range,ep_range  = (0,2),(0.05,1)
epsilon,delta = make_param_lists(ep_range,delta_range,n_ep,n_delta)
search_grid = make_search_grid(["epsilon","delta"],[epsilon,delta],True)
search_grid = [list(row) for row in search_grid]

for row in search_grid:
    for dict in row:
        f_name = get_parameter_suffix(dict)
        root_data = "/mnt/c/Users/bennm/Documents/UNI/Year3/Modelling Tissues Project/data"
        folder_name = f"{root_data}/interaction_test/{f_name}"
        try:
            os.mkdir(folder_name)
        except FileExistsError:
            shutil.rmtree(folder_name)
            os.mkdir(folder_name)
        p = params.copy()
        interaction_test(dict["delta"],dict["epsilon"],folder_name)
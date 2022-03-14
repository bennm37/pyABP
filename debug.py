# Debugging ABP script
# Where to look for the module:
import sys
sys.path.append("./build") 
import os
import shutil
import pyABP

#// geometry and size
#int N; // Number of particles
#double L; // system size

#// dynamics
#double dt; // time step
#int Nsteps; // number of time steps
#int freq; // saving frequency
#int seed; // RNG seed

#// ABPs
#double mu; // mobility
#double Dr; // rotational diffusion constant
#double v0; // self-propulsion velocity
#// Interaction
#double k; // interaction stiffness
#double poly; // polydispersity

#// options
#bool saveText; // save as text file
#bool saveVTK; // save as vtk file
##TODO make sure this lines up with python dictionary on analysis end
params={}
# system
params["N"]=2000
params["L"]= 100.0

# dynamics
params["dt"]=0.01
params["seed"]=1

# ABPs
params["mu"]=1.0
params["Dr"]=0.001
params["v0"]=0.1
#// Interaction
params["k"]= 1.0
params["epsilon"]=0.15
params["poly"]=0.2
## repulsion is 0,  k2 is 1, delta is 2
params["inter_type"]= 2
params["k2"]=1
params["delta"]=1

# C++ internal: debugging output?
params["verbose"]=False

# Python script options only
params["Nsteps"]=50
params["freq"]=100
params["saveText"]=True
params["saveVTK"]=True

print(params)

# set up system
thisSystem = pyABP.System(params)
# run system
nsave = int(params["Nsteps"]/params["freq"])

# make test output directory. Delete previous version first
k = params["k"]
folder_name = f"data/pyABP_k2_bh_test"
try:
	os.mkdir(folder_name)
except FileExistsError:
	shutil.rmtree(folder_name)
	os.mkdir(folder_name)

for i in range(nsave):
	thisSystem.step(params["freq"])
	filename1 = folder_name +'/data'+str(i)+'.dat'
	filename2 = folder_name +'/data'+str(i)+'.vtp'
	# void output(string filename, bool _saveText, bool _saveVTP);
	thisSystem.output(filename1,filename2,params["saveText"],params["saveVTK"])
	print("Ran and saved after " + str(params["freq"]) + " steps, total at " + str((i+1)*params["freq"]))

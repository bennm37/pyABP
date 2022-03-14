params={}
# system
params["N"]=2000
params["L"]= 200.0

# dynamics
params["dt"]=0.01
params["seed"]=1

# ABPs
params["mu"]=1.0
params["Dr"]=0.1
params["v0"]=0.1
#// Interaction
params["k"]= 1.0
params["epsilon"]=0.15
params["poly"]=0.2
## repulsion is 0,  k2 is 1, delta is 2
params["inter_type"]=2
params["k2"]=1
params["delta"]=1

# C++ internal: debugging output?
params["verbose"]=False

# Python script options only
params["Nsteps"]=500000
params["freq"]=1000
params["saveText"]=True
params["saveVTK"]=True
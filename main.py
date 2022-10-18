# the tutorial link explaining this code (made by Mike Saint-Antoine):
# https://www.youtube.com/watch?v=jVDcRqzJIJk&list=PLWVKUEZ25V94kdT2Lh97KqB9MoLV9ZzmU&index=3



# An Overview of the 2 ODEs:

# ————————————————————————————————————————————————
#   dmdt = k_m - gamma_m * m
#   dpdt = k_p * m - gamma_p * p
# ————————————————————————————————————————————————


# ——————— the variables ——————————————————————————
# m: mRNA
# k_m: mRNA concentration
# gamma_m: rate of mRNA degradation

# p: protein
# k_p: protein concentration
# gamma_p: rate of protein degradation


# ——————— the meaning ————————————————————————————
# {the amount of mRNA over time}  =  {amount of mRNA  -  (mRNA degrading rate  *  amount of mRNA)}
# {the amount of protein over time}  =  {(amount of protein  *  amount of mRNA)  -  (protein degrading rate  *  amount of protein)}



# ——————— the code ————————————————————————————

# inital conditions:
y0 = [0,0] # 0 mRNA, 0 protein

# variables:
t = np.linspace(0,200,num=100) # time
k_m = 0.2 # mRNA concentration
gamma_m = 0.05 # rate of mRNA degradation
k_p = 0.4 # protein concentration
gamma_p = 0.1 # rate of protein degradation

params = [k_m, gamma_m, k_p, gamma_p]


def sim(variables, t, params):

    m = variables[0] # mRNA
    p = variables[1] # protein

    k_m = params[0]
    gamma_m = params[1]
    k_p = params[2]
    gamma_p = params[3]

    dmdt = k_m - gamma_m * m # ODE 1
    dpdt = k_p * m - gamma_p * p # ODE 2

    return([dmdt,dpdt]) # return variables in the same order as they were passed in


# run ODE
y = odeint(sim, y0, t, args=(params,))

# create plot
f,ax = plt.subplots(1)

line1, = ax.plot(t,y[:,0], color="b", label="M") # all rows in column 1
line2, = ax.plot(t,y[:,1], color="r", label="P") # all rows in column 2

ax.set_ylabel("Abundance")
ax.set_xlabel("Time")

ax.legend(handles=[line1,line2])
plt.show()

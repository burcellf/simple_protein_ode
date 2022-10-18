### This script is an example of how to model simple protein and mRNA levels
the [tutorial](https://www.youtube.com/watch?v=jVDcRqzJIJk&list=PLWVKUEZ25V94kdT2Lh97KqB9MoLV9ZzmU&index=3) link explaining this code (made by Mike Saint-Antoine)
<br><br>


### An Overview of the 2 ODEs:

  dm/dt = k_m - gamma_m * m   <br>
  dp/dt = k_p * m - gamma_p * p

<br>

### the variables
m: mRNA
k_m: mRNA concentration
gamma_m: rate of mRNA degradation

p: protein
k_p: protein concentration
gamma_p: rate of protein degradation

<br>

### the meaning
{the amount of mRNA over time}  =  {amount of mRNA  -  (mRNA degrading rate  *  amount of mRNA)}  <br>
{the amount of protein over time}  =  {(amount of protein  *  amount of mRNA)  -  (protein degrading rate  *  amount of protein)}

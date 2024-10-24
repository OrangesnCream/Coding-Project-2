"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt


fname = "sample_data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
direct_time = df[var_names[1]].values.tolist()
vector_time = df[var_names[2]].values.tolist()
indirect_time = df[var_names[3]].values.tolist()

plt.title("Comparison of 3 Codes")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

# here, we are plotting the raw values read from the input .csv file, which
# we interpret as being "time" that maps directly to the y-axis.
#
# what if we want to plot MFLOPS instead? How do we compute MFLOPS from
# time and problem size? You may need to add some code here to compute
# MFLOPS, then modify the plt.plot() lines below to plot MFLOPS rather than time.

print("Choose what to plot 0=MFLOPS, 1=Bandwith, 2=latency, anything else is just time")
input1 = int(input())
print("var names =", input1)

if(input1==0):
    plt.title("Comparison of 3 Sum methods: Perlmutter CPU Node")
    for index, time in enumerate(direct_time):
        print("time=", time)
        direct_time[index]=(problem_sizes[index]/1000000)/time
        print("mflops =", direct_time[index])
    for index, time in enumerate(vector_time):
        print("time=", time)
        vector_time[index]=(problem_sizes[index]/1000000)/time
        print("mflops =", vector_time[index])
    for index, time in enumerate(indirect_time):
        print("time=", time)
        indirect_time[index]=(problem_sizes[index]/1000000)/time
        print("mflops =",indirect_time[index])
    plt.xlabel("Problem Sizes")
    plt.ylabel("MFLOP/s")
    plt.yscale("log")
elif(input1==1):
    plt.title("Comparison of 3 Sum methods: Perlmutter CPU Node")
    for index, time in enumerate(direct_time):
        print("time=", time)
        direct_time[index]=((((problem_sizes[index]*0)/1000000000)/time)/204.8)*100
        print("mflops =", direct_time[index])
    for index, time in enumerate(vector_time):
        print("time=", time)
        vector_time[index]=((((problem_sizes[index]*2)/1000000000)/time)/204.8)*100
        print("mflops =", vector_time[index])
    for index, time in enumerate(indirect_time):
        print("time=", time)
        indirect_time[index]=((((problem_sizes[index]*4)/1000000000)/time)/204.8)*100
        print("mflops =",indirect_time[index])
    plt.xlabel("Problem Sizes")
    plt.ylabel("percentage of Bandwidth used(0.0 to 100.0)")
elif(input1==2):
    plt.title("Comparison of 3 Sum methods: Perlmutter CPU Node")
    for index, time in enumerate(direct_time):
        print("time=", time)
        direct_time[index]=0
        print("mflops =", direct_time[index])
    for index, time in enumerate(vector_time):
        print("time=", time)
        vector_time[index]=(time*1000000000)/(problem_sizes[index]*2)
        print("mflops =", vector_time[index])
    for index, time in enumerate(indirect_time):
        print("time=", time)
        indirect_time[index]=(time*1000000000)/(problem_sizes[index]*4)
        print("mflops =",indirect_time[index])
    plt.xlabel("Problem Sizes")
    plt.ylabel("Latency nanoseconds/bytes")
    
else:
    plt.xlabel("Problem Sizes")
    plt.ylabel("runtime")


plt.plot(direct_time, "r-o")
plt.plot(vector_time, "b-x")
plt.plot(indirect_time, "g-^")

#plt.xscale("log")



varNames = [var_names[1], var_names[2], var_names[3]]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.show()

# EOF

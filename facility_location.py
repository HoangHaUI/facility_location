import pandas as pd
import gurobipy as gp
from gurobipy import GRB
import numpy as np
import os
import matplotlib.pyplot as plt


try:
    os.remove("result.txt")
except:
    pass

PROVINCE_NUMBER = 25
BUDGET = np.arange(5, 15)

# Read data from csv file
coverages = pd.read_csv("data/coverages.csv")
population = pd.read_csv("data/population_cost.csv")

def inference(province_num):

    list_tinh = list()
    data = coverages[["ID", "Coverage"]].set_index(
        "ID").join(population.set_index("id"), on="ID")
    data = data.reset_index(False)
    data = data[["ID", "Coverage", "provice", "population", "cost"]]
    coverages[:3], population[:3], data[:3]

    data_np = data.to_numpy()
    data_np[:3]

    city_ = data_np[:, 0][:province_num]
    coverage_ = data_np[:, 1][:province_num]
    cost_ = data_np[:, 4][:province_num]
    city_[:5], coverage_[:5], cost_[:15]

    input_data = {}
    for i in range(len(cost_)):
        coverage_arr = []
        try:
            coverage_arr = np.array(coverage_[i].split(", "), dtype=int)
        except:
            coverage_arr = []
        ele = [{cov for cov in coverage_arr}, cost_[i]]
        input_data[i] = ele

    city, coverage, cost = gp.multidict(input_data)

    m = gp.Model("set_covering1")

    build = m.addVars(len(city), vtype=GRB.BINARY, name="build")
    m.addConstrs((gp.quicksum(
        build[r] for r in city if r in coverage[t]) >= 1 for t in city), name="Build2cover")
    m.setObjective(gp.quicksum(build[t] for t in city), GRB.MINIMIZE)
    m.update()
    m.write("set_covering1.lp")
    m.optimize()
    try:
        print(f"Finish result of value: ")
        for ct in build.keys():
            
            if (abs(build[ct].x) > 1e-6):
                print(f"\n Setup a Kho Lien Vung in city {ct}")
                with open("result.txt", 'a') as f:
                    f.write(f"\n Setup a Kho Lien Vung in city {ct}")
                    list_tinh.append(str(ct) + ",")

        return list_tinh
    except Exception as e:
        print(f"ERROR: {e}")
        


bugets = []
province_nums = []
list_tinh = inference(25)
with open("list_tinh.txt", "w") as f:
    f.writelines(list_tinh)


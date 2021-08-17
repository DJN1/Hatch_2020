
import os
import glob
import pandas as pd
from graphviz import Digraph, Graph


currDIR = os.getcwd() + "\\\\"


def getShape(gender):
    if gender == "M":
        return "rect"
    else:
        return "circle"

fileNameList = [f for f in glob.glob("data/*.csv")]

familyNameDict = {}

for name in fileNameList:
    familyNameDict[(name.replace("data\\", "").replace(".csv", ""))] = pd.read_csv(currDIR + name, encoding="UTF-8", skiprows=1)
    # familiesList.append(pd.read_csv(currDIR + name, encoding="UTF-8"))


# #df = pd.read_csv("data/F1.csv")

# #print(df)
selfNode = familyNameDict["F1"].iloc[0]
print(familyNameDict["F1"])
# familyName = fileNameList[0].replace("data\\", "").replace(".csv", "")

# fam = Graph(comment=familyName)
# fam.node("{}".format(str(familyName + selfNode), selfNode, shape=getShape(selfNode[1]))
# fam.node()


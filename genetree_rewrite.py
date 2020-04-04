# from graphviz import Digraph
import pandas as pd
import re
# import numpy as np

relationLevelMap = {
    "child": -1,
    "sibling child": -1,
    "self": 0,
    "sibling": 0,
    "sibling mate": 0,
    "father sibling child": 0,
    "father mate child": 0,
    "mate": 0,
    "mother sibling child": 0,
    "paternal grandfather sibling child child": 0,
    "mate father": 1,
    "mate mother": 1,
    "father": 1,
    "father mate": 1,
    "father sibling": 1,
    "father sibling mate": 1,
    "mother": 1,
    "mother sibling": 1,
    "mother sibling mate": 1,
    "paternal grandfather sibling child": 1,
    "paternal grandfather sibling child mate": 1,
    "maternal grandfather": 2,
    "maternal grandmother": 2,
    "maternal grandfather sibling": 2,
    "maternal grandmother sibling": 2,
    "paternal grandfather": 2,
    "paternal grandfather sibling": 2,
    "paternal grandfather sibling mate": 2,
    "paternal grandmother": 2,
    "paternal grandmother sibling": 2,
    "maternal grandfather father": 3,
    "maternal grandfather mother": 3,
    "maternal grandmother father": 3,
    "maternal grandmother mother": 3,
    "paternal grandfather father": 3,
    "paternal grandfather mother": 3,
    "paternal grandmother father": 3,
    "paternal grandmother mother": 3,
}

relationMap = {
    "Self": {
        "Mate": "Mate",
        "Child": "Child"
    },
    "Sibling": {
        "Mate": "Sibling Mate",
        "Child": "Sibling Child"
    },
    "Sibling Mate": {
        "Mate": "Sibling",
        "Child": "Sibling Child"
    },
    "Mate": {
        "Mate": "Self",
        "Child": "Child"
    },
    "Father": {
        "Mate": "Mother",
        "Child": ["Self", "Sibling"]
    },
    "Mother": {
        "Mate": "Father",
        "Child": ["Self", "Sibling"]
    },
    "Father Sibling": {
        "Mate": "Father Sibling Mate",
        "Child": "Father Sibling Child"
    },
    "Father Sibling Mate": {
        "Mate": "Father Sibling",
        "Child": "Father Sibling Child"
    },
    "Mother Sibling": {
        "Mate": "Mother Sibling Mate",
        "Child": "Mother Sibling Child"
    },
    "Mother Sibling Mate": {
        "Mate": "Mother Sibling",
        "Child": "Mother Sibling Child"
    },
    "Mate Father": {
        "Mate": "Mate Mother",
        "Child": "Mate"
    },
    "Mate Mother": {
        "Mate": "Mate Father",
        "Child": "Mate"
    },
    "Maternal Grandfather": {
        "Mate": "Maternal Grandmother",
        "Child": ["Mother", "Mother Sibling"]
    },
    "Maternal Grandmother": {
        "Mate": "Maternal Grandfather",
        "Child": ["Mother", "Mother Sibling"]
    },
    "Maternal Grandfather Father": {
        "Mate": "Maternal Grandfather Mother",
        "Child": ["Maternal Grandfather", "Maternal Grandfather Sibling"]
    },
    "Maternal Grandfather Mother": {
        "Mate": "Maternal Grandfather Father",
        "Child": ["Maternal Grandfather", "Maternal Grandfather Sibling"]
    },
    "Maternal Grandmother Father": {
        "Mate": "Maternal Grandmother Mother",
        "Child": ["Maternal Grandmother", "Maternal Grandmother Sibling"]
    },
    "Maternal Grandmother Mother": {
        "Mate": "Maternal Grandmother Father",
        "Child": ["Maternal Grandmother", "Maternal Grandmother Sibling"]
    },
    "Paternal Grandfather": {
        "Mate": "Paternal Grandmother",
        "Child": ["Father", "Father Sibling"]
    },
    "Paternal Grandmother": {
        "Mate": "Paternal Grandfather",
        "Child": ["Father", "Father Sibling"]
    },
    "Paternal Grandmother Father": {
        "Mate": "Paternal Grandmother Mother",
        "Child": ["Paternal Grandmother", "Paternal Grandmother Sibling"]
    },
    "Paternal Grandmother Mother": {
        "Mate": "Paternal Grandmother Father",
        "Child": ["Paternal Grandmother", "Paternal Grandmother Sibling"]
    },
    "Paternal Grandfather Father": {
        "Mate": "Paternal Grandfather Mother",
        "Child": ["Paternal Grandfather", "Paternal Grandfather Sibling"]
    },
    "Paternal Grandfather Mother": {
        "Mate": "Paternal Grandfather Father",
        "Child": ["Paternal Grandfather", "Paternal Grandfather Sibling"]
    },
    "Paternal Grandfather Sibling": {
        "Mate": "Paternal Grandfather Sibling Mate",
        "Child": "Paternal Grandfather Sibling Child"
    },
    "Paternal Grandfather Sibling Mate": {
        "Mate": "Paternal Grandfather Sibling",
        "Child": "Paternal Grandfather Sibling Child"
    },
    "Paternal Grandfather Sibling Child": {
        "Mate": "Paternal Grandfather Sibling Child Mate",
        "Child": "Paternal Grandfather Sibling Child Child"
    }
}


class Person:
    mother = None
    father = None
    children = None
    info = None
    relationLevel = None

    def __init__(self, mother, father, children, info, relationLevel):
        self.mother = mother
        self.father = father
        self.children = children
        self.info = info
        self.relationLevel = relationLevel

    def __str__(self):
        out = ""
        out += "Mother: " + self.mother if self.mother is not None else "N/A" + "\n"
        out += "Father: " + self.father if self.father is not None else "N/A" + "\n"
        out += "Children: " + (str(self.children) if self.children is not None else "N/A") + "\n"
        out += "Info: \n" + str(self.info) + "\n"
        out += "Relationlevel: " + str(self.relationLevel)
        return out

    def __repr__(self):
        out = ""
        out += "Mother: " + (self.mother if self.mother is not None else "N/A") + "\n"
        out += "Father: " + (self.father if self.father is not None else "N/A") + "\n"
        out += "Children: " + (str(self.children) if self.children is not None else "N/A") + "\n"
        out += "Info: \n" + str(self.info) + "\n"
        out += "Relationlevel: " + str(self.relationLevel)
        return out


class Info:
    relation = None
    sex = None
    alive = None
    disease = None
    onset = None
    death = None
    drawn = False

    def __init__(self, relation, sex, alive, disease, onset, death):
        self.relation = relation
        self.sex = sex
        self.alive = alive
        self.disease = disease
        self.onset = onset
        self.death = death

    def __str__(self):
        out = ""
        out += "Relation: " + self.relation + "\n"
        out += "Sex: " + self.sex + "\n"
        out += "Living: " + str(self.alive) + "\n"
        out += "Disease: " + str(self.disease) + "\n"
        out += "Age of Onset: " + str(self.onset) + "\n"
        out += "Age of Death: " + str(self.death) + "\n"
        return out

    def __repr__(self):
        out = ""
        out += "Relation: " + self.relation + "\n"
        out += "Sex: " + self.sex + "\n"
        out += "Living: " + str(self.alive) + "\n"
        out += "Disease: " + str(self.disease) + "\n"
        out += "Age of Onset: " + str(self.onset) + "\n"
        out += "Age of Death: " + str(self.death) + "\n"
        return out


def simplifyRel(rel):
    if rel == "self identical twin":
        return "sibling"
    elif rel == "self (adopted)":
        return "self"
    elif rel == "self twin":
        return "sibling"
    elif rel == "sibling identical twin":
        return "sibling"
    elif rel == "sibling twin":
        return "sibling"
    elif rel == "mother sibling identical twin":
        return "mother sibling"
    elif rel == "mother identical twin":
        return "mother sibling"
    elif rel == "mate's mother":
        return "mate mother"
    elif rel == "mate's father":
        return "mate father"
    elif rel == "child identical twin":
        return "child"
    elif rel == "paternal grandmother (adopted)":
        return "paternal grandmother"
    else:
        return rel


def mapChildren(sortedMappedList):
    return None


# for i in range(1, 21):
#     print(f"\n\nprocessing F{i}.csv\n")
fileDF = pd.read_csv(f"data/F1.csv")
# mapRelationsLevel1()
selfDF = fileDF.iloc[0]
# print(fileDF.iloc[0])

# selfInfo = Info(selfDF.iloc[0], selfDF.iloc[1], (True if selfDF.iloc[2] == 'Y' else False), selfDF.iloc[3], selfDF.iloc[4], selfDF.iloc[5])
# print(selfInfo)
# print(fileDF)
infoList = {}
for index, row in fileDF.iterrows():
    infoList[row.Relationship] = Info(row.Relationship, row.Sex, (True if row.Living == 'Y' else False), row.Disease, row.Onset, row.Death).__dict__

# print(infoList)

relations = infoList.keys()
relations = list(map(lambda s: re.sub(r" [0-9]", "", s).strip().lower(), relations))
relations = list(map(lambda s: re.sub(r" \(through adoption\)", "", s), relations))
relations = list(map(lambda s: simplifyRel(s), relations))
# Info(relation, sex, alive, disease, onset, death)
# print(relations)

maximumIndex = 0
maximumRel = relationLevelMap[relations[maximumIndex]]
maxList = [maximumIndex]
levels = [relationLevelMap[relations[0]]]


for i in range(1, len(relations)):
    levels.append(relationLevelMap[relations[i]])
    if relationLevelMap[relations[i]] > relationLevelMap[relations[maximumIndex]]:
        maximumIndex = i
        maximumRel = relationLevelMap[relations[maximumIndex]]
        maxList = [i]
    elif relationLevelMap[relations[i]] == relationLevelMap[relations[maximumIndex]]:
        maxList.append(i)

levelMappedList = sorted(list(zip(fileDF["Relationship"].tolist(), levels)), key=lambda tup: tup[1], reverse=True)
sortedMappedDict = dict(levelMappedList)
minimumLevel = min(levelMappedList, key=lambda tup: tup[1])[1]
maximumLevel = max(levelMappedList, key=lambda tup: tup[1])[1]

levelneg1List = []
level0List = []
level1List = []
level2List = []
level3List = []

personDict = {}

mainPerson = Person(None, None, None, None, None)
lowestPerson = None

for i in levelMappedList:
    personDict[i[0]] = Person(None, None, None, infoList[i[0]], i[1]).__dict__


print(personDict)
# for i in levelMappedList:
#     if i[1] == -1:
#         levelneg1List.append(Person(None, None))
#     elif i[1] == 0:
#         level0List.append(i)
#     elif i[1] == 1:
#         level1List.append(i)
#     elif i[1] == 2:
#         level2List.append(i)
#     elif i[1] == 3:
#         level3List.append(i)

# for i in levelneg1List:
#     lowestPerson = Person(None, None, None, infoList[i[0]])

# print(sortedMappedDict)
# print(infoList)

maxPersonList = []

# for i in range(len(maxList)):
#     currPerson = levelMappedList.pop(0)
#     maxPersonList.append(Person(None, None, None, infoList[currPerson[0]]))
#     print(levelMappedList[i])

# print(maxPersonList)
# print("\n\n\n\n")
# print(levelMappedList)

# Info(relation, sex, alive, disase, onset, death)
# Person(mother, father, children, info)


# while len(levelMappedList) > 0:
#     print(levelMappedList[0])
#     levelMappedList.pop(0)
# print(levels)

# print(f"maximum: {maximumRel} at index: {maximumIndex}. Relation: {relations[maximumIndex]}")
# for i in range(len(maxList)):
#     print(f"maxlist[i]: {maxList[i]}. Relation: {relations[maxList[i]]}")


done = []
# mapRelationsLevel1(infoList, done)
# print(done)

# grandparent = Digraph(name='grandparent', comment='f1.txt', format="png")
# parent = Digraph(name='parent')
# you = Digraph(name='self')
# child = Digraph(name='child')

# prev = None
# p = infoList.get("Self")

# print(infoList)
# while p.children is not None:
#     p = infoList.get(p.children[0])
# layer = 0
# while p is not None:
#     if layer == 0:
#         print(p.info.sex)
#         child.node(p.info.relation, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))
#     elif layer == 1:
#         print(p.info.sex)
#         you.node(p.info.relation, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))
#     elif layer == 2:
#         print(p.info.sex)
#         parent.node(p.info.relation, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))
#     elif layer == 3:
#         print(p.info.sex)
#         grandparent.node(p.info.relation, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))
#     print("p:{}".format(type(p)))
#     if p.mother is not None and p.father is not None:
#         children = infoList.get(p.mother).children.copy()
#         if layer == 0:
#             print(p.info.sex)
#             child.node(p.mother + 'dot', shape='point')
#             child.edge(p.info.relation, p.mother + 'dot', dir='none')
#             you.node(p.mother, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))
#             you.edge(p.mother, p.mother + 'dot', dir='none')
#             you.node(p.father, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))
#             you.edge(p.father, p.mother + 'dot', dir='none')
#         elif layer == 1:
#             print(p.info.sex)
#             you.node(p.mother + 'dot', shape='point')
#             you.edge(p.info.relation, p.mother + 'dot', dir='none')
#             parent.node(p.mother, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))
#             parent.edge(p.mother, p.mother + 'dot', dir='none')
#             parent.node(p.father, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))
#             parent.edge(p.father, p.mother + 'dot', dir='none')
#         elif layer == 2:
#             print(p.info.sex)
#             parent.node(p.mother + 'dot', shape='point')
#             parent.edge(p.info.relation, p.mother + 'dot', dir='none')
#             grandparent.node(p.mother, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))
#             grandparent.edge(p.mother, p.mother + 'dot', dir='none')
#             grandparent.node(p.father, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))
#             grandparent.edge(p.father, p.mother + 'dot', dir='none')
#         elif layer == 3:
#             print(p.info.sex)
#             grandparent.node(p.mother + 'dot', shape='point')
#             grandparent.edge(p.info.relation, p.mother + 'dot', dir='none')
#             grandparent.node(p.mother, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))
#             grandparent.edge(p.mother, p.mother + 'dot', dir='none')
#             grandparent.node(p.father, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))
#             grandparent.edge(p.father, p.mother + 'dot', dir='none')
#         if len(children) > 1:
#             children.remove(p.info.relation)
#             p = infoList.get(p.mother).children[0]
#             layer -= 1
#         else:
#             p = infoList.get(p.mother)
#             layer += 1
#     else:
#         p = p.mother


# grandparent.subgraph(parent)
# grandparent.subgraph(you)
# grandparent.subgraph(child)
# print(grandparent.source)
# grandparent.render(view=True)
# dot.node(p.info.relation, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))

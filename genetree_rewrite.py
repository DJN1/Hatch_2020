from graphviz import Graph
import pandas as pd
import re

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
    "mate's father": 1,
    "mate's mother": 1,
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

childMap = {
    "Self": {
        "Mate": "Mate",
        "Child": ["Child", "Child 1", "Child 2", "Child 3", "Child Identical Twin 1", "Child Identical Twin 2"]
    },
    "Mate": {
        "Mate": "Self",
        "Child": ["Child", "Child 1", "Child 2", "Child 3", "Child Identical Twin 1", "Child Identical Twin 2"]
    },
    "Sibling": {
        "Mate": "Sibling Mate",
        "Child": ["Sibling Child", "Sibling Child 1", "Sibling Child 2", "Sibling Child 3"]
    },
    "Sibling Mate": {
        "Mate": "Sibling",
        "Child": ["Sibling Child", "Sibling Child 1", "Sibling Child 2", "Sibling Child 3"]
    },
    "Sibling 1 (Through Adoption)": {
        "Mate": "Sibling 1 (Through Adoption) Mate",
        "Child": ["Sibling 1 (Through Adoption) Child"]
    },
    "Sibling 1 (Through Adoption) Mate": {
        "Mate": "Sibling 1 (Through Adoption)",
        "Child": ["Sibling 1 (Through Adoption) Child"]
    },
    "Sibling 1": {
        "Mate": "Sibling 1 Mate",
        "Child": ["Sibling 1 Child"]
    },
    "Sibling 1 Mate": {
        "Mate": "Sibling 1",
        "Child": ["Sibling 1 Child"]
    },
    "Sibling 2": {
        "Mate": "Sibling 2 Mate",
        "Child": ["Sibling 2 Child 1", "Sibling 2 Child 1 (Through Adoption)", "Sibling 2 Child 2", "Sibling 2 Child 2 (Through Adoption)", "Sibling 2 Child 3"]
    },
    "Sibling 2 Mate": {
        "Mate": "Sibling 2",
        "Child": ["Sibling 2 Child 1", "Sibling 2 Child 1 (Through Adoption)", "Sibling 2 Child 2", "Sibling 2 Child 2 (Through Adoption)", "Sibling 2 Child 3"]
    },
    "Sibling 2 (Through Adoption)": {
        "Mate": "Sibling 2 (Through Adoption) Mate",
        "Child": ["Sibling 2 (Through Adoption) Child"]
    },
    "Father": {
        "Mate": "Mother",
        "Child": ["Self", "Self (Adopted)", "Self Identical Twin", "Self Twin", "Sibling", "Sibling Identical Twin", "Sibling Twin", "Sibling 1", "Sibling 1 (Through Adoption)", "Sibling 2", "Sibling 2 (Through Adoption)", "Sibling 3", "Sibling 4", "Sibling 5"]
    },
    "Mother": {
        "Mate": "Father",
        "Child": ["Self", "Self (Adopted)", "Self Identical Twin", "Self Twin", "Sibling", "Sibling Identical Twin", "Sibling Twin", "Sibling 1", "Sibling 1 (Through Adoption)", "Sibling 2", "Sibling 2 (Through Adoption)", "Sibling 3", "Sibling 4", "Sibling 5"]
    },
    "Father Mate 2": {
        "Mate": "Father",
        "Child": ["Father Mate 2 Child"]
    },
    "Father Sibling": {
        "Mate": "Father Sibling Mate",
        "Child": ["Father Sibling Child", "Father Sibling Child 1", "Father Sibling Child 2"]
    },
    "Father Sibling Mate": {
        "Mate": "Father Sibling",
        "Child": ["Father Sibling Child", "Father Sibling Child 1", "Father Sibling Child 2"]
    },
    "Father Sibling 1": {
        "Mate": "Father Sibling 1 Mate",
        "Child": ["Father Sibling 1 Child"]
    },
    "Father Sibling 1 Mate": {
        "Mate": "Father Sibling 1",
        "Child": ["Father Sibling 1 Child"]
    },
    "Father Sibling 2": {
        "Mate": "Father Sibling 2 Mate",
        "Child": ["Father Sibling 2 Child 1", "Father Sibling 2 Child 2"]
    },
    "Fathe Sibling 2 Mate": {
        "Mate": "Father Sibling 2",
        "Child": ["Father Sibling 2 Child 1", "Father Sibling 2 Child 2"]
    },
    "Father Sibling 3": {
        "Mate": "Father Sibling 3 Mate",
        "Child": ["Father Sibling 3 Child 1", "Father Sibling 3 Child 2"]
    },
    "Mother Sibling": {
        "Mate": "Mother Sibling Mate",
        "Child": ["Mother Sibling Child 1", "Mother Sibling Child 2"]
    },
    "Mother Sibling 1": {
        "Mate": "Mother Sibling 1 Mate",
        "Child": ["Mother Sibling 1 Child 1", "Mother Sibling 1 Child 2", "Mother Sibling 1 Child 3"]
    },
    "Mother Sibling 1 Mate": {
        "Mate": "Mother Sibling",
        "Child": ["Mother Sibling 1 Child 1", "Mother Sibling 1 Child 2", "Mother Sibling 1 Child 3"]
    },
    "Mother Sibling 2": {
        "Mate": "Mother Sibling 2 Mate",
        "Child": ["Mother Sibling 2 Child", "Mother Sibling 2 Child 1", "Mother Sibling 2 Child 2", "Mother Sibling 2 Child 3", "Mother Sibling 2 Child 4"]
    },
    "Mother Sibling 2 Mate": {
        "Mate": "Mother Sibling 2",
        "Child": ["Mother Sibling 2 Child", "Mother Sibling 2 Child 1", "Mother Sibling 2 Child 2", "Mother Sibling 2 Child 3", "Mother Sibling 2 Child 4"]
    },
    "Mother Sibling 4": {
        "Mate": "Mother Sibling 4 Mate",
        "Child": ["Mother Sibling 4 Child"]
    },
    "Mate's Father": {
        "Mate": "Mate Mother",
        "Child": ["Mate"]
    },
    "Mate's Mother": {
        "Mate": "Mate Father",
        "Child": ["Mate"]
    },
    "Maternal Grandfather": {
        "Mate": "Maternal Grandmother",
        "Child": ["Mother", "Mother (Through Adoption)", "Mother Identical Twin", "Mother Sibling", "Mother Sibling Identical Twin", "Mother Sibling 1", "Mother Sibling 1 (Through Adoption)", "Mother Sibling 2", "Mother Sibling 2 (Through Adoption)", "Mother Sibling 2 Identical Twin", "Mother Sibling 3", "Mother Sibling 3 (Through Adoption)", "Mother Sibling 3 Identical Twin", "Mother Sibling 4"]
    },
    "Maternal Grandmother": {
        "Mate": "Maternal Grandfather",
        "Child": ["Mother", "Mother (Through Adoption)", "Mother Identical Twin", "Mother Sibling", "Mother Sibling Identical Twin", "Mother Sibling 1", "Mother Sibling 1 (Through Adoption)", "Mother Sibling 2", "Mother Sibling 2 (Through Adoption)", "Mother Sibling 2 Identical Twin", "Mother Sibling 3", "Mother Sibling 3 (Through Adoption)", "Mother Sibling 3 Identical Twin", "Mother Sibling 4"]
    },
    "Maternal Grandfather Father": {
        "Mate": "Maternal Grandfather Mother",
        "Child": ["Maternal Grandfather", "Maternal Grandfather (Through Adoption)", "Maternal Grandfather Sibling"]
    },
    "Maternal Grandfather Mother": {
        "Mate": "Maternal Grandfather Father",
        "Child": ["Maternal Grandfather", "Maternal Grandfather (Through Adoption)", "Maternal Grandfather Sibling"]
    },
    "Maternal Grandmother Father": {
        "Mate": "Maternal Grandmother Mother",
        "Child": ["Maternal Grandmother", "Maternal Grandmother (Through Adoption)", "Maternal Grandmother Sibling", "Maternal Grandmother Sibling 1", "Maternal Grandmother Sibling 2"]
    },
    "Maternal Grandmother Mother": {
        "Mate": "Maternal Grandmother Father",
        "Child": ["Maternal Grandmother", "Maternal Grandmother (Through Adoption)", "Maternal Grandmother Sibling", "Maternal Grandmother Sibling 1", "Maternal Grandmother Sibling 2"]
    },
    "Paternal Grandfather": {
        "Mate": "Paternal Grandmother",
        "Child": ["Father", "Father (Through Adoption)", "Father Sibling", "Father Sibling 1", "Father Sibling 2", "Father Sibling 3"]
    },
    "Paternal Grandmother": {
        "Mate": "Paternal Grandfather",
        "Child": ["Father", "Father (Through Adoption)", "Father Sibling", "Father Sibling 1", "Father Sibling 2", "Father Sibling 3"]
    },
    "Paternal Grandmother Father": {
        "Mate": "Paternal Grandmother Mother",
        "Child": ["Paternal Grandmother", "Paternal Grandmother Sibling"]
    },
    "Paternal Grandmother Mother": {
        "Mate": "Paternal Grandmother Father",
        "Child": ["Paternal Grandmother", "Paternal Grandmother (Adopted)", "Paternal Grandmother (Through Adoption)", "Paternal Grandmother Sibling", "Paternal Grandmother Sibling 1", "Paternal Grandmother Sibling 2", "Paternal Grandmother Sibling 3", "Paternal Grandmother Sibling 4", "Paternal Grandmother Sibling 5", "Paternal Grandmother Sibling 6", "Paternal Grandmother Sibling 7", "Paternal Grandmother Sibling 8"]
    },
    "Paternal Grandfather Father": {
        "Mate": "Paternal Grandfather Mother",
        "Child": ["Paternal Grandfather", "Paternal Grandfather (Through Adoption)", "Paternal Grandfather Sibling", "Paternal Grandfather Sibling 1", "Paternal Grandfather Sibling 2", "Paternal Grandfather Sibling 3", "Paternal Grandfather Sibling 4"]
    },
    "Paternal Grandfather Mother": {
        "Mate": "Paternal Grandfather Father",
        "Child": ["Paternal Grandfather", "Paternal Grandfather (Through Adoption)", "Paternal Grandfather Sibling", "Paternal Grandfather Sibling 1", "Paternal Grandfather Sibling 2", "Paternal Grandfather Sibling 3", "Paternal Grandfather Sibling 4"]
    },
    "Paternal Grandfather Sibling 1": {
        "Mate": "Paternal Grandfather Sibling 1 Mate",
        "Child": ["Paternal Grandfather Sibling 1 Child"]
    },
    "Paternal Grandfather Sibling 1 Mate": {
        "Mate": "Paternal Grandfather Sibling 1",
        "Child": ["Paternal Grandfather Sibling 1 Child"]
    },
    "Paternal Grandfather Sibling 1 Child": {
        "Mate": "Paternal Grandfather Sibling 1 Child Mate",
        "Child": "Paternal Grandfather Sibling 1 Child Child"
    },
    "Paternal Grandfather Sibling 2": {
        "Mate": "Paternal Grandfather Sibling 2 Mate",
        "Child": ["Paternal Grandfather Sibling 2 Child"]
    },
    "Paternal Grandfather Sibling 2 Mate": {
        "Mate": "Paternal Grandfather Sibling 2",
        "Child": ["Paternal Grandfather Sibling 2 Child"]
    },
    "Paternal Grandfather Sibling 2 Child": {
        "Mate": "Paternal Grandfather Sibling 2 Child Mate",
        "Child": ["Paternal Grandfather Sibling 2 Child Child"]
    },
    "Paternal Grandfather Sibling 2 Child Mate": {
        "Mate": "Paternal Grandfather Sibling 2 Child",
        "Child": ["Paternal Grandfather Sibling 2 Child Child"]
    }
}

parentMap = {
    "Child": {
        "Parent1": "Self",
        "Parent2": "Mate"
    },
    "Father": {
        "Parent1": "Paternal Grandfather",
        "Parent2": "Paternal Grandmother"
    },
    "Father Sibling Child": {
        "Parent1": "Father Sibling",
        "Parent2": "Father Sibling Mate"
    },
    "Father Mate 2 Child": {
        "Parent1": "Father",
        "Parent2": "Father Mate 2"
    },
    "Father Sibling 1 Child": {
        "Parent1": "Father Sibling 1",
        "Parent2": "Father Sibling 1 Mate"
    },
    "Father Sibling 2 Child 1": {
        "Parent1": "Father Sibling 2",
        "Parent2": "Father Sibling 2 Mate"
    },
    "Father Sibling 3 Child 1": {
        "Parent1": "Father Sibling 3",
        "Parent2": "Father Sibling 3 Mate"
    },
    "Maternal Grandfather": {
        "Parent1": "Maternal Grandfather Father",
        "Parent2": "Maternal Grandfather Mother"
    },
    "Maternal Grandmother": {
        "Parent1": "Maternal Grandmother Father",
        "Parent2": "Maternal Grandmother Mother"
    },
    "Mate": {
        "Parent1": "Mate's Father",
        "Parent2": "Mate's Mother"
    },
    "Mother": {
        "Parent1": "Maternal Grandfather",
        "Parent2": "Maternal Grandmother"
    },
    "Mother Sibling Child 1": {
        "Parent1": "Mother Sibling",
        "Parent2": "Mother Sibling Mate"
    },
    "Mother Sibling 1 Child 1": {
        "Parent1": "Mother Sibling 1",
        "Parent2": "Mother Sibling 1 Mate"
    },
    "Mother Sibling 2 Child": {
        "Parent1": "Mother Sibling 2",
        "Parent2": "Mother Sibling 2 Mate"
    },
    "Mother Sibling 4 Child": {
        "Parent1": "Mother Sibling 4",
        "Parent2": "Mother Sibling 4 Mate"
    },
    "Paternal Grandfather": {
        "Parent1": "Paternal Grandfather Father",
        "Parent2": "Paternal Grandfather Mother"
    },
    "Paternal Grandfather Sibling 1 Child": {
        "Parent1": "Paternal Grandfather Sibling 1",
        "Parent2": "Paternal Grandfather Sibling 1 Mate"
    },
    "Paternal Grandfather Sibling 1 Child Child": {
        "Parent1": "Paternal Grandfather Sibling 1 Child",
        "Parent2": "Paternal Grandfather Sibling 1 Child Mate"
    },
    "Paternal Grandfather Sibling 2 Child": {
        "Parent1": "Paternal Grandfather Sibling 2",
        "Parent2": "Paternal Grandfather Sibling 2 Mate"
    },
    "Paternal Grandfather Sibling 2 Child Child": {
        "Parent1": "Paternal Grandfather Sibling 2 Child",
        "Parent2": "Paternal Grandfather Sibling 2 Child Mate"
    },
    "Paternal Grandmother": {
        "Parent1": "Paternal Grandmother Father",
        "Parent2": "Paternal Grandmother Mother"
    },
    "Self": {
        "Parent1": "Father",
        "Parent2": "Mother"
    },
    "Sibling 1 (Through Adoption) Child": {
        "Parent1": "Sibling 1 (Through Adoption)",
        "Parent2": "Sibling 1 (Through Adoption) Mate"
    },
    "Sibling 1 Child": {
        "Parent1": "Sibling 1",
        "Parent2": "Sibling 1 Mate"
    },
    "Sibling 2 Child 1": {
        "Parent1": "Sibling 2",
        "Parent2": "Sibling 2 Mate"
    },
    "Sibling Child": {
        "Parent1": "Sibling",
        "Parent2": "Sibling Mate"
    },
}

aliasMap = {
    "Child 1": "Child",
    "Child 2": "Child",
    "Child 3": "Child",
    "Child Identical Twin 1": "Child",
    "Child Identical Twin 2": "Child",
    "Father (Through Adoption)": "Father",
    "Father Sibling": "Father",
    "Father Sibling 1": "Father",
    "Father Sibling 2": "Father",
    "Father Sibling 3": "Father",
    "Father Sibling Child 1": "Father Sibling Child",
    "Father Sibling Child 2": "Father Sibling Child",
    "Father Sibling 2 Child 2": "Father Sibling 2 Child 1",
    "Father Sibling 3 Child 2": "Father Sibling 3 Child 1",
    "Maternal Grandfather (Through Adoption)": "Maternal Grandfather",
    "Maternal Grandfather Sibling": "Maternal Grandfather",
    "Maternal Grandmother (Through Adoption)": "Maternal Grandmother",
    "Maternal Grandmother Sibling": "Maternal Grandmother",
    "Maternal Grandmother Sibling 1": "Maternal Grandmother",
    "Maternal Grandmother Sibling 2": "Maternal Grandmother",
    "Mother (Through Adoption)": "Mother",
    "Mother Identical Twin": "Mother",
    "Mother Sibling Identical Twin": "Mother",
    "Mother Sibling": "Mother",
    "Mother Sibling 1": "Mother",
    "Mother Sibling 1 (Through Adoption)": "Mother",
    "Mother Sibling 2": "Mother",
    "Mother Sibling 2 (Through Adoption)": "Mother",
    "Mother Sibling 2 Identical Twin": "Mother",
    "Mother Sibling 3": "Mother",
    "Mother Sibling 3 (Through Adoption)": "Mother",
    "Mother Sibling 3 Identical Twin": "Mother",
    "Mother Sibling 4": "Mother",
    "Paternal Grandfather (Through Adoption)": "Paternal Grandfather",
    "Paternal Grandfather Sibling": "Paternal Grandfather",
    "Paternal Grandfather Sibling 1": "Paternal Grandfather",
    "Paternal Grandfather Sibling 2": "Paternal Grandfather",
    "Paternal Grandfather Sibling 3": "Paternal Grandfather",
    "Paternal Grandfather Sibling 4": "Paternal Grandfather",
    "Paternal Grandmother (Adopted)": "Paternal Grandmother",
    "Paternal Grandmother (Though Adoption)": "Paternal Grandmother",
    "Paternal Grandmother Sibling 1": "Paternal Grandmother",
    "Paternal Grandmother Sibling 2": "Paternal Grandmother",
    "Paternal Grandmother Sibling 3": "Paternal Grandmother",
    "Paternal Grandmother Sibling 4": "Paternal Grandmother",
    "Paternal Grandmother Sibling 5": "Paternal Grandmother",
    "Paternal Grandmother Sibling 6": "Paternal Grandmother",
    "Paternal Grandmother Sibling 7": "Paternal Grandmother",
    "Paternal Grandmother Sibling 8": "Paternal Grandmother",
    "Self (Adopted)": "Self",
    "Self Identical Twin": "Self",
    "Self Twin": "Self",
    "Sibling": "Self",
    "Sibling Identical Twin": "Self",
    "Sibling Twin": "Self",
    "Sibling 1": "Self",
    "Sibling 1 (Through Adoption)": "Self",
    "Sibling 2": "Self",
    "Sibling 2 (Through Adoption)": "Self",
    "Sibling 3": "Self",
    "Sibling 4": "Self",
    "Sibling 5": "Self",
    "Mother Sibling Child 2": "Mother Sibling Child 1",
    "Mother Sibling 1 Child 2": "Mother Sibling 1 Child 1",
    "Mother Sibling 1 Child 3": "Mother Sibling 1 Child 1",
    "Mother Sibling 2 Child 1": "Mother Sibling 2 Child",
    "Mother Sibling 2 Child 2": "Mother Sibling 2 Child",
    "Mother Sibling 2 Child 3": "Mother Sibling 2 Child",
    "Mother Sibling 2 Child 4": "Mother Sibling 2 Child",
    "Sibling 2 Child 1 (Through Adoption)": "Sibling 2 Child 1",
    "Sibling 2 Child 2": "Sibling 2 Child 1",
    "Sibling 2 Child 2 (Through Adoption)": "Sibling 2 Child 1",
    "Sibling 2 Child 3 (Through Adoption)": "Sibling 2 Child 1",
    "Sibling Child 1": "Sibling Child",
    "Sibling Child 2": "Sibling Child",
    "Sibling Child 3": "Sibling Child"
}


class Person:
    mother = None
    father = None
    children = None
    info = None
    relationLevel = None

    def __init__(self, mother, father, children, info, relationLevel=None):
        self.mother = mother
        self.father = father
        self.children = children
        self.info = info
        self.relationLevel = relationLevel

    def getChildren(self):
        return self.children

    def getMother(self):
        return self.mother

    def getFather(self):
        return self.father

    def getParents(self):
        return f"Father: {self.father}\nMother: {self.mother}"

    def getInfo(self):
        return self.info

    def getRelationLevel(self):
        return self.relationLevel

    def setChildren(self, children):
        self.children = children

    def setMother(self, mother):
        self.mother = mother

    def setFather(self, father):
        self.father = father

    def setInfo(self, info):
        self.info = info

    def setRelationlevel(self, relationLevel):
        self.relationLevel = relationLevel

    def __str__(self):
        out = ""
        out += "Mother: " + (self.mother + "\n") if self.mother is not None else "N/A" + "\n"
        out += "Father: " + (self.father + "\n") if self.father is not None else "N/A" + "\n"
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
    elif rel == "child identical twin":
        return "child"
    elif rel == "paternal grandmother (adopted)":
        return "paternal grandmother"
    else:
        return rel


def mapChildren(person, infoList, personDict):
    try:
        childList = []
        for child in childMap[person]["Child"]:
            if child in infoList:
                childList.append(child)
    except KeyError:
        childList = []
    personDict[person].setChildren(childList)


def mapParents(person, infoList, personDict):
    parents = []
    father = ""
    mother = ""
    try:
        parents = [parentMap[person]["Parent1"], parentMap[person]["Parent2"]]
    except KeyError:
        try:
            parents = [parentMap[aliasMap[person]]["Parent1"], parentMap[person]["Parent2"]]
        except:
            parents = None
    if parents:
        try:
            if re.search("father", parents[0], flags=re.IGNORECASE):
                father = parents.pop(0)
                mother = parents.pop(0)
            elif infoList[parents[0]]["sex"] == 'M':
                father = parents.pop(0)
                mother = parents.pop(0)
            else:
                father = parents.pop(1)
                mother = parents.pop(0)
        except:
            father = "Unknown"
            mother = "Unknown"
    else:
        father = "Unknown"
        mother = "Unknown"
    personDict[person].setFather(father)
    personDict[person].setMother(mother)


# for itr in range(1, 21):
    # print(f"\n\nF{itr}.csv\n")
filename = "F3"
fileDF = pd.read_csv(f"data/{filename}.csv")
selfDF = fileDF.iloc[0]
personDict = {}

infoList = {}
for index, row in fileDF.iterrows():
    infoList[row.Relationship] = Info(row.Relationship, row.Sex, (True if row.Living == 'Y' else False), row.Disease, row.Onset, row.Death).__dict__

for p in infoList.keys():
    personDict[p] = Person(None, None, None, infoList[p])
    mapChildren(p, infoList, personDict)
    mapParents(p, infoList, personDict)

orderedPersonList = list(personDict.keys())

relations = infoList.keys()
relations = list(map(lambda s: re.sub(r" [0-9]", "", s).strip().lower(), relations))
relations = list(map(lambda s: re.sub(r" \(through adoption\)", "", s), relations))
relations = list(map(lambda s: simplifyRel(s), relations))

levels = [relationLevelMap[relations[0]]]

for i in range(1, len(relations)):
    levels.append(relationLevelMap[relations[i]])

levelMappedList = sorted(list(zip(fileDF["Relationship"].tolist(), levels)), key=lambda tup: tup[1], reverse=True)

for p in levelMappedList:
    personDict[p[0]].setRelationlevel(p[1])

maxLength = 0
for p in levelMappedList:
    maxLength = max(maxLength, len(p[0]))
print(maxLength)

graph = Graph(format="png", comment=filename, node_attr={
    "fixedsize": "true",
    "width": f"{maxLength / 8}",
})

childList = []
for p in personDict:
    if personDict[p].getChildren() not in childList and personDict[p].getChildren() != []:
        childList.append(personDict[p].getChildren())

parentList = []


for children in childList:
    for child in children:
        currCouple = (personDict[child].getFather(), personDict[child].getMother())
        if currCouple not in parentList and currCouple != ("Unknown", "Unknown"):
            parentList.append(currCouple)

coupleGraphList = []

for couple in parentList:
    g = Graph(name=couple[0], format="png", node_attr={
        "rank": "same",
        "fixedsize": "true",
        "width": f"{maxLength / 8}"
    }, graph_attr={"rankdir": "LR"}, edge_attr={"concentrate": "true"})
    fatherInfo = personDict[couple[0]].getInfo()
    motherInfo = personDict[couple[1]].getInfo()
    fatherDisease = ""
    fatherOnset = ""
    fatherDeath = ""
    motherDisease = ""
    motherOnset = ""
    motherDeath = ""
    if type(fatherInfo["disease"]) is str:
        fatherDisease = f"Disease: {fatherInfo['disease']}"
        fatherOnset = f"Onset: {fatherInfo['onset']}"
    if type(motherInfo["disease"]) is str:
        motherDisease = f"Disease: {motherInfo['disease']}"
        motherOnset = f"Onset: {motherInfo['onset']}"
    g.graph_attr["rankdir"] = "LR"
    if personDict[couple[0]].getInfo()["alive"]:
        g.node(couple[0], f"{couple[0]}\n{fatherDisease}\n{fatherOnset}", shape="square")
    else:
        fatherDeath = f"Died: {fatherInfo['death']}"
        g.node(couple[0], f"{couple[0]}\n{fatherDisease}\n{fatherOnset}\n{fatherDeath}", shape="square", color="black", fontcolor="white", style="filled")
    if personDict[couple[1]].getInfo()["alive"]:
        g.node(couple[1], f"{couple[1]}\n{motherDisease}\n{motherOnset}", shape="circle")
    else:
        motherDeath = f"Died: {motherInfo['death']}"
        g.node(couple[1], f"{couple[1]}\n{motherDisease}\n{motherOnset}\n{motherDeath}", shape="circle", color="black", fontcolor="white", style="filled")
    g.edge(couple[0], couple[1], constraint="true")
    coupleGraphList.append(g)

childrenGraphList = []


for idx, children in enumerate(childList):
    g = Graph(name=children[0], format="png", node_attr={
        "rank": "same",
        "fixedsize": "true",
        "width": f"{maxLength / 8}"
    }, graph_attr={"rankdir": "LR"}, edge_attr={"concentrate": "true"})

    for child in children:
        childInfo = personDict[child].getInfo()
        childDisease = ""
        childOnset = ""
        childDeath = ""
        if type(childInfo["disease"]) is str:
            childDisease = childInfo["disease"]
            childOnset = childInfo["onset"]
        if childInfo["sex"] == "M":
            if childInfo["alive"]:
                g.node(child, f"{child}\n{childDisease}\n{childOnset}", shape="square")
            else:
                childDeath = childInfo["death"]
                g.node(child, f"{child}\n{childDisease}\n{childOnset}\n{childDeath}", shape="square", color="black", fontcolor="white", style="filled")
        else:
            if childInfo["alive"]:
                g.node(child, f"{child}\n{childDisease}\n{childOnset}", shape="circle")
            else:
                childDeath = childInfo["death"]
                g.node(child, f"{child}\n{childDisease}\n{childOnset}\n{childDeath}", shape="circle", color="black", fontcolor="white", style="filled")
    for i in range(1, len(children)):
        g.edge(children[i - 1], children[i])

    childrenGraphList.append(g)

graphList = []
for idx in range(len(coupleGraphList)):
    parentG = coupleGraphList[idx]
    childrenG = childrenGraphList[idx]
    parentG.edge(childList[idx][0], parentList[idx][0], constraint="false")
    parentG.edge(childList[idx][0], parentList[idx][1], constraint="false")
    parentG.subgraph(childrenG)
    graphList.append(parentG)


G = Graph("combinedGraph", format="png", node_attr={"rank": "same"}, graph_attr={"rankdir": "TB"})
for graph in graphList:
    G.subgraph(graph)
G.render(filename="graph", format="png", cleanup=True)

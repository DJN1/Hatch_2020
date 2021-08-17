import networkx as nx
import matplotlib.pyplot as plt


class Person:
    relationship = ''
    sex = None
    alive = False
    disease = ''
    onset = ''
    death = ''
    value = 0
    values = {
        "greatgreatgrandchild": -3,
        "grandchild": -2,
        "child": -1,
        "sibling": 0,
        "self": 0,
        "cousin": 0,
        "mate": 0,
        "twin": 0,
        "mother": 1,
        "father": 1,
        "mate's father": 1,
        "mate's mother": 1,
        "grandfather": 2,
        "grandmother": 2,
        "greatgrandfather": 3,
        "greatgrandmother": 3,
        "greatgreatgrandfather": 4,
        "greatgreatgrandmother": 4
    }

    def getRelationValue(self):
        return self.values.get(self.relationship, 0)

    def setRelation(self, relation):
        self.relationship = relation.lower()

    def setSex(self, sex):
        self.sex = sex

    def setAlive(self, alive):
        self.alive = alive

    def setDisease(self, disease):
        self.disease = disease

    def setOnset(self, onset):
        self.onset = onset

    def setDeath(self, death):
        self.death = death

    def setValue(self):
        self.value = self.getRelationValue()

    def getRelation(self):
        return self.relationship

    def getSex(self):
        return self.sex

    def getAlive(self):
        return self.alive

    def getDisease(self):
        return self.disease

    def getOnset(self):
        return self.onset

    def getDeath(self):
        return self.death

    def getValue(self):
        return self.value

    def __str__(self):
        out = ''
        out += 'Relation: ' + self.relationship + '\n'
        out += 'Sex: ' + self.sex + '\n'
        out += 'Alive: ' + str(self.alive) + '\n'
        out += 'Disease: ' + (self.disease if self.disease != '' else 'None') + '\n'
        out += 'Age of Onset: ' + str(self.onset if self.onset != '' else 'N\A') + '\n'
        out += 'Age of Death: ' + str(self.death if self.death != '' else 'N\A') + '\n'
        return out


myFile = open("data/F1.txt", "rU")
people = []
for aRow in myFile:
    d = aRow.replace('\n', '').split('\t')
    p = Person()
    p.setRelation(d[0])
    p.setSex(d[1])
    p.setAlive(True if d[2] == 'Y' else False)
    p.setDisease(d[3])
    p.setOnset(d[4])
    p.setDeath(d[5] if d[5] != '' else '')
    p.setValue()
    people.append(p)
    # print(p)
    # print(aRow.replace('\n','').split('\t'))
myFile.close()

if people is not None:
    people.sort(key=lambda x: x.value, reverse=True)

# print(people)
g = nx.Graph()
val = people[0].getValue()
for x in range(1, len(people)):
    print(people[x].getValue())
    if int(people[x].getValue()) < int(val):
        val = people[x].getValue()
    else:
        g.add_edge(people[x], people[x - 1])

nx.draw(g)
plt.savefig("test.png")

from graphviz import Digraph
import pandas as pd
import numpy as np


class Person:
    mother = None
    father = None
    children = None
    info = None

    def __init__(self, mother, father, children, info):
        self.mother = mother
        self.father = father
        self.children = children
        self.info = info

    def __str__(self):
        out = ''
        out += "Mother: " + self.mother if self.mother is not None else 'N/A' + "\n"
        out += "Father: " + self.father if self.father is not None else 'N/A' + "\n"
        out += "Children: " + (str(self.children) if self.children is not None else 'N/A') + "\n"
        out += "Info: \n" + str(self.info)
        return out

    def __repr__(self):
        out = ''
        out += "Mother: " + (self.mother if self.mother is not None else 'N/A') + "\n"
        out += "Father: " + (self.father if self.father is not None else 'N/A') + "\n"
        out += "Children: " + (str(self.children) if self.children is not None else 'N/A') + "\n"
        out += "Info: \n" + str(self.info)
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
        out = ''
        out += "Sex: " + self.sex + "\n"
        out += "Living: " + str(self.alive) + "\n"
        out += "Disease: " + str(self.disease) + "\n"
        out += "Age of Onset: " + str(self.onset) + "\n"
        out += "Age of Death: " + str(self.death) + "\n"
        return out

    def __repr__(self):
        out = ''
        out += "Sex: " + self.sex + "\n"
        out += "Living: " + self.alive + "\n"
        out += "Disease: " + self.disease + "\n"
        out += "Age of Onset: " + self.disease + "\n"
        out += "Age of Death: " + self.death + "\n"
        return out


def getChildren(p, lines, level, done):
    children = []
    if level == 2:
        if "Child" in lines:
            if lines.get("Child").mother == p or lines.get("Child").father == p:
                children.append("Child")
        if "Child 1" in lines:
            if lines.get("Child 1").mother == p or lines.get("Child 1").father == p:
                children.append("Child 1")
        if "Child 2" in lines:
            if lines.get("Child 2").mother == p or lines.get("Child 2").father == p:
                children.append("Child 2")
        if "Child 3" in lines:
            if lines.get("Child 3").mother == p or lines.get("Child 3").father == p:
                children.append("Child 3")
        if "Sibling Child" in lines:
            if lines.get("Sibling Child").mother == p or lines.get("Sibling Child").father == p:
                children.append("Sibling Child")
        if "Sibling Child 1" in lines:
            if lines.get("Sibling Child 1").mother == p or lines.get("Sibling Child 1").father == p:
                children.append("Sibling Child 1")
        if "Sibling Child 2" in lines:
            if lines.get("Sibling Child 2").mother == p or lines.get("Sibling Child 2").father == p:
                children.append("Sibling Child 2")
        if "Sibling Child 3" in lines:
            if lines.get("Sibling Child 3").mother == p or lines.get("Sibling Child 3").father == p:
                children.append("Sibling Child 3")
        if "Sibling 1 (Through Adoption) Child" in lines:
            if lines.get("Sibling 1 (Through Adoption) Child").mother == p or lines.get("Sibling 1 (Through Adoption) Child").father == p:
                children.append("Sibling 1 (Through Adoption) Child")
        if "Sibling 1 Child" in lines:
            if lines.get("Sibling 1 Child").mother == p or lines.get("Sibling 1 Child").father == p:
                children.append("Sibling 1 Child")
        if "Sibling 2 Child 1" in lines:
            if lines.get("Sibling 2 Child 1").mother == p or lines.get("Sibling 2 Child 1").father == p:
                children.append("Sibling 2 Child 1")
        if "Sibling 2 Child 1 (Through Adoption)" in lines:
            if lines.get("Sibling 2 Child 1 (Through Adoption)").mother == p or lines.get("Sibling 2 Child 1 (Through Adoption)").father == p:
                children.append("Sibling 2 Child 1 (Through Adoption)")
        if "Sibling 2 Child 2" in lines:
            if lines.get("Sibling 2 Child 2").mother == p or lines.get("Sibling 2 Child 2").father == p:
                children.append("Sibling 2 Child 2")
        if "Sibling 2 Child 2 (Through Adoption)" in lines:
            if lines.get("Sibling 2 Child 2 (Through Adoption)").mother == p or lines.get("Sibling 2 Child 2 (Through Adoption)").father == p:
                children.append("Sibling 2 Child 2 (Through Adoption)")
        if "Sibling 2 Child 3" in lines:
            if lines.get("Sibling 2 Child 3").mother == p or lines.get("Sibling 2 Child 3").father == p:
                children.append("Sibling 2 Child 3")
        return children if len(children) != 0 else None
    elif level == 3:
        if "Self" in lines:
            if lines.get("Self").mother == p or lines.get("Self").father == p:
                children.append("Self")
        if "Self Identical Twin" in lines:
            if lines.get("Self Identical Twin").mother == p or lines.get("Self Identical Twin").father == p:
                children.append("Self Identical Twin")
        if "Self (Adopted)" in lines:
            if lines.get("Self (Adopted)").mother == p or lines.get("Self (Adopted)").father == p:
                children.append("Self (Adopted)")
        if "Self Twin" in lines:
            if lines.get("Self Twin").mother == p or lines.get("Self Twin").father == p:
                children.append("Self Twin")
        if "Mate" in lines:
            if lines.get("Mate").mother == p or lines.get("Mate").father == p:
                children.append("Mate")
        if "Sibling" in lines:
            if lines.get("Sibling").mother == p or lines.get("Sibling").father == p:
                children.append("Sibling")
        if "Sibling 1" in lines:
            if lines.get("Sibling 1").mother == p or lines.get("Sibling 1").father == p:
                children.append("Sibling 1")
        if "Sibling (Through Adoption)" in lines:
            if lines.get("Sibling (Through Adoption)").mother == p or lines.get("Sibling (Through Adoption)").father == p:
                children.append("Sibling (Through Adoption)")
        if "Sibling 2" in lines:
            if lines.get("Sibling 2").mother == p or lines.get("Sibling 2").father == p:
                children.append("Sibling 2")
        if "Sibling 2 (Through Adoption)" in lines:
            if lines.get("Sibling 2 (Through Adoption)").mother == p or lines.get("Sibling 2 (Through Adoption)").father == p:
                children.append("Sibling 2 (Through Adoption)")
        if "Sibling 3" in lines:
            if lines.get("Sibling 3").mother == p or lines.get("Sibling 3").father == p:
                children.append("Sibling 3")
        if "Sibling 4" in lines:
            if lines.get("Sibling 4").mother == p or lines.get("Sibling 4").father == p:
                children.append("Sibling 4")
        if "Sibling 5" in lines:
            if lines.get("Sibling 5").mother == p or lines.get("Sibling 5").father == p:
                children.append("Sibling 5")
        if "Sibling Twin" in lines:
            if lines.get("Sibling Twin").mother == p or lines.get("Sibling Twin").father == p:
                children.append("Sibling Twin")
        if "Sibling Mate" in lines:
            if lines.get("Sibling Mate").mother == p or lines.get("Sibling Mate").father == p:
                children.append("Sibling Mate")
        if "Sibling Identical Twin" in lines:
            if lines.get("Sibling Identical Twin").mother == p or lines.get("Sibling Identical Twin").father == p:
                children.append("Sibling Identical Twin")
        if "Mother Sibling 1 Child 1" in lines:
            if lines.get("Mother Sibling 1 Child 1").mother == p or lines.get("Mother Sibling 1 Child 1").father == p:
                children.append("Mother Sibling 1 Child 1")
        if "Mother Sibling 1 Child 2" in lines:
            if lines.get("Mother Sibling 1 Child 2").mother == p or lines.get("Mother Sibling 1 Child 2").father == p:
                children.append("Mother Sibling 1 Child 2")
        if "Mother Sibling 1 Child 3" in lines:
            if lines.get("Mother Sibling 1 Child 3").mother == p or lines.get("Mother Sibling 1 Child 3").father == p:
                children.append("Mother Sibling 1 Child 3")
        if "Mother Sibling 2 Child" in lines:
            if lines.get("Mother Sibling 2 Child").mother == p or lines.get("Mother Sibling 2 Child").father == p:
                children.append("Mother Sibling 2 Child")
        if "Mother Sibling 2 Child 1" in lines:
            if lines.get("Mother Sibling 2 Child 1").mother == p or lines.get("Mother Sibling 2 Child 1").father == p:
                children.append("Mother Sibling 2 Child 1")
        if "Mother Sibling 2 Child 2" in lines:
            if lines.get("Mother Sibling 2 Child 2").mother == p or lines.get("Mother Sibling 2 Child 2").father == p:
                children.append("Mother Sibling 2 Child 2")
        if "Mother Sibling 2 Child 3" in lines:
            if lines.get("Mother Sibling 2 Child 3").mother == p or lines.get("Mother Sibling 2 Child 3").father == p:
                children.append("Mother Sibling 2 Child 3")
        if "Mother Sibling 2 Child 4" in lines:
            if lines.get("Mother Sibling 2 Child 4").mother == p or lines.get("Mother Sibling 2 Child 4").father == p:
                children.append("Mother Sibling 2 Child 4")
        if "Mother Sibling 4 Child" in lines:
            if lines.get("Mother Sibling 4 Child").mother == p or lines.get("Mother Sibling 4 Child").father == p:
                children.append("Mother Sibling 4 Child")
        if "Mother Sibling Child 1" in lines:
            if lines.get("Mother Sibling Child 1").mother == p or lines.get("Mother Sibling Child 1").father == p:
                children.append("Mother Sibling Child 1")
        if "Mother Sibling Child 2" in lines:
            if lines.get("Mother Sibling Child 2").mother == p or lines.get("Mother Sibling Child 2").father == p:
                children.append("Mother Sibling Child 2")
        return children if len(children) != 0 else None


def mapRelationsLevel3(lines, done):
    if "Mother" not in done and "Mother" in lines:
        done.append("Mother")
        lines.update({"Mother": Person("Maternal Grandmother", "Maternal Grandfather", getChildren("Mother", lines, 3, []), lines.get("Mother"))})
    if "Mother (Through Adoption)" not in done and "Mother (Through Adoption)" in lines:
        done.append("Mother (Through Adoption)")
        lines.update({"Mother (Through Adoption)": Person("Maternal Grandmother (Through Adoption)", "Maternal Grandfather (Through Adoption)", getChildren("Mother (Through Adoption)", lines, 3, []), lines.get("Mother (Through Adoption)"))})
    if "Mother Identical Twin" not in done and "Mother Identical Twin" in lines:
        done.append("Mother Identical Twin")
        lines.update({"Mother Identical Twin": Person("Maternal Grandmother", "Maternal Grandfather", getChildren("Mother Identical Twin", lines, 3, []), lines.get("Mother Identical Twin"))})
    if "Mother Sibling" not in done and "Mother Sibling" in lines:
        done.append("Mother Sibling")
        lines.update({"Mother Sibling": Person("Maternal Grandmother", "Maternal Grandfather", getChildren("Mother Sibling", lines, 3, []), lines.get("Mother Sibling"))})
    if "Mother Sibling Identical Twin" not in done and "Mother Sibling Identical Twin" in lines:
        done.append("Mother Sibling Identical Twin")
        lines.update({"Mother Sibling Identical Twin": Person("Maternal Grandmother", "Maternal Grandfather", getChildren("Mother Sibling Identical Twin", lines, 3, []), lines.get("Mother Sibling Identical Twin"))})
    if "Mother Sibling Mate" not in done and "Mother Sibling Mate" in lines:
        done.append("Mother Sibling Mate")
        lines.update({"Mother Sibling Mate": Person(None, None, getChildren("Mother Sibling Mate", lines, 3, []), lines.get("Mother Sibling Mate"))})
    if "Mother Sibling 1" not in done and "Mother Sibling 1" in lines:
        done.append("Mother Sibling 1")
        lines.update({"Mother Sibling 1": Person("Maternal Grandmother", "Maternal Grandfather", getChildren("Mother Sibling 1", lines, 3, []), lines.get("Mother Sibling 1"))})
    if "Mother Sibling 1 (Through Adoption)" not in done and "Mother Sibling 1 (Through Adoption)" in lines:
        done.append("Mother Sibling 1 (Through Adoption)")
        lines.update({"Mother Sibling 1 (Through Adoption)": Person("Maternal Grandmother (Through Adoption)", "Maternal Grandfather (Through Adoption)", getChildren("Mother Sibling 1 (Through Adoption)", lines, 3, []), lines.get("Mother Sibling 1 (Through Adoption)"))})
    if "Mother Sibling 1 Mate" not in done and "Mother Sibling 1 Mate" in lines:
        done.append("Mother Sibling 1 Mate")
        lines.update({"Mother Sibling 1 Mate": Person(None, None, getChildren("Mother Sibling 1 Mate", lines, 3, []), lines.get("Mother Sibling 1 Mate"))})
    if "Mother Sibling 2" not in done and "Mother Sibling 2" in lines:
        done.append("Mother Sibling 2")
        lines.update({"Mother Sibling 2": Person("Maternal Grandmother", "Maternal Grandfather", getChildren("Mother Sibling 2", lines, 3, []), lines.get("Mother Sibling 2"))})
    if "Mother Sibling 2 (Through Adoption)" not in done and "Mother Sibling 2 (Through Adoption)" in lines:
        done.append("Mother Sibling 2 (Through Adoption)")
        lines.update({"Mother Sibling 2 (Through Adoption)": Person("Maternal Grandmother (Through Adoption)", "Maternal Grandfather (Through Adoption)", getChildren("Mother Sibling 2 (Through Adoption)", lines, 3, []), lines.get("Mother Sibling 2 (Through Adoption)"))})
    if "Mother Sibling 2 Identical Twin" not in done and "Mother Sibling 2 Identical Twin" in lines:
        done.append("Mother Sibling 2 Identical Twin")
        lines.update({"Mother Sibling 2 Identical Twin": Person("Maternal Grandmother", "Maternal Grandfather", getChildren("Mother Sibling 2 Identical Twin", lines, 3, []), lines.get("Mother Sibling 2 Identical Twin"))})
    if "Mother Sibling 2 Mate" not in done and "Mother Sibling 2 Mate" in lines:
        done.append("Mother Sibling 2 Mate")
        lines.update({"Mother Sibling 2 Mate": Person(None, None, getChildren("Mother Sibling 2 Mate", lines, 3, []), lines.get("Mother Sibling 2 Mate"))})
    if "Mother Sibling 3" not in done and "Mother Sibling 3" in lines:
        done.append("Mother Sibling 3")
        lines.update({"Mother Sibling 3": Person("Maternal Grandmother", "Maternal Grandfather", getChildren("Mother Sibling 3", lines, 3, []), lines.get("Mother Sibling 3"))})
    if "Mother Sibling 3 (Through Adoption)" not in done and "Mother Sibling 3 (Through Adoption)" in lines:
        done.append("Mother Sibling 3 (Through Adoption)")
        lines.update({"Mother Sibling 3 (Through Adoption)": Person("Maternal Grandmother (Through Adoption)", "Maternal Grandfather (Through Adoption)", getChildren("Mother Sibling 3 (Through Adoption)", lines, 3, []), lines.get("Mother Sibling 3 (Through Adoption)"))})
    if "Mother Sibling 3 Identical Twin" not in done and "Mother Sibling 3 Identical Twin" in lines:
        done.append("Mother Sibling 3 Identical Twin")
        lines.update({"Mother Sibling 3 Identical Twin": Person("Maternal Grandmother", "Maternal Grandfather", getChildren("Mother Sibling 3 Identical Twin", lines, 3, []), lines.get("Mother Sibling 3 Identical Twin"))})
    if "Mother Sibling 4" not in done and "Mother Sibling 4" in lines:
        done.append("Mother Sibling 4")
        lines.update({"Mother Sibling 4": Person("Maternal Grandmother", "Maternal Grandfather", getChildren("Mother Sibling 4", lines, 3, []), lines.get("Mother Sibling 4"))})
    if "Mother Sibling 4 Mate" not in done and "Mother Sibling 4 Mate" in lines:
        done.append("Mother Sibling 4 Mate")
        lines.update({"Mother Sibling 4 Mate": Person("Maternal Grandmother", "Maternal Grandfather", getChildren("Mother Sibling 4 Mate", lines, 3, []), lines.get("Mother Sibling 4 Mate"))})
    if "Father" not in done and "Father" in lines:
        done.append("Father")
        lines.update({"Father": Person("Paternal Grandmother", "Paternal Grandfather", getChildren("Father", lines, 3, []), lines.get("Father"))})
    if "Mate Father" not in done and "Mate Father" in lines:
        done.append("Mate Father")
        lines.update({"Mate Father": Person(None, None, getChildren("Mate Father", lines, 3, []), lines.get("Mate Father"))})
    if "Mate Mother" not in done and "Mate Mother" in lines:
        done.append("Mate Mother")
        lines.update({"Mate Mother": Person(None, None, getChildren("Mate Mother", lines, 3, []), lines.get("Mate Mother"))})
    if "Father (Through Adoption)" not in done and "Father (Through Adoption)" in lines:
        done.append("Father (Through Adoption)")
        lines.update({"Father (Through Adoption)": Person("Paternal Grandmother (Through Adoption)", "Paternal Grandfather (Through Adoption)", getChildren("Father (Through Adoption)", lines, 3, []), lines.get("Father (Through Adoption)"))})
    if "Father Mate 2" not in done and "Father Mate 2" in lines:
        done.append("Father Mate 2")
        lines.update({"Father Mate 2": Person(None, None, getChildren("Father Mate 2", lines, 3, []), lines.get("Father Mate 2"))})
    if "Father Sibling" not in done and "Father Sibing" in lines:
        done.append("Father Sibling")
        lines.update({"Father Sibling": Person("Paternal Grandmother", "Paternal Grandfather", getChildren("Father Sibling", lines, 3, []), lines.get("Father Sibling"))})
    if "Father Sibling Mate" not in done and "Father Sibling Mate" in lines:
        done.append("Father Sibling Mate")
        lines.update({"Father Sibling Mate": Person(None, None, getChildren("Father Sibling Mate", lines, 3, []), lines.get("Father Sibling Mate"))})
    if "Father Sibling 1" not in done and "Father Sibling 1" in lines:
        done.append("Father Sibling 1")
        lines.update({"Father Sibling 1": Person("Paternal Grandmother", "Paternal Grandfather", getChildren("Father Sibling 1", lines, 3, []), lines.get("Father Sibling 1"))})
    if "Father Sibling 2" not in done and "Father Sibling 2" in lines:
        done.append("Father Sibling 2")
        lines.update({"Father Sibling 2": Person("Paternal Grandmother", "Paternal Grandfather", getChildren("Father Sibling 2", lines, 3, []), lines.get("Father Sibling 2"))})
    if "Father Sibling 2 Mate" not in done and "Father Sibling 2 Mate" in lines:
        done.append("Father Sibling 2 Mate")
        lines.update({"Father Sibling 2 Mate": Person(None, None, getChildren("Father Sibling 2 Mate", lines, 3, []), lines.get("Father Sibling 2 Mate"))})
    if "Father Sibling 3" not in done and "Father Sibling 3" in lines:
        done.append("Father Sibling 3")
        lines.update({"Father Sibling 3": Person("Paternal Grandmother", "Paternal Grandfather", getChildren("Father Sibling 3", lines, 3, []), lines.get("Father Sibling 3"))})
    if "Father Sibling 3 Mate" not in done and "Father Sibling 3 Mate" in lines:
        done.append("Father Sibling 3 Mate")
        lines.update({"Father Sibling 3 Mate": Person(None, None, getChildren("Father Sibling 3 Mate", lines, 3, []), lines.get("Father Sibling 3 Mate"))})


def mapRelationsLevel2(lines, done):
    if "Self" not in done and "Self" in lines:
        done.append("Self")
        lines.update({"Self": Person("Mother", "Father", getChildren("Self", lines, 2, []), lines.get("Self"))})
    if "Self Identical Twin" not in done and "Self Identical Twin" in lines:
        done.append("Self Identical Twin")
        lines.update({"Self Identical Twin": Person("Mother", "Father", getChildren("Self Identical Twin", lines, 2, []), lines.get("Self Identical Twin"))})
    if "Self (Adopted)" not in done and "Self (Adopted)" in lines:
        done.append("Self (Adopted)")
        lines.update({"Self (Adopted)": Person("Mother", "Father", getChildren("Self (Adopted)", lines, 2, []), lines.get("Self (Adopted)"))})
    if "Self Twin" not in done and "Self Twin" in lines:
        done.append("Self Twin")
        lines.update({"Self Twin": Person("Mother", "Father", getChildren("Self Twin", lines, 2, []), lines.get("Self Twin"))})
    if "Mate" not in done and "Mate" in lines:
        done.append("Mate")
        lines.update({"Mate": Person(("Mate Mother" if lines.get("Mate Mother") is not None else None), ("Mate Father" if lines.get("Mate Father") is not None else None), getChildren("Mate", lines, 2, []), lines.get("Mate"))})
    if "Sibling" not in done and "Sibling" in lines:
        done.append("Sibling")
        lines.update({"Sibling": Person("Mother", "Father", getChildren("Sibling", lines, 2, []), lines.get("Sibling"))})
    if "Sibling 1" not in done and "Sibling 1" in lines:
        done.append("Sibling 1")
        lines.update({"Sibling 1": Person("Mother", "Father", getChildren("Sibling 1", lines, 2, []), lines.get("Sibling 1"))})
    if "Sibling (Through Adoption)" not in done and "Sibling (Through Adoption)" in lines:
        done.append("Sibling 1 (Through Adoption)")
        lines.update({"Sibling 1 (Through Adoption)": Person("Mother", "Father", getChildren("Sibling 1 (Through Adoption)", lines, 2, []), lines.get("Sibling 1 (Through Adoption)"))})
    if "Sibling 2" not in done and "Sibling 2" in lines:
        done.append("Sibling 2")
        lines.update({"Sibling 2": Person("Mother", "Father", getChildren("Sibling 2", lines, 2, []), lines.get("Sibling 2"))})
    if "Sibling 2 (Through Adoption)" not in done and "Sibling 2 (Through Adoption)" in lines:
        done.append("Sibling 2 (Through Adoption)")
        lines.update({"Sibling 2 (Through Adoption)": Person("Mother", "Father", getChildren("Sibling 2 (Through Adoption)", lines, 2, []), lines.get("Sibling 2 (Through Adoption)"))})
    if "Sibling 3" not in done and "Sibling 3" in lines:
        done.append("Sibling 3")
        lines.update({"Sibling 3": Person("Mother", "Father", getChildren("Sibling 3", lines, 2, []), lines.get("Sibling 3"))})
    if "Sibling 4" not in done and "Sibling 4" in lines:
        done.append("Sibling 4")
        lines.update({"Sibling 4": Person("Mother", "Father", getChildren("Sibling 4", lines, 2, []), lines.get("Sibling 4"))})
    if "Sibling 5" not in done and "Sibling 5" in lines:
        done.append("Sibling 5")
        lines.update({"Sibling 5": Person("Mother", "Father", getChildren("Sibling 5", lines, 2, []), lines.get("Sibling 5"))})
    if "Sibling Twin" not in done and "Sibling Twin" in lines:
        done.append("Sibling Twin")
        lines.update({"Sibling Twin": Person("Mother", "Father", getChildren("Sibling Twin", lines, 2, []), lines.get("Sibling Twin"))})
    if "Sibling Mate" not in done and "Sibling Mate" in lines:
        done.append("Sibling Mate")
        lines.update({"Sibling Mate": Person(("Sibling Mate Mother" if lines.get("Sibling Mate Mother") is not None else None), ("Sibling Mate Father" if lines.get("Sibling Mate Father") is not None else None), getChildren("Sibling Mate", lines, 2, []), lines.get("Sibling Mate"))})
    if "Sibling Identical Twin" not in done and "Sibling Identical Twin" in lines:
        done.append("Sibling Identical Twin")
        lines.update({"Sibling Identical Twin": Person("Mother", "Father", getChildren("Sibling Identical Twin", lines, 2, []), lines.get("Sibling Identical Twin"))})
    if "Mother Sibling 1 Child 1" not in done and "Mother Sibling 1 Child 1" in lines:
        done.append("Mother Sibling 1 Child 1")
        if lines.get("Mother Sibling 1").sex == 'M':
            lines.update({"Mother Sibling 1 Child 1": Person("Mother Sibling 1 Mate", "Mother Sibling 1", getChildren("Mother Sibling 1 Child 1", lines, 2, []), lines.get("Mother Sibling 1 Child 1"))})
        else:
            lines.update({"Mother Sibling 1 Child 1": Person("Mother Sibling 1", "Mother Sibling 1 Mate", getChildren("Mother Sibling 1 Child 1", lines, 2, []), lines.get("Mother Sibling 1 Child 1"))})
    if "Mother Sibling 1 Child 2" not in done and "Mother Sibling 1 Child 2" in lines:
        done.append("Mother Sibling 1 Child 2")
        if lines.get("Mother Sibling 1").sex == 'M':
            lines.update({"Mother Sibling 1 Child 2": Person("Mother Sibling 1 Mate", "Mother Sibling 1", getChildren("Mother Sibling 1 Child 2", lines, 2, []), lines.get("Mother Sibling 1 Child 2"))})
        else:
            lines.update({"Mother Sibling 1 Child 2": Person("Mother Sibling 1", "Mother Sibling 1 Mate", getChildren("Mother Sibling 1 Child 2", lines, 2, []), lines.get("Mother Sibling 1 Child 2"))})
    if "Mother Sibling 1 Child 3" not in done and "Mother Sibling 1 Child 3" in lines:
        done.append("Mother Sibling 1 Child 3")
        if lines.get("Mother Sibling 1").sex == 'M':
            lines.update({"Mother Sibling 1 Child 3": Person("Mother Sibling 1 Mate", "Mother Sibling 1", getChildren("Mother Sibling 1 Child 3", lines, 2, []), lines.get("Mother Sibling 1 Child 3"))})
        else:
            lines.update({"Mother Sibling 1 Child 3": Person("Mother Sibling 1", "Mother Sibling 1 Mate", getChildren("Mother Sibling 1 Child 3", lines, 2, []), lines.get("Mother Sibling 1 Child 3"))})
    if "Mother Sibling 2 Child" not in done and "Mother Sibling 2 Child" in lines:
        done.append("Mother Sibling 2 Child")
        if lines.get("Mother Sibling 2").sex == 'M':
            lines.update({"Mother Sibling 2 Child": Person("Mother Sibling 2 Mate", "Mother Sibling 2", getChildren("Mother Sibling 2 Child", lines, 2, []), lines.get("Mother Sibling 2 Child"))})
        else:
            lines.update({"Mother Sibling 2 Child": Person("Mother Sibling 2", "Mother Sibling 2 Mate", getChildren("Mother Sibling 2 Child", lines, 2, []), lines.get("Mother Sibling 2 Child"))})
    if "Mother Sibling 2 Child 1" not in done and "Mother Sibling 2 Child 1" in lines:
        done.append("Mother Sibling 2 Child 1")
        if lines.get("Mother Sibling 2").sex == 'M':
            lines.update({"Mother Sibling 2 Child 1": Person("Mother Sibling 2 Mate", "Mother Sibling 2", getChildren("Mother Sibling 2 Child 1", lines, 2, []), lines.get("Mother Sibling 2 Child 1"))})
        else:
            lines.update({"Mother Sibling 2 Child 1": Person("Mother Sibling 2", "Mother Sibling 2 Mate", getChildren("Mother Sibling 2 Child 1", lines, 2, []), lines.get("Mother Sibling 2 Child 1"))})
    if "Mother Sibling 2 Child 2" not in done and "Mother Sibling 2 Child 2" in lines:
        done.append("Mother Sibling 2 Child 2")
        if lines.get("Mother Sibling 2").sex == 'M':
            lines.update({"Mother Sibling 2 Child 2": Person("Mother Sibling 2 Mate", "Mother Sibling 2", getChildren("Mother Sibling 2 Child 2", lines, 2, []), lines.get("Mother Sibling 2 Child 2"))})
        else:
            lines.update({"Mother Sibling 2 Child 2": Person("Mother Sibling 2", "Mother Sibling 2 Mate", getChildren("Mother Sibling 2 Child 2", lines, 2, []), lines.get("Mother Sibling 2 Child 2"))})
    if "Mother Sibling 2 Child 3" not in done and "Mother Sibling 2 Child 3" in lines:
        done.append("Mother Sibling 2 Child 3")
        if lines.get("Mother Sibling 2").sex == 'M':
            lines.update({"Mother Sibling 2 Child 3": Person("Mother Sibling 2 Mate", "Mother Sibling 2", getChildren("Mother Sibling 2 Child 3", lines, 2, []), lines.get("Mother Sibling 2 Child 3"))})
        else:
            lines.update({"Mother Sibling 2 Child 3": Person("Mother Sibling 2", "Mother Sibling 2 Mate", getChildren("Mother Sibling 2 Child 3", lines, 2, []), lines.get("Mother Sibling 2 Child 3"))})
    if "Mother Sibling 2 Child 4" not in done and "Mother Sibling 2 Child 4" in lines:
        done.append("Mother Sibling 2 Child 4")
        if lines.get("Mother Sibling 2").sex == 'M':
            lines.update({"Mother Sibling 2 Child 4": Person("Mother Sibling 2 Mate", "Mother Sibling 2", getChildren("Mother Sibling 2 Child 4", lines, 2, []), lines.get("Mother Sibling 2 Child 4"))})
        else:
            lines.update({"Mother Sibling 2 Child 4": Person("Mother Sibling 2", "Mother Sibling 2 Mate", getChildren("Mother Sibling 2 Child 4", lines, 2, []), lines.get("Mother Sibling 2 Child 4"))})
    if "Mother Sibling 4 Child" not in done and "Mother Sibling 4 Child" in lines:
        done.append("Mother Sibling 4 Child")
        if lines.get("Mother Sibling 4").sex == 'M':
            lines.update({"Mother Sibling 4 Child": Person("Mother Sibling 4 Mate", "Mother Sibling 4", getChildren("Mother Sibling 4 Child", lines, 2, []), lines.get("Mother Sibling 4 Child"))})
        else:
            lines.update({"Mother Sibling 4 Child": Person("Mother Sibling 4", "Mother Sibling 4 Mate", getChildren("Mother Sibling 4 Child", lines, 2, []), lines.get("Mother Sibling 4 Child"))})
    if "Mother Sibling Child 1" not in done and "Mother Sibling Child 1" in lines:
        done.append("Mother Sibling Child 1")
        if lines.get("Mother Sibling").sex == 'M':
            lines.update({"Mother Sibling Child 1": Person("Mother Sibling Mate", "Mother Sibling", getChildren("Mother Sibling Child 1", lines, 2, []), lines.get("Mother Sibling Child 1"))})
        else:
            lines.update({"Mother Sibling Child 1": Person("Mother Sibling", "Mother Sibling Mate", getChildren("Mother Sibling Child 1", lines, 2, []), lines.get("Mother Sibling Child 1"))})
    if "Mother Sibling Child 2" not in done and "Mother Sibling Child 2" in lines:
        done.append("Mother Sibling Child 2")
        if lines.get("Mother Sibling").sex == 'M':
            lines.update({"Mother Sibling Child 2": Person("Mother Sibling Mate", "Mother Sibling", getChildren("Mother Sibling Child 2", lines, 2, []), lines.get("Mother Sibling Child 2"))})
        else:
            lines.update({"Mother Sibling Child 2": Person("Mother Sibling", "Mother Sibling Mate", getChildren("Mother Sibling Child 2", lines, 2, []), lines.get("Mother Sibling Child 2"))})
    mapRelationsLevel3(lines, [])


def mapRelationsLevel1(lines, done):
    if "Child" not in done and "Child" in lines:
        done.append("Child")
        if lines.get("Self").sex == 'M':
            if "Mate" in lines:
                lines.update({"Child": Person("Mate", "Self", None, lines.get("Child"))})
            else:
                lines.update({"Child": Person(None, "Self", None, lines.get("Child"))})
        else:
            if "Mate" in lines:
                lines.update({"Child": Person("Self", "Mate", None, lines.get("Child"))})
            else:
                lines.update({"Child": Person("Self", None, None, lines.get("Child"))})
        # go up a level
    if "Child 1" not in done and "Child 1" in lines:
        # go up and delete relation
        done.append("Child 1")
        try:
            if lines.get("Self").sex == 'M':
                if "Mate" in lines:
                    lines.update({"Child 1": Person("Mate", "Self", None, lines.get("Child 1"))})
                else:
                    lines.update({"Child 1": Person(None, "Self", None, lines.get("Child 1"))})
            else:
                if "Mate" in lines:
                    lines.update({"Child 1": Person("Self", "Mate", None, lines.get("Child 1"))})
                else:
                    lines.update({"Child 1": Person("Self", None, None, lines.get("Child 1"))})
        except:
            if "Mate" in lines:
                lines.update({"Child 1": Person("Self", "Mate", None, lines.get("Child 1"))})
            else:
                lines.update({"Child 1": Person("Self", None, None, lines.get("Child 1"))})
        # go up a level
    if "Child 2" not in done and "Child 2" in lines:
        # go up
        done.append("Child 2")
        try:
            if lines.get("Self").sex == 'M':
                if "Mate" in lines:
                    lines.update({"Child 2": Person("Mate", "Self", None, lines.get("Child 2"))})
                else:
                    lines.update({"Child 2": Person(None, "Self", None, lines.get("Child 2"))})
            else:
                if "Mate" in lines:
                    lines.update({"Child 2": Person(None, "Self", None, lines.get("Child 2"))})
                else:
                    lines.update({"Child 2": Person("Self", None, None, lines.get("Child 2"))})
        except:
            if "Mate" in lines:
                lines.update({"Child 2": Person(None, "Self", None, lines.get("Child 2"))})
            else:
                lines.update({"Child 2": Person("Self", None, None, lines.get("Child 2"))})
        # go up a level
    if "Child 3" not in done and "Child 3" in lines:
        # go up
        done.append("Child 3")
        if lines.get("Self").sex == 'M':
            if "Mate" in lines:
                lines.update({"Child 3": Person("Mate", "Self", None, lines.get("Child 3"))})
            else:
                lines.update({"Child 3": Person(None, "Self", None, lines.get("Child 3"))})
        else:
            if "Mate" in lines:
                lines.update({"Child 3": Person("Self", "Mate", None, lines.get("Child 3"))})
            else:
                lines.update({"Child 3": Person("Self", None, None, lines.get("Child 3"))})
        # go up a level
    if "Sibling Child" not in done and "Sibling Child" in lines:
        # go up
        done.append("Sibling Child")
        try:
            if lines.get("Sibling").sex == 'M':
                if "Sibling Mate" in lines:
                    lines.update({"Sibling Child": Person("Sibling Mate", "Sibling", None, lines.get("Sibling Child"))})
                else:
                    lines.update({"Sibling Child": Person(None, "Sibling", None, lines.get("Sibling Child"))})
            else:
                if "Sibling Mate" in lines:
                    lines.update({"Sibling Child": Person("Sibling", "Sibling Mate", None, lines.get("Sibling Child"))})
                else:
                    lines.update({"Sibling Child": Person("Sibling", None, None, lines.get("Sibling Child"))})
        except:
            if "Sibling Mate" in lines:
                lines.update({"Sibling Child": Person("Sibling", "Sibling Mate", None, lines.get("Sibling Child"))})
            else:
                lines.update({"Sibling Child": Person("Sibling", None, None, lines.get("Sibling Child"))})
    if "Sibling Child 1" not in done and "Sibling Child 1" in lines:
        # go up
        done.append("Sibling Child 1")
        if lines.get("Sibling").sex == 'M':
            if "Sibling Mate" in lines:
                lines.update({"Sibling Child 1": Person("Sibling Mate", "Sibling", None, lines.get("Sibling Child 1"))})
            else:
                lines.update({"Sibling Child 1": Person(None, "Sibling", None, lines.get("Sibling Child 1"))})
        else:
            if "Sibling Mate" in lines:
                lines.update({"Sibling Child 1": Person("Sibling", "Sibling Mate", None, lines.get("Sibling Child 1"))})
            else:
                lines.update({"Sibling Child 1": Person("Sibling", None, None, lines.get("Sibling Child 1"))})
    if "Sibling Child 2" not in done and "Sibling Child 2" in lines:
        # go up
        done.append("Sibling Child 2")
        if lines.get("Sibling").sex == 'M':
            if "Sibling Mate" in lines:
                lines.update({"Sibling Child 2": Person("Sibling Mate", "Sibling", None, lines.get("Sibling Child 2"))})
            else:
                lines.update({"Sibling Child 2": Person(None, "Sibling", None, lines.get("Sibling Child 2"))})
        else:
            if "Sibling Mate" in lines:
                lines.update({"Sibling Child 2": Person("Sibling", "Sibling Mate", None, lines.get("Sibling Child 2"))})
            else:
                lines.update({"Sibling Child 2": Person("Sibling", None, None, lines.get("Sibling Child 2"))})
    if "Sibling Child 3" not in done and "Sibling Child 3" in lines:
        # go up
        done.append("Sibling Child 3")
        if lines.get("Sibling").sex == 'M':
            if "Sibling Mate" in lines:
                lines.update({"Sibling": Person("Sibling Mate", "Sibling", None, lines.get("Sibling Child 3"))})
            else:
                lines.update({"Sibling": Person(None, "Sibling", None, lines.get("Sibling Child 3"))})
        else:
            if "Sibling Mate" in lines:
                lines.update({"Sibling": Person("Sibling", "Sibling Mate", None, lines.get("Sibling Child 3"))})
            else:
                lines.update({"Sibling": Person("Sibling", None, None, lines.get("Sibling Child 3"))})
    if "Sibling 1 (Through Adoption) Child" not in done and "Sibling 1 (Through Adoption) Child" in lines:
        # go up
        done.append("Sibling 1 (Through Adoption) Child")
        if lines.get("Sibling 1 (Through Adoption)").sex == 'M':
            if "Sibling 1 (Through Adoption) Mate" in lines:
                lines.update({"Sibling 1 (Through Adoption) Child": Person("Sibling 1 (Through Adoption) Mate", "Sibling 1 (Through Adoption)", None, lines.get("Sibling 1 (Through Adoption) Child"))})
            else:
                lines.update({"Sibling 1 (Through Adoption) Child": Person(None, "Sibling 1 (Through Adoption)", None, lines.get("Sibling 1 (Through Adoption) Child"))})
        else:
            if "Sibling 1 (Through Adoption) Mate" in lines:
                lines.update({"Sibling 1 (Through Adoption) Child": Person("Sibling 1 (Through Adoption)", "Sibling 1 (Through Adoption) Mate", None, lines.get("Sibling 1 (Through Adoption) Child"))})
            else:
                lines.update({"Sibling 1 (Through Adoption) Child": Person("Sibling 1 (Through Adoption)", None, None, lines.get("Sibling 1 (Through Adoption) Child"))})
    if "Sibling 1 Child" not in done and "Sibling 1 Child" in lines:
        # go up
        done.append("Sibling 1 Child")
        if lines.get("Sibling 1").sex == 'M':
            if "Sibling 1 Mate" in lines:
                lines.update({"Sibling 1 Child": Person("Sibling 1 Mate", "Sibling 1", None, lines.get("Sibling 1 Child"))})
            else:
                lines.update({"Sibling 1 Child": Person(None, "Sibling 1", None, lines.get("Sibling 1 Child"))})
        else:
            if "Sibling 1 Mate" in lines:
                lines.update({"Sibling 1 Child": Person("Sibling 1", "Sibling 1 Mate", None, lines.get("Sibling 1 Child"))})
            else:
                lines.update({"Sibling 1 Child": Person("Sibling 1", None, None, lines.get("Sibling 1 Child"))})
    if "Sibling 2 Child 1" not in done and "Sibling 2 Child 1" in lines:
        # go up
        done.append("Sibling 2 Child 1")
        if lines.get("Sibling 2").sex == 'M':
            if "Sibling 2 Mate" in lines:
                lines.update({"Sibling 2 Child 1": Person("Sibling 2 Mate", "Sibling 2", None, lines.get("Sibling 2 Child 1"))})
            else:
                lines.update({"Sibling 2 Child 1": Person(None, "Sibling 2", None, lines.get("Sibling 2 Child 1"))})
        else:
            if "Sibling 2 Mate" in lines:
                lines.update({"Sibling 2 Child 1": Person("Sibling 2", "Sibling 2 Mate", None, lines.get("Sibling 2 Child 1"))})
            else:
                lines.update({"Sibling 2 Child 1": Person("Sibling 2", None, None, lines.get("Sibling 2 Child 1"))})
    if "Sibling 2 Child 1 (Through Adoption)" not in done and "Sibling 2 Child 1 (Through Adoption)" in lines:
        # go up
        done.append("Sibling 2 Child 1 (Through Adoption)")
        try:
            if lines.get("Sibling 2").sex == 'M':
                if "Sibling 2 Mate" in lines:
                    lines.update({"Sibling 2 Child 1 (Through Adoption)": Person("Sibling 2 Mate", "Sibling 2", None, lines.get("Sibling 2 Child 1 (Through Adoption)"))})
                else:
                    lines.update({"Sibling 2 Child 1 (Through Adoption)": Person(None, "Sibling 2", None, lines.get("Sibling 2 Child 1 (Through Adoption)"))})
            else:
                if "Sibling 2 Mate" in lines:
                    lines.update({"Sibling 2 Child 1 (Through Adoption)": Person("Sibling 2", "Sibling 2 Mate", None, lines.get("Sibling 2 Child 1 (Through Adoption)"))})
                else:
                    lines.update({"Sibling 2 Child 1 (Through Adoption)": Person("Sibling 2", None, None, lines.get("Sibling 2 Child 1 (Through Adoption)"))})
        except:
            if "Sibling 2 Mate" in lines:
                lines.update({"Sibling 2 Child 1 (Through Adoption)": Person("Sibling 2", "Sibling 2 Mate", None, lines.get("Sibling 2 Child 1 (Through Adoption)"))})
            else:
                lines.update({"Sibling 2 Child 1 (Through Adoption)": Person("Sibling 2", None, None, lines.get("Sibling 2 Child 1 (Through Adoption)"))})
    if "Sibling 2 Child 2" not in done and "Sibling 2 Child 2" in lines:
        # go up
        done.append("Sibling 2 Child 2")
        if lines.get("Sibling 2").sex == 'M':
            if "Sibling 2 Mate" in lines:
                lines.update({"Sibling 2 Child 2": Person("Sibling 2 Mate", "Sibling 2", None, lines.get("Sibling 2 Child 2"))})
            else:
                lines.update({"Sibling 2 Child 2": Person(None, "Sibling 2", None, lines.get("Sibling 2 Child 2"))})
        else:
            if "Sibling 2 Mate" in lines:
                lines.update({"Sibling 2 Child 2": Person("Sibling 2", "Sibling 2 Mate", None, lines.get("Sibling 2 Child 2"))})
            else:
                lines.update({"Sibling 2 Child 2": Person("Sibling 2", None, None, lines.get("Sibling 2 Child 2"))})
    if "Sibling 2 Child 2 (Through Adoption)" not in done and "Sibling 2 Child 2 (Through Adoption)" in lines:
        # go up
        done.append("Sibling 2 Child 2 (Through Adoption)")
        try:
            if lines.get("Sibling 2").sex == 'M':
                if "Sibling 2 Mate" in lines:
                    lines.update({"Sibling 2": Person("Sibling 2 Mate", "Sibling 2", None, lines.get("Sibling 2 Child 2 (Through Adoption)"))})
                else:
                    lines.update({"Sibling 2": Person(None, "Sibling 2", None, lines.get("Sibling 2 Child 2 (Through Adoption)"))})
            else:
                if "Sibling 2 Mate" in lines:
                    lines.update({"Sibling 2": Person("Sibling 2", "Sibling 2 Mate", None, lines.get("Sibling 2 Child 2 (Through Adoption)"))})
                else:
                    lines.update({"Sibling 2": Person("Sibling 2", None, None, lines.get("Sibling 2 Child 2 (Through Adoption)"))})
        except:
            if "Sibling 2 Mate" in lines:
                lines.update({"Sibling 2": Person("Sibling 2", "Sibling 2 Mate", None, lines.get("Sibling 2 Child 2 (Through Adoption)"))})
            else:
                lines.update({"Sibling 2": Person("Sibling 2", None, None, lines.get("Sibling 2 Child 2 (Through Adoption)"))})
    if "Sibling 2 Child 3" not in done and "Sibling 2 Child 3" in lines:
        # go up
        done.append("Sibling 2 Child 3")
        if lines.get("Sibling 2").sex == 'M':
            if "Sibling 2 Mate" in lines:
                lines.update({"Sibling 2": Person("Sibling 2 Mate", "Sibling 2", None, lines.get("Sibling 2 Child 3"))})
            else:
                lines.update({"Sibling 2": Person(None, "Sibling 2", None, lines.get("Sibling 2 Child 3"))})
        else:
            if "Sibling 2 Mate" in lines:
                lines.update({"Sibling 2": Person("Sibling 2", "Sibling 2 Mate", None, lines.get("Sibling 2 Child 3"))})
            else:
                lines.update({"Sibling 2": Person("Sibling 2", None, None, lines.get("Sibling 2 Child 3"))})
    mapRelationsLevel2(lines, [])


fileDF = pd.read_csv("data/F1.csv")
# print(fileDF)
# mapRelationsLevel1()
selfDF = fileDF.iloc[0]
# print(fileDF.iloc[0])

# selfInfo = Info(selfDF.iloc[0], selfDF.iloc[1], (True if selfDF.iloc[2] == 'Y' else False), selfDF.iloc[3], selfDF.iloc[4], selfDF.iloc[5])
# print(selfInfo)
# print(fileDF)
infoList = []
for index, row in fileDF.iterrows():
    infoList.append(Info)


# myFile = open("data/F1.txt", "r")
# lines = {}
# next(myFile)
# for aRow in myFile:
#     line = aRow.replace('\n', '').split('\t')
#     lines.update({str(line[0]): Info(line[0], line[1], line[2], line[3], line[4], line[5])})
# myFile.close()

# print(lines.get("Self"))
# print(lines)

# done = []
# mapRelationsLevel1(lines, done)
# print(lines)

# grandparent = Digraph(name='grandparent', comment='f1.txt', format="png")
# parent = Digraph(name='parent')
# you = Digraph(name='self')
# child = Digraph(name='child')

# prev = None
# p = lines.get("Self")
# while p.children is not None:
#     p = lines.get(p.children[0])
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
#     # print("p:{}".format(type(p)))
#     if p.mother is not None and p.father is not None:
#         children = lines.get(p.mother).children.copy()
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
#             p = lines.get(p.mother).children[0]
#             layer -= 1
#         else:
#             p = lines.get(p.mother)
#             layer += 1
#     else:
#         p = p.mother


# grandparent.subgraph(parent)
# grandparent.subgraph(you)
# grandparent.subgraph(child)
# print(grandparent.source)
# grandparent.render(view=True)
# dot.node(p.info.relation, shape=('box' if p.info.sex == 'M' else 'circle'), color=('blue' if p.info.sex == 'M' else 'pink'))

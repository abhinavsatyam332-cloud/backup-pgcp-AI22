'''
Q.2.In English, present participle is formed by adding suffix -ing to infinite form: go -> going. A simple set of rules can be given as follows:
 a. If the verb ends in e, drop the e and add ing
 b. If the verb ends in ie, change ie to y and add ing
Write a function make_ing_form() which accepts a list of verbs and returns a dictionary with verb : present participle

'''

def getPresentParticiple(word):
    if word.endswith("ie"):
        res = word.replace("ie","y")
        res += "ing"
    elif word.endswith("e"):
        res = word.replace("e", "ing")
    else:
        res = word + "ing"
    return res

print(getPresentParticiple("Role"))
print(getPresentParticiple("sie"))
print(getPresentParticiple("Go"))

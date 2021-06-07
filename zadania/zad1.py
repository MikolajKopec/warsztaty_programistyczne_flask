import random


names = ("Franek","Marek","Zbyszek","Asia","Basia","Kasia",)
surnames = ("Banach","Currie","Kowalski","Studencki",)
for each in names:
    if each[-1] == 'a':
        print(each)
def looks_like_polish_surname(s):
    for each in surnames:
        polish_suffixes = ('ski','cki')
        for each in polish_suffixes:
            if s.endswith(each):
                return True
        return False
for each in surnames:
    if looks_like_polish_surname(each):
        print(each)
people=[]

# for n in names:
#     for s in surnames:
#         people.append((n,s,))
# for each in people:
#     print(each)
for n in names:
    for s in surnames:
        if n[-1] == 'a' and looks_like_polish_surname(s):
            s=s[:-1]+'a'
        people.append((n,s,))
for each in people:
    print(each)

def create_a_person(names,surnames):
    x = random.randint(0,len(names)-1)
    random_name = names[x]
    x =random.randint(0,len(surnames)-1)
    random_surname = surnames[x]
    if random_name[-1]=='a' and looks_like_polish_surname(random_surname):
        random_surname=random_surname[:-1]+'a'
    return f"{random_name} {random_surname}"
print (create_a_person(names,surnames))
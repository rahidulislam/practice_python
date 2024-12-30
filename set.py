skills = set()
if not skills:
    print("empty Set is falsy")
else:
    print("Set is not empty")

skills = set(['Python','Java','C++','Ruby','Python'])
print(skills)
print(len(skills))

ratings = {1,2,3,4,5}
rating =1
if rating in ratings:
    print(f"rating {rating} is available")

skills.add('SQL')
print(skills)

skills.remove('Java')
print(skills)
skills.discard('Java')
print(skills)
skill =skills.pop()
print(skill)

# To make a set immutable, use frozenset
# skills = frozenset(skills)
# skills.add('Django')

for skill in skills:
    print(skill)

# to access a set by index, use enumerate
for index,skill in enumerate(skills):
    print(f"{index}:{skill}")
# set comprehension
skills = {'Python','Java','C++','Ruby','Python'}
new_skills = {skill.lower() for skill in skills}
print(new_skills)

tags = {'python','java','c++','ruby','numpy','pandas'}
new_tags = {tag for tag in tags if tag!='numpy'}
print(new_tags)

# union
s1 = {1,2,3}
s2= {3,4,5}
s= s1.union(s2)
# s= s1 | s2
print(s)

# intersection
s3 = s1.intersection(s2)
# s3 = s1 & s2
print(s3)

# difference
s4 = s1.difference(s2)
# s4 = s1-s2
print(s4)

# symmetric difference
s5 =s1.symmetric_difference(s2)
# s5 = s1 ^ s2
print(s5)
s6= {1,2,3}
s7 = {1,2,3,4,5}
# subset = s6.issubset(s7)
subset = s6 <= s7
print(subset)
# superset = s7.issuperset(s6)
superset = s7 >= s6
print(superset)

# isdisjoint
s8 = {1,2,3,5}
s9= {4,5,6,6}
disjoint = s8.isdisjoint(s9)
print(disjoint)

import math

AVOID = -1
NEUTRAL = 0
PREFERRED = 1

# find the intersection of n sets
def intersection(first, *others):
    return set(first).intersection(*others)

def separate_students(preferences, group_size):
    students = list(preferences.keys())
    for student in preferences:
        if student not in placed:
            avoid = []
            for i, rating in enumerate(preferences[student]):
                if rating == AVOID:
                    avoid.append(students[i-1])
            if len(avoid):
                for person in avoid:
                    if person not in placed:
                        groups.sort(key = len)
                        for group in groups:
                            if len(group) != group_size:
                                if person not in group:
                                    group.append(person)
                                    placed.append(person)
                                    break
                if student not in placed:
                    groups.sort(key = len)
                    for group in groups:
                        if len(group) != group_size:
                            if student not in group and not any(dude in group for dude in avoid):
                                group.append(student)
                                placed.append(student)
                                break

def fill_students(preferences, group_size):
    students = list(preferences.keys())
    for student in preferences:
        if student not in placed:
            matches = []
            for i, rating in enumerate(preferences[student]):
                if rating == PREFERRED:
                    matches.append(students[i-1])
            groups.sort(key = len)
            for group in groups:
                if len(group) != group_size:
                    if student not in group and any(dude in group for dude in matches):
                        group.append(student)
                        placed.append(student)
                        break

    for student in preferences:
        if student not in placed:
            groups.sort(key = len)
            for group in groups:
                if len(group) != group_size:
                    group.append(student)
                    placed.append(student)
                    break
            

# Load preferences from the 'preferences.py' file
from preferences import pairing_preferences, project_preferences

group_size = 5
groups = [[] for _ in range(len(pairing_preferences) // group_size + 1)]
group_types = [[] for _ in range(len(pairing_preferences) // group_size + 1)]
placed = []

project_options = 2
projects = [[] for _ in range(project_options)]
for student in project_preferences:    
    if project_preferences[student][0] >= 3:
        projects[0].append(student)
    if project_preferences[student][1] >= 3:
        projects[1].append(student)
    if project_preferences[student][0] <= 2 and project_preferences[student][1] <= 2:
        projects[0].append(student)
        projects[1].append(student)


# convert to sets, find difference (clear preference) and intersection (neutral)
projects_sets = {}
projects_sets['1'] = set(projects[0]).difference(set(projects[1]))
projects_sets['2'] = set(projects[1]).difference(set(projects[0]))
projects_sets['both'] = set(projects[0]).intersection(set(projects[1]))
print(projects_sets)
i = 0
num = math.ceil(len(projects_sets['1'])//group_size)
while i < num:
    group_types[i] = '1'
    i += 1
num = math.ceil(len(projects_sets['2'])//group_size)
while i < num:
    group_types[i] = '2'
    i += 1


separate_students(pairing_preferences, group_size)
print(groups)
fill_students(pairing_preferences, group_size)

for i, group in enumerate(groups):
    print(f"Group {i+1}: {group}")

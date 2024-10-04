# all_levels_for_majors = {}

# with open("all_majors.txt") as file:
#     calc_category = ""
#     for line in file:
#         if line[0:12] == "Pre-Calculus":
#             calc_category = "Pre-Calculus"
#         elif line[0:14] == "Calculus Ready":
#             calc_category = "Calculus Ready"
#         elif line[0:17] == "Extended Calculus":
#             calc_category = "Extended Calculus"
#         if line[0:2] == "- ":
#             all_levels_for_majors[line.lstrip("- ").rstrip()] = calc_category
# print(all_levels_for_majors)

# req_units = {}
# with open("all_units_for_majors.txt") as file:
#     for line in file:
#         next_line = 0
#         vals = line.split(":")
#         #print(len(vals))
#         #print(vals)
#         units_clean = []
#         for index, units in enumerate(vals[1:]):
#             for idx, unit in enumerate(units.split(", ")):
#                 unit_stripped = unit.lstrip().rstrip()
#                 calc_level = {}

#                 if unit_stripped == "pre-calculus/calculus ready": #in other use if dict.keys == None
#                     calc_level_units = []
#                     for j in vals[index + 2].split(","):
#                         x = j.lstrip().rstrip(". extended calculus")
#                         calc_level_units.append(x)
#                     calc_level["pre-calculus"] = calc_level_units
#                     calc_level["calculus ready"] = calc_level_units
#                     calc_level_units = []
#                     for k in vals[index + 3].split(","):
#                         x = k.lstrip().rstrip()
#                         calc_level_units.append(x)
#                     calc_level["extended calculus"] = calc_level_units
#                     #print(calc_level)
#                     req_units[vals[0]] = calc_level
#                     next_line = 1
#                     break
#                 else:
#                     units_clean.append(unit_stripped)   
#                     req_units[vals[0]] = units_clean
#             if next_line == 1:
#                 break
# print(req_units)

# all_majors_categories = []
# with open("all_majors.txt") as file:
#     for line in file:
#         if line[0:2] == "- ":
#             all_majors_categories.append(line.lstrip("- ").rstrip())
# print(all_majors_categories)

# units_with_calc_category = {}
# with open("units_with_calc_level.txt") as file:
#     category = ""
#     for index, line in enumerate(file):
#         if index % 2 == 0:
#             category = line.lstrip("- ")
#             category = category[:-9].lower()
#         else:
#             ls = []
#             for unit in line.split(", "):
#                 ls.append(unit.lstrip().rstrip())
#             units_with_calc_category[category] = ls
# print(units_with_calc_category)

# domestic_maths = []
# with open("domestic_maths.txt") as file:
#     for line in file:
#         if line[0:2] == "- ":
#             domestic_maths.append(line.lstrip("- ").rstrip())
# print(domestic_maths)

# support_pathways_dict = {}
# with open("support_pathways.txt") as file:
#     support_pathways_dict['Pre-Calculus'] = {}
#     support_pathways_dict['Calculus Ready'] = {}
#     support_pathways_dict['Pre-Calculus']['Calculus Ready'] = []
#     support_pathways_dict['Pre-Calculus']['Extended Calculus'] = []
#     support_pathways_dict['Calculus Ready']['Extended Calculus'] = []
#     for index, line in enumerate(file):
#         if index == 1 or index == 2:
#             support_pathways_dict['Pre-Calculus']['Calculus Ready'].append(line.rstrip())
#         if index == 4:
#             support_pathways_dict['Calculus Ready']['Extended Calculus'].append(line.rstrip())
#         if index == 6 or index == 7:
#             support_pathways_dict['Pre-Calculus']['Extended Calculus'].append(line.rstrip())

# print(support_pathways_dict)

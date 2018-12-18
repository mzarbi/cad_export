st = """id	Type	name	styleCode	Techno	boxDst	boxSrc	link_ID	scenario_ID	trench_ID	id	MaxDimaterSheath1	MaxDimaterSheath2	MaxPossibleSheath1	MaxPossibleSheath2	Cost	deploymentType	id2	Length	name	state	cable_Link	link	scenario_ID	trenchModelModel_ID	id	cost	depth_Max	depth_Min	length_Max	length_Min	name	id	address	deploymentType	equipmentType	id2	isOutdoor	lat	lon	NAME	state	styleCode	tag	tag_building	BuildingID	CableDrawinBoxModelID	scenario_ID	iSite	id	address	deploymentType	equipmentType	id2	isOutdoor	lat	lon	NAME	state	styleCode	tag	tag_building	BuildingID	CableDrawinBoxModelID	scenario_ID	iSite"""
s = []
counter = 0

"""
for i in st.split("	"):
    if i in s:
        print i + "_" + str(counter)  + ","
        counter += 1
    else:
        print i + ","
        s.append(i)
v = 0
for i in st.split("	"):
    if i in s:
        print "        self." + i + "_" + str(counter) + " = None"
        counter += 1
    else:
        print "        self." + i + " = None"
        s.append(i)
    v+=1
"""

v = 0
for i in st.split("	"):
    print "        self." + i + "_" + str(v) + " = arr[" + str(v) + "]"
    v+=1
print 555555555555555555555555555555
v = 0
for i in st.split("	"):
    if i in s:
        print "        self." + i + "_" + str(counter) + " = None"
        counter += 1
    else:
        print "        self." + i + " = None"
        s.append(i)
    v+=1


from pyproj import Proj, transform


def project_point(point):
    outProj = Proj(init='epsg:32632')
    inProj = Proj(init='epsg:4326')

    return transform(inProj, outProj,point[1] , point[0])

def project_point_collection(point_collection):
    tmp = []
    for point in point_collection:
        tmp.append(project_point(point))

    return tmp

def transform_array(arr):
    l = len(arr)
    tmp = []
    for i in range(l/2):
        tmp.append((arr[i],arr[l/2+i]))
    return tmp
import pygeoj
from shapely.geometry import Polygon, LineString
import numpy as np
from dxf_playground.render.coordinates import BoundingBox


class road:
    def __init__(self,properties= None,geometry=None):
        self.properties = properties
        self.geometry = geometry

    def isInside(self,bounding_box):
        poly = Polygon(bounding_box)
        return poly.contains(LineString(self.geometry))

    def draw_road(self,cx,cy,bloc):
        geo = [(i[0] - cx, i[1] - cy) for i in self.geometry]
        """
        bloc.add_lwpolyline(
            geo,
            dxfattribs={'color': 7,
                        'layer': "roads",
                        'linetype': "DASHED"})
        """

        line = LineString(geo)
        xy_right = line.parallel_offset(3.2, 'right', 0, 3, 1).coords.xy

        xy_left = line.parallel_offset(3.2, 'left', 0, 3, 1).coords.xy

        coords = []
        for i in range(len(xy_right[0])):
            coords.append((xy_right[0][i], xy_right[1][i]))

        bloc.add_lwpolyline(
            coords,
            dxfattribs={'color': 7,
                        'layer': "roads", })

        coords = []
        for i in range(len(xy_left[1])):
            coords.append((xy_left[0][i], xy_left[1][i]))

        bloc.add_lwpolyline(
            coords,
            dxfattribs={'color': 7,
                        'layer': "roads", })


class road_collection(list):
    def __init__(self,dwg,modelspace,resource_path,bounding_box):
        list.__init__(self)
        self.dwg = dwg
        self.modelspace = modelspace
        self.resources_path = resource_path
        self.bounding_box = bounding_box

    def from_feature_file(self):
        huge_map = pygeoj.load(filepath=self.resources_path + "/feature_files/huge_map_lines_utm.geojson")
        for feature in huge_map:
            tmp = road(feature.properties,feature.geometry.coordinates)
            self.append(tmp)

    def query_roads(self):
        tmp = road_collection(self.dwg,self.modelspace,self.resources_path,self.bounding_box)
        for i in self:
            if i.isInside(self.bounding_box) == True:
                tmp.append(i)
        return tmp

    def inside_bounding_box(self):
        tmp = road_collection(self.dwg,self.modelspace,self.resources_path,self.bounding_box)
        for i in self:
            if self.bounding_box.contains(LineString(i.geometry)):
                tmp.append(i)
            elif self.bounding_box.intersection(LineString(i.geometry)):
                if str(type(self.bounding_box.intersection(
                        LineString(i.geometry)))) == "<class 'shapely.geometry.linestring.LineString'>":
                    inte = self.bounding_box.intersection(LineString(i.geometry)).coords
                    rd = road(i.properties,inte)
                    tmp.append(rd)
                else:
                    for line in self.bounding_box.intersection(LineString(i.geometry)):
                        inte = line.coords
                        rd = road(i.properties,inte)
                        tmp.append(rd)

        return tmp

    def bbox(self):
        l = []
        for i in self:
            for j in i.geometry:
                l.append(j)
        return BoundingBox(np.array(l))

    def draw(self):
        bbox = self.bbox()
        center = bbox.center
        bloc = self.dwg.blocks.new(name="roads.block1.A4")
        self.modelspace.add_blockref("roads.block1.A4",
                                     (-95., 0.),
                                     dxfattribs={
                                         "xscale": 571. / bbox.width,
                                         "yscale": 458. / bbox.height})

        for i in self:
            try:
                i.draw_road(center[0],center[1],bloc)
            except:
                pass
        bloc = self.dwg.blocks.new(name="roads.block2.A4")
        self.modelspace.add_blockref("roads.block1.A4",
                                     (-95 + 840 + 151., 0.),
                                     dxfattribs={
                                         "xscale": 571. / bbox.width,
                                         "yscale": 458. / bbox.height})

        try:
            i.draw_road(center[0], center[1], bloc)
        except:
            pass

        bloc = self.dwg.blocks.new(name="roads.block3.A4")
        self.modelspace.add_blockref("roads.block1.A4",
                                     (-95. -840 - 146, 0.),
                                     dxfattribs={
                                         "xscale": 571. / bbox.width,
                                         "yscale": 458. / bbox.height})

        try:
            i.draw_road(center[0], center[1], bloc)
        except:
            pass
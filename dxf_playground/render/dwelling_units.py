import pygeoj
from shapely.geometry import Polygon, LineString
import numpy as np
from dxf_playground.render.coordinates import BoundingBox

class building:
    def __init__(self, properties=None, geometry=None):
        self.properties = properties
        self.geometry = geometry


    def draw_building(self, cx, cy,bloc):
        polygon = Polygon(self.geometry[0][0])
        if polygon.area < 5000:
            geo = [(i[0] - cx, i[1] - cy) for i in self.geometry[0][0]]

            bloc.add_lwpolyline(
                geo,
                dxfattribs={'color': 7,
                            'layer': "building"})

            bloc.add_text("DU ",
                                     dxfattribs={'color': 7}).set_pos(
                BoundingBox(np.array(geo)).center,
                align='CENTER')

class building_collection(list):
    def __init__(self, dwg,modelspace,resource_path,bounding_box,bbox):
        list.__init__(self)

        self.dwg = dwg
        self.modelspace = modelspace
        self.resources_path = resource_path
        self.bounding_box = bounding_box
        self.bbox = bbox

    def from_feature_file(self):
        huge_map = pygeoj.load(
            filepath=self.resources_path + "/feature_files/huge_map_polygons_utm.geojson")
        for feature in huge_map:
            tmp = building(feature.properties, feature.geometry.coordinates)
            self.append(tmp)

    def inside_bounding_box(self):
        tmp = building_collection(self.dwg,self.modelspace,self.resources_path,self.bounding_box,self.bbox)
        for i in self:

            if self.bounding_box.contains(LineString(i.geometry[0][0])):
                tmp.append(i)
            """
            elif self.bounding_box.intersection(LineString(i.geometry[0][0])):
                if str(type(self.bounding_box.intersection(
                        LineString(i.geometry[0][0])))) == "<class 'shapely.geometry.linestring.LineString'>":
                    inte = self.bounding_box.intersection(LineString(i.geometry[0][0])).coords
                    inte = [(d[0], d[1]) for d in inte]
                    if len(inte) == 2:
                        inte.append(inte[0])
                    rd = building(i.properties,inte)
                    tmp.append(rd)
                else:
                    for line in self.bounding_box.intersection(LineString(i.geometry[0][0])):
                        inte = line.coords
                        inte = [(d[0], d[1]) for d in inte]
                        if len(inte) == 2:
                            inte.append(inte[0])
                        rd = building(i.properties,inte)
                        tmp.append(rd)
            """
        return tmp

    def draw(self):
        bloc = self.dwg.blocks.new(name="buildings.block1.A4")
        self.modelspace.add_blockref("buildings.block1.A4",
                                     (-95., 0.),
                                     dxfattribs={
                                         "xscale": 571. / self.bbox.width,
                                         "yscale": 458. / self.bbox.height})

        for i in self:
            try:
                i.draw_building(self.bbox.center[0], self.bbox.center[1], bloc)
            except:
                pass
        bloc = self.dwg.blocks.new(name="buildings.block2.A4")
        self.modelspace.add_blockref("buildings.block2.A4",
                                     (-95 + 840 + 151., 0.),
                                     dxfattribs={
                                         "xscale": 571. / self.bbox.width,
                                         "yscale": 458. / self.bbox.height})

        for i in self:
            try:
                i.draw_building(self.bbox.center[0], self.bbox.center[1], bloc)
            except:
                pass

        bloc = self.dwg.blocks.new(name="buildings.block3.A4")
        self.modelspace.add_blockref("buildings.block3.A4",
                                     (-95. - 840 - 146, 0.),
                                     dxfattribs={
                                         "xscale": 571. / self.bbox.width,
                                         "yscale": 458. / self.bbox.height})

        for i in self:
            try:
                i.draw_building(self.bbox.center[0], self.bbox.center[1], bloc)
            except:
                pass
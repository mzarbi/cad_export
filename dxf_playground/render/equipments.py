from shapely.geometry import Polygon, LineString
import numpy as np

from dxf_playground.data_access.data_query import DB_Handler
from dxf_playground.render.coordinates import BoundingBox
from dxf_playground.utils.projections import project_point_collection


class equipment:
    def __init__(self, properties=None, geometry=None):
        self.properties = properties
        self.geometry = geometry


    def draw_equipment(self, cx, cy,bloc):
        geo = [(i[0] - cx, i[1] - cy) for i in self.geometry]
        bloc.add_lwpolyline(
            geo,
            dxfattribs={'color': 2})
        cent = BoundingBox(np.array(geo)).center
        bloc.add_text(str(self.properties.length) + "m",
                      dxfattribs={'color': 7}).set_pos(
            cent,
            align='CENTER')

        bloc.add_text(self.properties.name,
                      dxfattribs={'color': 7}).set_pos(
            (cent[0],cent[1] -5),
            align='CENTER')

class equipment_collection(list):
    def __init__(self, dwg,modelspace,scenario_id,bounding_box,bbox):
        list.__init__(self)

        self.dwg = dwg
        self.modelspace = modelspace
        self.scenario_id = scenario_id
        self.bounding_box = bounding_box
        self.bbox = bbox

    def from_data_base(self):
        hndl = DB_Handler()
        result = hndl.query_cables(self.scenario_id)
        for res in result:
            cp = equipment_properties()
            cp.fromArray(res)


            c = equipment(cp,project_point_collection([(cp.lat, cp.lon), (cp.lat_19, cp.lon_20)]))
            self.append(c)
        hndl.close()

    def inside_bounding_box(self):
        tmp = equipment_collection(self.dwg, self.modelspace, self.scenario_id, self.bounding_box,self.bbox)
        for i in self:
            if self.bounding_box.contains(LineString(i.geometry)):
                tmp.append(i)
            elif self.bounding_box.intersection(LineString(i.geometry)):
                if str(type(self.bounding_box.intersection(
                        LineString(i.geometry)))) == "<class 'shapely.geometry.linestring.LineString'>":
                    inte = self.bounding_box.intersection(LineString(i.geometry)).coords
                    rd = equipment(i.properties, inte)
                    tmp.append(rd)
                else:
                    for line in self.bounding_box.intersection(LineString(i.geometry)):
                        inte = line.coords
                        rd = equipment(i.properties, inte)
                        tmp.append(rd)

        return tmp

    def draw(self):
        bloc = self.dwg.blocks.new(name="cables.block1.A4")
        self.modelspace.add_blockref("cables.block1.A4",
                                     (-95., 0.),
                                     dxfattribs={
                                         "xscale": 571. / self.bbox.width,
                                         "yscale": 458. / self.bbox.height})

        for i in self:
            i.draw_cable(self.bbox.center[0], self.bbox.center[1], bloc)


class equipment_properties:
    def __init__(self):
        pass

    def fromArray(self,arr):
        pass

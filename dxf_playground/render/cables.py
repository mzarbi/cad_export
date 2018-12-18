import pygeoj
from shapely.geometry import Polygon, LineString
import numpy as np

from dxf_playground.data_access.data_query import DB_Handler
from dxf_playground.render.coordinates import BoundingBox
from dxf_playground.utils.projections import project_point_collection


class cable:
    def __init__(self, properties=None, geometry=None):
        self.properties = properties
        self.geometry = geometry


    def draw_cable(self, cx, cy,bloc):
        geo = [(i[0] - cx, i[1] - cy) for i in self.geometry]

        colormap = [96, 48, 2, 36, 4, 72, 12, 336, 16, 120, 84, 8, 576, 24, 564, 168, 156, 192, 264, 312]
        color = colormap.index(int(self.properties.Nb_FO_76))
        bloc.add_lwpolyline(
            geo,
            dxfattribs={'color': color})
        cent = BoundingBox(np.array(geo)).center
        bloc.add_text(str(self.properties.length_6) + "m",
                      dxfattribs={'color': 7}).set_pos(
            cent,
            align='CENTER')

        bloc.add_text(self.properties.name_7,
                      dxfattribs={'color': 7,'height': 0.35}).set_pos(
            (cent[0],cent[1] -1.5),
            align='CENTER')
        bloc.add_text(self.properties.Description_71,
                      dxfattribs={'color': 7,'height': 0.35}).set_pos(
            (cent[0], cent[1] - 3),
            align='CENTER')

class cable_collection(list):
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
            cp = cable_properties()
            cp.fromArray(res)

            c = cable(cp,project_point_collection([(cp.lat_40, cp.lon_41), (cp.lat_57, cp.lon_58)]))
            self.append(c)
        hndl.close()

    def inside_bounding_box(self):
        tmp = cable_collection(self.dwg, self.modelspace, self.scenario_id, self.bounding_box,self.bbox)
        for i in self:
            if self.bounding_box.contains(LineString(i.geometry)):
                tmp.append(i)
            elif self.bounding_box.intersection(LineString(i.geometry)):
                if str(type(self.bounding_box.intersection(
                        LineString(i.geometry)))) == "<class 'shapely.geometry.linestring.LineString'>":
                    inte = self.bounding_box.intersection(LineString(i.geometry)).coords
                    rd = cable(i.properties, inte)
                    tmp.append(rd)
                else:
                    for line in self.bounding_box.intersection(LineString(i.geometry)):
                        inte = line.coords
                        rd = cable(i.properties, inte)
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


class cable_properties:
    def __init__(self):
        pass

    def fromArray(self,arr):
        self.id_0 = arr[0]
        self.directionInversed_1 = arr[1]
        self.id2_2 = arr[2]
        self.initialEq1_3 = arr[3]
        self.initialEq2_4 = arr[4]
        self.isIndoor_5 = arr[5]
        self.length_6 = arr[6]
        self.name_7 = arr[7]
        self.state_8 = arr[8]
        self.type_9 = arr[9]
        self.cableModel_ID_10 = arr[10]
        self.link_11 = arr[11]
        self.subtubes_ID_12 = arr[12]
        self.id_13 = arr[13]
        self.name_14 = arr[14]
        self.Sheat_ID_15 = arr[15]
        self.sheathModel_ID_16 = arr[16]
        self.id_17 = arr[17]
        self.MaximumSubtubesCapacity_18 = arr[18]
        self.name_19 = arr[19]
        self.position_20 = arr[20]
        self.position2_21 = arr[21]
        self.sheathModel_ID_22 = arr[22]
        self.trench_ID_23 = arr[23]
        self.id_24 = arr[24]
        self.Type_25 = arr[25]
        self.name_26 = arr[26]
        self.styleCode_27 = arr[27]
        self.Techno_28 = arr[28]
        self.boxDst_29 = arr[29]
        self.boxSrc_30 = arr[30]
        self.link_ID_31 = arr[31]
        self.scenario_ID_32 = arr[32]
        self.trench_ID_33 = arr[33]
        self.id_34 = arr[34]
        self.address_35 = arr[35]
        self.deploymentType_36 = arr[36]
        self.equipmentType_37 = arr[37]
        self.id2_38 = arr[38]
        self.isOutdoor_39 = arr[39]
        self.lat_40 = arr[40]
        self.lon_41 = arr[41]
        self.NAME_42 = arr[42]
        self.state_43 = arr[43]
        self.styleCode_44 = arr[44]
        self.tag_45 = arr[45]
        self.tag_building_46 = arr[46]
        self.BuildingID_47 = arr[47]
        self.CableDrawinBoxModelID_48 = arr[48]
        self.scenario_ID_49 = arr[49]
        self.iSite_50 = arr[50]
        self.id_51 = arr[51]
        self.address_52 = arr[52]
        self.deploymentType_53 = arr[53]
        self.equipmentType_54 = arr[54]
        self.id2_55 = arr[55]
        self.isOutdoor_56 = arr[56]
        self.lat_57 = arr[57]
        self.lon_58 = arr[58]
        self.NAME_59 = arr[59]
        self.state_60 = arr[60]
        self.styleCode_61 = arr[61]
        self.tag_62 = arr[62]
        self.tag_building_63 = arr[63]
        self.BuildingID_64 = arr[64]
        self.CableDrawinBoxModelID_65 = arr[65]
        self.scenario_ID_66 = arr[66]
        self.iSite_67 = arr[67]
        self.id_68 = arr[68]
        self.Attenuation_1310_69 = arr[69]
        self.Attenuation_1550_70 = arr[70]
        self.Description_71 = arr[71]
        self.FOPerRibbon_72 = arr[72]
        self.Height_73 = arr[73]
        self.Max_Length_74 = arr[74]
        self.NbUnitPerTube_75 = arr[75]
        self.Nb_FO_76 = arr[76]
        self.Nb_Slott_77 = arr[77]
        self.Nb_Tubes_78 = arr[78]
        self.Price_79 = arr[79]
        self.Reference_80 = arr[80]
        self.Weight_81 = arr[81]
        self.Width_82 = arr[82]
        self.application_83 = arr[83]
        self.standard_84 = arr[84]
        self.structure_85 = arr[85]
        self.Constructor_86 = arr[86]
        self.Code_87 = arr[87]
        self.DeploymentType_88 = arr[88]
import mysql.connector

class DB_Handler:
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost",  # your host, usually localhost
                                          user="root",  # your username
                                          passwd="root",  # your password
                                          db="nestOptics")  # name of the data base
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def query_cables(self,scenario_id):

        query = "select * from cable,subtubes,sheath,Cable_Link,cabledrawinbox c1,cabledrawinbox c2, cable_model where subtubes.id= cable.subtubes_ID and sheath.id = subtubes.Sheat_ID and sheath.trench_ID = Cable_Link.trench_ID and c1.id= Cable_Link.boxSrc and c2.id= Cable_Link.boxDst and c1.scenario_ID = c2.scenario_ID and cable_model.id = cable.cableModel_ID and c1.scenario_ID =" + str(scenario_id)
        self.cur.execute(query)
        imp = []
        for row in self.cur.fetchall():
            imp.append(row)
        return imp

    def query_subscriber_dwelling(self,scenario_id):

        query = "select * from cable,cable_model,building,subtubes,sheath,Cable_Link,cabledrawinbox where subtubes.id= cable.subtubes_ID and sheath.id = subtubes.Sheat_ID and sheath.trench_ID = Cable_Link.trench_ID and cabledrawinbox.id= Cable_Link.boxDst  and cabledrawinbox.id=building.Box_ID and cable_model.id = cable.cableModel_ID and cabledrawinbox.scenario_ID =" + str(scenario_id)
        self.cur.execute(query)
        imp = []
        for row in self.cur.fetchall():
            imp.append(row)
        return imp

    def query_splicer(self,scenario_id):

        query = "select * from cabledrawinbox,splice_closure,splicingclosure_model where cabledrawinbox.id = splice_closure.CableDrawnBox_ID and splicingclosure_model.id= splice_closure.Splice_ClosureModel_ID and cabledrawinbox.scenario_ID = " + str(scenario_id)
        self.cur.execute(query)
        imp = []
        for row in self.cur.fetchall():
            imp.append(row)
        return imp

    def query_fdh(self,scenario_id):

        query = "select * from terminalbox, cabledrawinbox where terminalbox.CableDrawnBox_ID = cabledrawinbox.id and cabledrawinbox.scenario_ID=" + str(scenario_id)
        self.cur.execute(query)
        imp = []
        for row in self.cur.fetchall():
            imp.append(row)
        return imp

    def query_box(self,scenario_id):

        query = "select * from Cable_Link,trench,trenchmodel,cabledrawinbox c1,cabledrawinbox c2   where Cable_Link.trench_ID = trench.id and trenchmodel.id = trench.trenchModelModel_ID and c1.id = Cable_Link.boxSrc and c2.id = Cable_Link.boxDst  and trench.scenario_ID=" + str(scenario_id)
        self.cur.execute(query)
        imp = []
        for row in self.cur.fetchall():
            imp.append(row)
        return imp

    def query_olt(self,scenario_id):

        query = "select * from olt, cabledrawinbox where olt.CableDrawnBox_ID = cabledrawinbox.id and cabledrawinbox.scenario_ID = " + str(scenario_id)
        self.cur.execute(query)
        imp = []
        for row in self.cur.fetchall():
            imp.append(row)
        return imp

    def query_equipments(self,scenario_id):

        query = "select * from cable,subtubes,sheath,Cable_Link,cabledrawinbox c1,cabledrawinbox c2 where subtubes.id= cable.subtubes_ID and sheath.id = subtubes.Sheat_ID and sheath.trench_ID = Cable_Link.trench_ID and c1.id= Cable_Link.boxSrc and c2.id= Cable_Link.boxDst and c1.scenario_ID = c2.scenario_ID and c1.scenario_ID = " + str(scenario_id)
        self.cur.execute(query)
        imp = []
        for row in self.cur.fetchall():
            imp.append(row)
        return imp

    def query_trenches(self,scenario_id):

        query = "select * from Cable_Link,trench,trenchmodel,cabledrawinbox c1,cabledrawinbox c2   where Cable_Link.trench_ID = trench.id and trenchmodel.id = trench.trenchModelModel_ID and c1.id = Cable_Link.boxSrc and c2.id = Cable_Link.boxDst  and trench.scenario_ID=" + str(scenario_id)
        self.cur.execute(query)
        imp = []
        for row in self.cur.fetchall():
            imp.append(row)
        return imp




if __name__ == "__main__":
    hndl = DB_Handler()
    hndl.query_cables(3)
    hndl.close()
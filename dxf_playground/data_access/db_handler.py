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

    def queryGeography(self,scenario_id):
        self.cur.execute("DESC geographicalzone")
        for row in self.cur.fetchall():
            print row
        self.cur.execute("SELECT * FROM geographicalzone WHERE geographicalzone.scenario_ID = " + str(scenario_id))
        imp = []
        for row in self.cur.fetchall():
            print row
            imp.append(row)
        return imp

    def queryMeta(self, scenario_id):
        # Use all the SQL you like
        self.cur.execute("SELECT * FROM scenario WHERE scenario.id = " + str(scenario_id))
        imp = []
        for row in self.cur.fetchall():
            imp.append(row[0])  # id
            imp.append(row[1])  # date created
            imp.append(row[2])  # name
        return imp

    def queryBuildings(self, scenario_id):
        self.cur.execute("DESC building")
        for row in self.cur.fetchall():
            pass
        self.cur.execute("SELECT * FROM building WHERE building.Scenario_ID = " + str(scenario_id))
        imp = []
        for row in self.cur.fetchall():
            imp.append(row)
        return imp

    def queryBoxes(self, scenario_id):

        self.cur.execute("SELECT * FROM cabledrawinbox WHERE cabledrawinbox.scenario_ID = " + str(scenario_id))
        imp = []
        for row in self.cur.fetchall():
            imp.append(row)
        return imp

    def queryTrenches(self, scenario_id,boxes):

        self.cur.execute("SELECT * FROM Cable_Link,trench WHERE Cable_Link.trench_ID = trench.id and Cable_Link.scenario_ID = " + str(scenario_id))
        imp = []
        for row in self.cur.fetchall():
            imp.append(row)
        imp_ = []
        c = 0
        for i in imp:
            dst = i[5]
            src = i[6]
            imp_.append([i,self.find_box(boxes,dst),self.find_box(boxes,src)])
        return imp_
    @staticmethod
    def find_box(boxes,id):
        for box in boxes:
            if box[0] == id:
                return box


if __name__ == "__main__":
    pass
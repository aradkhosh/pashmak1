import mysql.connector

class Database:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                db='school',
                user='root',
                password='',
                host='localhost'
            ) 
            self.cr = self.db.cursor()
        except:
            print('error1')


class StudentInsert(Database):
    def __init__(self, name, family, birthDATE, nationalCODE, adress):
        Database.__init__(self)
        data = (name, family, birthDATE, nationalCODE, adress)
        query = """INSERT INTO student
        (name, family, birthDATE, nationalCODE, adress)
        VALUES
        (%s,%s,%s,%s,%s)"""
        self.cr.execute(query, data)
        self.db.commit()

        self.cr = self.cr.close()
        self.db = self.db.close()


class StudentDelet(Database):
    def __init_(self,nationalCODE):
        data = (nationalCODE,)  
        query = "DELETE FROM student WHERE id=%s"
        self.cr.execute(query, data)
        self.db.commit()

        self.cr = self.cr.close()
        self.db = self.db.close()

class StudentUpdate(Database):
    def __init__(self, colNAME, colValue, id):
        Database.__init__(self)
        data =  ()
        query = "UPDATE student SET" +colNAME +"=%s WHERE id=%s"
        self.cr.execute(query, data)
        self.db.commit()
        self.cr = self.cr.close()
        self.db = self.db.close()
        
class StudentSelect(Database):
    def __init__(self):
        Database.__init__(self)
        query = "select * from student"
        self.cr.execute(query)
        self.result = self.cr.fetchall()

        self.cr.close()
        self.db.close()

    def get(self):
        return self.result

 class StudentSearch(Database):
    def __init__(self, strValue):
        Database.__init__(self)
        strValue = '%' + strValue +'%'
        data =(strValue, strValue)
        query = """Select * FROM student
        WHERE name LIKE %s OR family LIKE %s"""

        self.cr.execute(query, data)
        self.result = self.cr.fetchall()

        self.cr.close()
        self.db.close()

    def get(self):
        return self.result


# class GradeInsert(Database):
#     def __init__(self,studentId,math,shimi,fizic,tarikh, programming):
#         Database.__init__(self)
#         data = (studentId,math,shimi,fizic,tarikh, programming)
#         query = """INSERT INTO grade
#         (studentId,math,shimi,fizic,tarikh, programming)
#         VALUES
#         (%s,%s,%s,%s,%s,%s)"""
#         self.cr.execute(query, data)
#         self.db.commit()

#         self.cr = self.cr.close
#         self.db = self.db.close

# class   GradeSearch(Database):
#     def __init__(self, studentId):
#         Database.__init__(self)
#         data =(studentId,)
#         query = """Select * FROM grade
#         WHERE studentId LIKE %s"""

#         self.cr.execute(query, data)
#         self.result = self.cr.fetchall()

#         self.cr.close()
#         self.db.close()

#     def get(self):
#         return self.result


# class GradeInsert(Database):
#     def __init__(self,studentId,math,shimi,fizic,tarikh, programming):
#         Database.__init__(self)
#         data = (studentId,math,shimi,fizic,tarikh, programming)
#         query = """INSERT INTO grade
#         (studentId,math,shimi,fizic,tarikh, programming)
#         VALUES
#         (%s,%s,%s,%s,%s,%s)"""
#         self.cr.execute(query, data)
#         self.db.commit()

#         self.cr = self.cr.close
#         self.db = self.db.close

# class GradeSearch(Database):
#     def __init__(self, studentId):
#         Database.__init__(self)
#         data =(studentId,)
#         query = """Select * FROM grade
#         WHERE studentId LIKE %s"""

#         self.cr.execute(query, data)
#         self.result = self.cr.fetchall()

#         self.cr.close()
#         self.db.close()

#     def get(self):
#         return self.result
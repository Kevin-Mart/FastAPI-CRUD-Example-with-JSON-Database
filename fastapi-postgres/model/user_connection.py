import psycopg2

class UserConnection():
    conn=None
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="fastapi_test",
                user="postgres",
                password="root",
                port="5432"
            )
        except psycopg2.OperationalError as err:
            print("Error connecting to database:", err) 
            self.conn.close()

    def wrtite_db(self, data):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO "user" (name, phone) 
                VALUES (%(name)s, %(phone)s)
            """, data)
            self.conn.commit()

    def read_db(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "user"')
            records = cursor.fetchall()
            return records
        
    def read_byid_db(self,user_id):
        with self.conn.cursor() as cursor:
            cursor.execute("""SELECT * FROM "user" WHERE id = %s;""",(user_id))
            records = cursor.fetchall()
            return records
        
    def delete_bd(self,user_id):
        with self.conn.cursor() as cursor:
            cursor.execute("""DELETE FROM "user" WHERE id = %s""",(user_id))
            self.conn.commit()

    def update_bd(self, data):
        with self.conn.cursor() as cursor:
            cursor.execute("""UPDATE "user" SET name = %(name)s, phone = %(phone)s WHERE id = %(id)s""", data)
            self.conn.commit()

    def __del__(self):
        self.conn.close()   
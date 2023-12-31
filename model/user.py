import mysql.connector
import datetime

from config import *


class User:
    def __init__(self, username):
        self.username = username


class UserManager:
    @staticmethod
    def database():
        db = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )
        return db

    def insert_user(self, user):
        db = self.database()
        c = db.cursor()
        sql = "INSERT INTO user (username) VALUES (%s)"
        val = user.username
        c.execute(sql, (val,))
        db.commit()
        c.close()
        db.close()

    def get_user(self, username):
        db = self.database()
        c = db.cursor()
        sql = "SELECT * FROM user WHERE username = %s"
        c.execute(sql, (username,))
        user = c.fetchone()
        db.commit()
        c.close()
        db.close()
        if user is None:
            return None
        return User(user[0])

    def delete_user(self, username):
        db = self.database()
        c = db.cursor()
        sql = "DELETE FROM user WHERE username = %s"
        c.execute(sql, (username,))
        print("user(s) deleted")
        db.commit()
        c.close()
        db.close()

    def update_username(self, username, new_username):
        db = self.database()
        c = db.cursor()
        sql = "UPDATE User SET username = %s WHERE username = %s"
        c.execute(sql, (new_username, username))
        db.commit()
        c.close()
        db.close()

    def update_login_info(self, username):
        db = self.database()
        c = db.cursor()
        today = datetime.date.today()

        c.execute("SELECT last_login, log_count FROM User WHERE username = %s", (username,))
        result = c.fetchone()
        if result:
            last_login, log_count = result

            if last_login == today:
                log_count += 1
            else:
                last_login = today
                log_count = 1

            c.execute("UPDATE User SET last_login = %s, log_count = %s WHERE username = %s",
                    (last_login, log_count, username))

            db.commit()

            return log_count
        else:
            print('User does not exist')

            c.close()
            db.close()

            return None

    def get_user_login_info(self, username):
        db = self.database()
        c = db.cursor()
        c.execute("SELECT log_count FROM User WHERE username = %s", (username,))
        result = c.fetchone()
        c.close()
        db.close()
        return result[0]

    def insert_user_genre(self, user, genre):
        db = self.database()
        c = db.cursor()
        sql = "INSERT INTO usergenre (username, genre) VALUES (%s,%s)"
        val = user.username
        c.execute(sql, (val, genre))
        db.commit()
        c.close()
        db.close()

    def get_user_genre(self, user):
        db = self.database()
        c = db.cursor(buffered=True)
        sql = "SELECT genre FROM usergenre WHERE username = %s"
        val = user.username
        c.execute(sql, (val,))
        db.commit()
        genres = c.fetchall()
        c.close()
        db.close()
        return genres

    def delete_user_genre(self, user, genre):
        db = self.database()
        c = db.cursor()
        sql = "DELETE FROM usergenre WHERE username = %s AND genre = %s"
        val = user.username
        c.execute(sql, (val, genre))
        db.commit()
        c.close()
        db.close()

    def is_genre_in_user_genre(self, user, genre):
        db = self.database()
        c = db.cursor(buffered=True)
        sql = "SELECT * FROM usergenre WHERE username = %s AND genre = %s"
        val = user.username
        c.execute(sql, (val, genre))
        db.commit()
        genres = c.fetchone()
        c.close()
        db.close()
        if genres is None:
            return False
        else:
            return True

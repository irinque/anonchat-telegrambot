import psycopg2
from config import HOST, USER, PASSWORD, DATABASE

class Database(object):
    
    __host = None
    __user = None
    __password = None
    __database = None
    __cursor = None
    __connection = None

    def __init__(self, host=HOST, user=USER, password=PASSWORD, database=DATABASE):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
    
    def _connect(self):
        try:
            self.__connection = psycopg2.connect(host=self.__host, user=self.__user, password=self.__password, database=self.__database)
            self.__cursor = self.__connection.cursor()
        except Exception as e:
            print("[INFO] Error:", e)

    def _commit(self):
        self.__connection.commit()

    def _close(self):
        self.__connection.close()

    def user_exists(self, user_id):
        self._connect()
        self.__cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id};")
        self._commit()
        if self.__cursor.fetchone() != None:
            self._close()
            return True
        else:
            self._close()
            return False
        
    def user_check_ban(self, user_id):
        self._connect()
        self.__cursor.execute(f"SELECT user_ban FROM users WHERE user_id = {user_id}")
        self._commit()
        if bool(self.__cursor.fetchone()[0]):
            return True
        else:
            return False
        self._close()
    def insert_user(self, user_name, user_id):
        self._connect()
        self.__cursor.execute(f"INSERT INTO users (user_name, user_id) VALUES ('{user_name}', '{user_id}')")
        self._commit()
        self._close()

db = Database()
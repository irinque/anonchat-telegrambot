import psycopg2
import time
from datetime import date
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
        self.__cursor.close()
        self.__connection.close()

    def user_exists(self, user_id):
        self._connect()
        self.__cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id};")
        self._commit()
        user = self.__cursor.fetchone()
        self._close()
        if user != None:
            return True
        else:
            return False
        
    def user_check_ban(self, user_id):
        self._connect()
        self.__cursor.execute(f"SELECT user_ban FROM users WHERE user_id = {user_id};")
        self._commit()
        status = self.__cursor.fetchone()[0]
        self._close()
        if bool(status):
            return True
        else:
            return False
        
    def insert_user(self, user_name, user_id):
        self._connect()
        current_date = date.today().strftime("%d-%m-%Y")
        self.__cursor.execute(f"INSERT INTO users (user_name, user_id, user_regdate) VALUES ('{user_name}', '{user_id}', '{current_date}');")
        self._commit()
        self._close()

    def check_queue(self):
        self._connect()
        self.__cursor.execute(f"SELECT * FROM queue;")
        self._commit()
        queue = self.__cursor.fetchall()
        self._close()
        if len(queue) > 0:
            return True
        else:
            return False
        
    def add_queue(self, user_id):
        self._connect()
        self.__cursor.execute(f"INSERT INTO queue (user_id) VALUES ('{user_id}');")
        self._commit()
        self._close()

    def remove_queue(self, user_id):
        self._connect()
        self.__cursor.execute(f"DELETE FROM queue WHERE user_id = {user_id};")
        self._commit()
        self._close()

    def add_session(self, user_id1, user_id2):
        self._connect()
        self.__cursor.execute(f"INSERT INTO sessions (session_user_id_1, session_user_id_2) VALUES ('{user_id1}', '{user_id2}');")
        self._commit()
        self._close()

    def remove_session(self, user_id):
        self._connect()
        self.__cursor.execute(f"DELETE FROM sessions WHERE session_user_id_1 = {user_id} OR session_user_id_2 = {user_id};")
        self._commit()
        self._close()

    def random_user_from_queue(self):
        self._connect()
        self.__cursor.execute(f"SELECT user_id FROM queue LIMIT 1;")
        user_id = self.__cursor.fetchone()[0]
        self._commit()
        self._close()
        return user_id
    
    def check_queue_duplicated(self, user_id):
        self._connect()
        self.__cursor.execute(f"SELECT * FROM queue WHERE user_id = {user_id};")
        self._commit()
        queue_duplicated = self.__cursor.fetchall()
        self._close()
        if queue_duplicated:
            return True
        else:
            return False
        
    def check_session(self, user_id):
        self._connect()
        self.__cursor.execute(f"SELECT * FROM sessions WHERE session_user_id_1 = {user_id} OR session_user_id_2 = {user_id};")
        self._commit()
        session = self.__cursor.fetchall()
        self._close()
        if session:
            return True
        else:
            return False
    
    def get_user_from_session(self, user_id):
        self._connect()
        self.__cursor.execute((f"SELECT (session_user_id_1, session_user_id_2) FROM sessions WHERE session_user_id_1 = {user_id} OR session_user_id_2 = {user_id};"))
        self._commit()
        users = list(eval(self.__cursor.fetchall()[0][0]))
        self._close()
        users.remove(user_id)
        interlocutor = users[0]
        return interlocutor
    
    def get_user_chats(self, user_id):
        self._connect()
        self.__cursor.execute(f"SELECT user_chats FROM users WHERE user_id = {user_id};")
        self._commit()
        count = self.__cursor.fetchone()[0]
        self._close()
        return count
    
    def update_user_chats(self, user_id):
        self._connect()
        self.__cursor.execute(f"UPDATE users SET user_chats = user_chats + 1 WHERE user_id = {user_id};")
        self._commit()
        self._close()

    def get_user_regdate(self, user_id):
        self._connect()
        self.__cursor.execute(f"SELECT user_regdate FROM users WHERE user_id = {user_id};")
        self._commit()
        regdate = self.__cursor.fetchone()[0]
        self._close()
        return regdate
    
    def add_complaint(self, sender_id, target_id, reason):
        self._connect()
        self.__cursor.execute(f"INSERT INTO сomplaints (сomplaint_sender, сomplaint_target, complaint_reason) VALUES ('{sender_id}', '{target_id}', '{reason}');")
        self._commit()
        self._close()
    
    def get_target_messages(self, target_id):
        self._connect()
        self.__cursor.execute(f"SELECT session_user_messages_1 FROM sessions WHERE session_user_id_1 = {target_id};")
        messages_1 = self.__cursor.fetchone()
        self._commit()
        self.__cursor.execute(f"SELECT session_user_messages_2 FROM sessions WHERE session_user_id_2 = {target_id};")
        messages_2 = self.__cursor.fetchone()
        self._commit()
        self._close()
        if messages_1 != None:
            return messages_1[0]
        else:
            return messages_2[0]
        
    def add_user_message(self, user_id, message):
        messages = list(self.get_user_messages(user_id))
        self._connect()
        messages.append(f'"{message}"')
        messages = ",".join(messages)
        self.__cursor.execute(f"UPDATE sessions SET session_user_messages_1 = '%s' WHERE session_user_id_1 = {user_id};" % ("{" + messages + "}"))
        self._commit()
        self.__cursor.execute(f"UPDATE sessions SET session_user_messages_2 = '%s' WHERE session_user_id_2 = {user_id};" % ("{" + messages + "}"))
        self._commit()
        self._close()

    def get_user_messages(self, user_id):
        self._connect()
        self.__cursor.execute(f"SELECT session_user_messages_1 FROM sessions WHERE session_user_id_1 = {user_id};")
        messages_1 = self.__cursor.fetchone()
        self._commit()
        self.__cursor.execute(f"SELECT session_user_messages_2 FROM sessions WHERE session_user_id_2 = {user_id};")
        messages_2 = self.__cursor.fetchone()
        self._commit()
        self._close()
        if messages_1 != None:
            return messages_1[0]
        else:
            return messages_2[0]
        
    def get_user_images(self, user_id):
        self._connect()
        self.__cursor.execute(f"SELECT session_user_images_1 FROM sessions WHERE session_user_id_1 = {user_id};")
        images_1 = self.__cursor.fetchone()
        self._commit()
        self.__cursor.execute(f"SELECT session_user_images_2 FROM sessions WHERE session_user_id_2 = {user_id};")
        images_2 = self.__cursor.fetchone()
        self._commit()
        self._close()
        if images_1 != None:
            return images_1[0]
        else:
            return images_2[0]
    
    def add_user_image(self, user_id, photo_id):
        images = list(self.get_user_images(user_id))
        self._connect()
        images.append(f'"{photo_id}"')
        images = ",".join(images)
        self.__cursor.execute(f"UPDATE sessions SET session_user_images_1 = '%s' WHERE session_user_id_1 = {user_id};" % ("{" + images + "}"))
        self._commit()
        self.__cursor.execute(f"UPDATE sessions SET session_user_images_2 = '%s' WHERE session_user_id_2 = {user_id};" % ("{" + images + "}"))
        self._commit()
        self._close()

    def check_admin_status(self, user_id):
        self._connect()
        self.__cursor.execute(f"SELECT * FROM admins WHERE admin_id = {user_id};")
        self._commit()
        result = self.__cursor.fetchall()
        self._commit()
        self._close()
        if result:
            return True
        else:
            return False
        
    def update_complaint(self, target_id, status):
        self._connect()
        self.__cursor.execute(f"UPDATE сomplaints SET complaint_status = '{status}' WHERE сomplaint_target = {target_id} AND complaint_status = 'waiting';")
        self._commit()
        self._close()

    def ban_user(self, target_id, admin_id):
        self._connect()
        self.__cursor.execute(f"UPDATE users SET user_ban = True WHERE user_id = {target_id};")
        self._commit()
        self.__cursor.execute(f"UPDATE admins SET admin_bans = admin_bans + 1 WHERE admin_id = {admin_id};")
        self._commit()
        self._close()

db = Database()
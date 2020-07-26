import pymysql
import random
from scripts.handle_conf import hy


class HandleMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host=hy.read_yaml('mysql', 'host'),
            user=hy.read_yaml('mysql', 'user'),
            password=hy.read_yaml('mysql', 'password'),
            port=hy.read_yaml('mysql', 'port'),
            charset=hy.read_yaml('mysql', 'charset'),
            db=hy.read_yaml('mysql', 'db'),
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    @staticmethod
    def get_phone():
        return '138' + str(''.join(random.sample('0123456789', 8)))

    def get_mysql_result(self, sql, args=None, is_more=True):
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            result = self.cursor.fetchall()
        else:
            result = self.cursor.fetchone()

        return result

    def phone_exist_mysql(self, phone):
        sql = hy.read_yaml('mysql', 'phone_sql')
        result = self.get_mysql_result(sql=sql, args=phone)
        if result:
            return True
        else:
            return False

    def get_right_phone(self):
        while True:
            phone = self.get_phone()
            bl = self.phone_exist_mysql(phone)
            if not bl:
                break
            else:
                continue
        return phone

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    hm = HandleMysql()
    # print(hm.get_phone())
    print(hm.get_right_phone())
    hm.close()
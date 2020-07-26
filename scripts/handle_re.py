import re
from scripts.handle_mysql import HandleMysql

class HandleRe:

    @classmethod
    def get_re(cls, data):
        hm = HandleMysql()
        phone = hm.get_right_phone()
        if re.search(r'{no_exist_phone}', data):
            result = re.sub(r'{no_exist_phone}', phone, data)
            return result
        return data

from scripts.handle_request import HandleRequest
from scripts.handle_mysql import HandleMysql
from scripts.handle_conf import hy, HandleYaml
from scripts.handle_path import phone_yaml


class HandlePhone:
    @classmethod
    def get_phone(cls, user, password="12345678", type_num=1):
        hr = HandleRequest()
        hm = HandleMysql()
        hr.common_head({'X-Lemonban-Media-Type': 'lemonban.v2'})
        base_url = hy.read_yaml('api', 'load')
        register_url = hy.read_yaml('api', 'register')
        all_url = ''.join((base_url, register_url))
        while True:
            # 获取在数据库中不存在的电话号码
            phone = hm.get_right_phone()
            data = {"mobile_phone": phone, "pwd": password, "type": type_num, "reg_name": user}
            result = hr.send(url=all_url, data=data)
            if result.json()['code'] == 0 and result.json()["msg"] == "OK":
                break

        my_result = hm.get_mysql_result(hy.read_yaml('mysql', 'user_id'), args=phone)
        user_id = my_result[0]['id']

        result_data = {
            user: {
                "user_phone": phone,
                "pwd": password,
                "user_id": user_id,
                "reg_name": user
            }
        }
        hm.close()
        hr.close()
        return result_data


class LoopPhone:
    @classmethod
    def generate_phone(cls):
        hy_yaml = HandleYaml(filepath=phone_yaml)
        gen_phone = {}
        # admin
        admin_result = HandlePhone.get_phone(user='admin', type_num=0)
        gen_phone.update(admin_result)
        # investor
        invest_result = HandlePhone.get_phone(user='investor', type_num=1)
        gen_phone.update(invest_result)
        # loan
        loan_result = HandlePhone.get_phone(user='loan', type_num=1)
        gen_phone.update(loan_result)

        hy_yaml.write_yaml(data=gen_phone)


if __name__ == '__main__':
    LoopPhone.generate_phone()

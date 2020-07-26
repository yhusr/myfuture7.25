import unittest
from lib.ddt import ddt, data
from scripts.handle_excel import HandleExcel
from scripts.handle_mysql import HandleMysql
from scripts.handle_request import HandleRequest
from scripts.handle_conf import hy
from scripts.handle_re import HandleRe
from scripts.handle_log import logger


@ddt
class HandleRegister(unittest.TestCase):
    he = HandleExcel(sheetname='register')
    cases = he.read_excel()

    @classmethod
    def setUpClass(cls) -> None:
        cls.hm = HandleMysql()
        cls.hr = HandleRequest()
        cls.hr.common_head({'X-Lemonban-Media-Type': 'lemonban.v2'})

    @data(*cases)
    def test_register_case(self, case):
        title = case.title
        base_url = hy.read_yaml('api', 'load')
        all_url = ''.join((base_url, case.url))
        re_data = HandleRe.get_re(case.data)
        result = self.hr.send(url=all_url, data=re_data)
        code = result.json()['code']
        msg = result.json()['msg']
        try:
            self.assertListEqual([case.expected, case.msg], [code, msg], msg=f"用例{title}测试完成")
        except Exception as e:
            self.he.write_excel(int(case.caseId) + 1, 7, value="fail")
            self.he.write_excel(int(case.caseId) + 1, 8, value=result.text)
            logger.error(e)
            raise e
        else:
            self.he.write_excel(int(case.caseId) + 1, 7, value="success")
            self.he.write_excel(int(case.caseId) + 1, 8, value=result.text)
            logger.info(title)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.hm.close()
        cls.hr.close()

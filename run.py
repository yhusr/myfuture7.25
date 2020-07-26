import unittest
from scripts.handle_path import case_path, reports_path
from lib.HTMLTestRunnerNew import HTMLTestRunner
import time


class RunCase:
    @classmethod
    def run_my_cases(cls):
        suit = unittest.defaultTestLoader.discover(case_path)

        case_run = HTMLTestRunner(stream=open(reports_path, mode='wb'),
                                  title='我的初始报告',
                                  tester='y.h',
                                  description='接口测试')
        case_run.run(suit)


if __name__ == '__main__':
    RunCase.run_my_cases()

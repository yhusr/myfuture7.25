import os
import time

py_path = os.path.abspath(__file__)
file_path = os.path.dirname(py_path)
root_path = os.path.dirname(file_path)

# excel的路径
data_path = os.path.join(root_path, 'data')
excel_path = os.path.join(data_path, 'excelcases.xlsx')
# print(excel_path)

# yaml的路径
config_path = os.path.join(root_path, 'config')
yaml_path = os.path.join(config_path, 'conf.yaml')

# config的路径
conf_path = os.path.join(config_path, 'conf.ini')

# log的路径
logs_path = os.path.join(root_path, 'logs')

# 用例路径
case_path = os.path.join(root_path, 'cases')

# 报告路径
reporter_path = os.path.join(root_path, 'reports')
str_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
reports_path = os.path.join(reporter_path, str_time + '的报告.html')

# 手机号生成yaml文件路径
phone_yaml = os.path.join(config_path, 'phone_generate.yaml')


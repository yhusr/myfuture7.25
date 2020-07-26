import logging
import time
import os
from scripts.handle_path import logs_path


class HandleLog:

    @classmethod
    def get_logger(cls):
        logger = logging.getLogger('oper')
        logger.setLevel('DEBUG')
        format_log = logging.Formatter('%(asctime)s - %(name)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')

        # 控制台输出
        st_handler = logging.StreamHandler()
        st_handler.setLevel("DEBUG")
        st_handler.setFormatter(format_log)
        logger.addHandler(st_handler)

        # 文件输出
        str_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        file_path = os.path.join(logs_path, str_time+'.log')
        fh_handler = logging.FileHandler(filename=file_path, encoding='utf8')
        fh_handler.setLevel('DEBUG')
        fh_handler.setFormatter(format_log)
        logger.addHandler(fh_handler)

        return logger


logger = HandleLog.get_logger()


if __name__ == '__main__':
    logger = HandleLog.get_logger()
    logger.setLevel("DEBUG")
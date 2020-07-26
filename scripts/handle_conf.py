import configparser
import yaml
from scripts.handle_path import yaml_path, conf_path


class HandleYaml:
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = yaml_path

    def read_yaml(self, section_name, option_name):
        with open(self.filepath, 'r', encoding='utf8') as m:
            files = yaml.full_load(m)
        yaml_result = files[section_name][option_name]
        return yaml_result

    def write_yaml(self, data):
        with open(self.filepath, 'a', encoding='utf8') as o:
            yaml.dump(data, o, allow_unicode=True)


hy = HandleYaml()


class HandleConfig:
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = conf_path
        self.conf = configparser.ConfigParser()

    def read_config(self, section_name, option_name):
        self.conf.read(self.filepath, encoding='utf8')
        sc = self.conf.get(section_name, option_name)
        try:
            my_sc = eval(sc)
        except NameError as n:
            return sc
        else:
            return my_sc

    def write_config(self, datas):
        for data in datas:
            self.conf[data] = datas[data]
        with open(self.filepath, 'a', encoding='utf8') as f:
            self.conf.read(f)


if __name__ == '__main__':
    # hy = HandleYaml(yaml_path)
    # excel_result = hy.read_yaml('excel', 'excel_name')
    # data = {"mysql": {"host":'192.168.1.1'}}
    # hy.write_yaml(data)
    # print(excel_result)
    hc = HandleConfig()
    result = hc.read_config('excel', 'excel_name')
    print(result)
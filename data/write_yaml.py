import yaml
from data.read_yaml import read_data


with open("../data/write_data.yaml" , "w" , encoding= "utf-8")as f:
    data = {"name":"张三"}
    yaml.dump(data,f, allow_unicode =True)
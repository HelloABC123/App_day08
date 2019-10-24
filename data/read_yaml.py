import yaml
def read_data():
    with open("./data.yaml" , "r",encoding= "utf-8") as f:
        return yaml.load(f)

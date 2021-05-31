import argparse
import yaml
import os
from src.get_data import get_data,read_params



def load_and_save(config_path):   
    config = read_params(config_path)
    df = get_data(config_path)
    df.columns = [cols.replace(' ','_') for cols in df.columns]
    write_path = config['load_data']['raw_data_set']
    df.to_csv(write_path,sep=',',index=False,header=True)



if __name__== "__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("config",'params.yaml')
    load_and_save(default_config_path)
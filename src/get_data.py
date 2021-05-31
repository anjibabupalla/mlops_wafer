import os
import argparse
import yaml
import logging
import pandas as pd
import glob

def read_all_csv(path):
    all_files = glob.glob(path + "/*.csv")
    list_of_dfs = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0,sep=',')
        list_of_dfs.append(df)
    return pd.concat(list_of_dfs, axis=0, ignore_index=True)

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    print('displaying config values',config)
    data_path = config['data_source']['batch_files']
    df = pd.read_csv(data_path)
    print(df.columns)
    return df



if __name__=="__main__":
    args =  argparse.ArgumentParser()
    default_config_path = os.path.join("config",'params.yaml')
    
    args.add_argument("--config",default=default_config_path)
    # args.add_argument("--datasource",default=None)
    parsed_args = args.parse_args()    
    data = get_data(config_path=parsed_args.config)
import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from src.get_data import read_params


def split_and_save_data(config_path):
    config = read_params(config_path)
    test_data_path = config['split_data']['test_path']
    train_data_path = config['split_data']['train_path']
    raw_data_path = config['load_data']['raw_data_set']
    split_ratio = config['split_data']['test_size']
    random_state = config['base']['random_state']
    df = pd.read_csv(raw_data_path, sep=',')
    train, test = train_test_split(
        df, test_size=split_ratio, random_state=random_state)
    train.to_csv(train_data_path, sep=',', index=False,
                 encoding='utf-8', header=True)
    test.to_csv(test_data_path, sep=',', index=False,
                encoding='utf-8', header=True)


if __name__ == '__main__':
    # args =  argparse.ArgumentParser()
    default_config_path = os.path.join("config", 'params.yaml')

    # args.add_argument("--config",default=default_config_path)
    # # args.add_argument("--datasource",default=None)
    # parsed_args = args.parse_args()
    data = split_and_save_data(config_path=default_config_path)

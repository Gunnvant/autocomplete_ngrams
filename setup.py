import csv
from app import create_database, populate_db_table
from tqdm import tqdm
create_database()
db_name = "main.db"
csv_paths = ["./data/unigrams.csv",
             "./data/bigrams.csv",
             "./data/trigrams.csv"]
table_names = ['unigrams',
               'bigrams',
               'trigrams']
for path_csv, table_name in tqdm(zip(csv_paths, table_names)):
    populate_db_table(path_csv, db_name, table_name)
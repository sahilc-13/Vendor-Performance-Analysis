import pandas as pd
import os
import time
from sqlalchemy import create_engine
import logging

logging.basicConfig(filename="logs/ingestion_db.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filemode="a")

engine = create_engine('sqlite:///inventory.db', connect_args={"timeout": 60})

from sqlalchemy import text

def prepare_sqlite_for_bulk(engine):
    with engine.connect() as conn:
        conn.exec_driver_sql("PRAGMA journal_mode=WAL;")
        conn.exec_driver_sql("PRAGMA synchronous=OFF;")
        conn.exec_driver_sql("PRAGMA temp_store=MEMORY;")
        conn.exec_driver_sql("PRAGMA cache_size=-100000;") 

def ingest_csv_in_chunks(csv_path, table_name, engine, chunksize=50000):
    first = True
    for chunk in pd.read_csv(csv_path, chunksize=chunksize, low_memory=False):
        # memory optimizations - example: downcast numeric types
        for col in chunk.select_dtypes(include=['int64']).columns:
            chunk[col] = pd.to_numeric(chunk[col], downcast='integer')
        for col in chunk.select_dtypes(include=['float64']).columns:
            chunk[col] = pd.to_numeric(chunk[col], downcast='float')

        chunk.to_sql(table_name, con=engine, if_exists='replace' if first else 'append', index=False)
        first = False

def load_raw_data():
    start = time.time()
    prepare_sqlite_for_bulk(engine)
    for file in os.listdir('Data'):
        if file.endswith('.csv'):
            logging.info(f"Starting {file}")
            ingest_csv_in_chunks(os.path.join('Data', file), file[:-4], engine, chunksize=50000)
            logging.info(f"Finished {file}")
    end = time.time()
    logging.info(f"Total time (minutes): {(end-start)/60:.2f}")

if __name__ == '__main__':
    load_raw_data()

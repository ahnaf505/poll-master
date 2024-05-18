import plyvel
import logging

logging.basicConfig(filename='app_db.dbglog', filemode='a+', format='%(asctime)s - %(levelname)s: %(message)s')

def write_db(key, value):
    db = plyvel.DB('polls.db', create_if_missing=True)
    with db.write_batch() as wb:
        wb.put(key.encode(), value.encode())
    db.close()
    logging.info("Successfully read from database with key ("+key+") and value ("+value+")")

def read_db(key):
    db = plyvel.DB('polls.db', create_if_missing=True)
    value = db.get(key.encode())
    db.close()
    if value:
        logging.info("Successfully read from database with key ("+key+")")
        return value.decode()
    else:
        logging.error("Error reading database, no record for ("+key+")")
        return None

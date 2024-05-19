import plyvel
import logging

logging.basicConfig(filename='app_db.dbglog', level=logging.INFO, filemode='a+', format='%(asctime)s - %(levelname)s: %(message)s')

def write_db(key, value):
    db = plyvel.DB('polls.db', create_if_missing=True)
    with db.write_batch() as wb:
        wb.put(key.encode(), value.encode())
        logging.info("Successfully write to database with key ("+key+") and value ("+value+")")
    db.close()
    return

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

def delete_db(key):
    db = plyvel.DB('polls.db', create_if_missing=True)
    if db.get(key.encode()) is not None:
        db.delete(key.encode())
        logging.info("Successfully deleted from database with key (" + key+")")
    else:
        logging.error("Error deleting from database, no record for (" + key+")")
        return None
    db.close()

write_db("aaaaa", "asjnjsnsnnd")
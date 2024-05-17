import plyvel

def write_to_database(key, value):
    db = plyvel.DB('polls_question.db', create_if_missing=True)
    # Write data to the database
    with db.write_batch() as wb:
        wb.put(key.encode(), value.encode())

    # Close the database
    db.close()

def read_from_database(key):
    # Open the LevelDB database
    db = plyvel.DB('/path/to/database', create_if_missing=True)

    # Read data from the database
    value = db.get(key.encode())

    # Close the database
    db.close()

    # Convert value to string if it exists
    return value.decode() if value else None

# Example usage
write_to_database("key1", "value1")
write_to_database("key2", "value2")

value1 = read_from_database("key1")
print("Value for key1:", value1)

value2 = read_from_database("key2")
print("Value for key2:", value2)

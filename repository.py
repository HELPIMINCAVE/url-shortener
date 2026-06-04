database_table = {}

def save_record(record):
    shortcode = record["shortCode"]
    database_table[shortcode] = record
    return record

def get_record(shortcode):
    if shortcode not in database_table:
        return None
    return database_table.get(shortcode)

def increment_access_count(shortcode):
    database_table[shortcode]["accessCount"] += 1
    return database_table[shortcode]


def update_record(shortcode, new_url, update_timestamp):
    database_table[shortcode]["url"] = new_url
    database_table[shortcode]["updatedAt"] = update_timestamp
    
    return database_table[shortcode]

def delete_record(shortcode):
    del database_table[shortcode]
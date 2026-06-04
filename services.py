import random, repository, uuid
from datetime import datetime, timezone

allowed_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def generate_shortcode():
    while True:
        shortcode = "".join(random.choices(allowed_letters, k=6))
        
        if repository.get_record(shortcode) is None:
            return shortcode


def get_shortened_url(shortcode):
    record = repository.get_record(shortcode)
    if record is None:
        return None
    
    updated_record = repository.increment_access_count(shortcode)
    return updated_record

def update_url(shortcode, new_url: str):
    if not new_url.startswith("http://") or new_url.startswith("https://"):
        raise ValueError("Invalid URL.")
    
    record = repository.get_record(shortcode)
    if record is None:
        return None
    
    current_time = datetime.now(timezone.utc).isoformat()
    updated_record = repository.update_record(shortcode, new_url, current_time)
    
    return updated_record


def delete_url(shortcode):
    if repository.get_record(shortcode) is None:
        return False
    
    repository.delete_record(shortcode)
    return True

def shorten_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        raise ValueError("Invalid URL.")
    
    shortcode = generate_shortcode()
    id = uuid.uuid4().hex
    current_time = datetime.now(timezone.utc).isoformat()
    
    record = {
    "id": id,
    "url": url,
    "shortCode": shortcode,
    "createdAt": current_time,
    "updatedAt": current_time,
    "accessCount": 0
    }
    
    repository.save_record(record)
    return record
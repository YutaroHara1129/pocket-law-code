def select_records(records, limit=None):
    if limit is not None and limit < 0:
        raise ValueError("limit must not be negative")
    return list(records[:limit])

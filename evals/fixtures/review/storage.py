def expire(rows, owner, now):
    return [row for row in rows if row["expires"] > now]

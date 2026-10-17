# Expiration

`expire(rows, owner, now)` returns the remaining rows in input order. It removes
only rows belonging to the requested owner whose `expires` value is less than
or equal to `now`. Rows belonging to other owners must remain untouched.

# Record selection

`select_records(records, limit=None)` returns a new list containing the selected
records, in input order. Both `None` and `0` mean all records. Positive limits
return at most that many records. Negative limits raise `ValueError`.

`render_export(records, limit=0)` uses that contract to export all records by
default, one record per line. It does not change the input list.

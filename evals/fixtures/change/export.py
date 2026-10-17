from records import select_records


def render_export(records, limit=0):
    return "\n".join(select_records(records, limit))

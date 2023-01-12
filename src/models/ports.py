class Port:
    def __init__(self, code, name, parent_slug):
        self.code = code
        self.name = name
        self.parent_slug = parent_slug

    @classmethod
    def find_by_code(cls, code, conn):
        cur = conn.cursor()
        cur.execute("SELECT code, name, parent_slug FROM ports WHERE code = %s", (code,))
        data = cur.fetchone()
        return cls(data[0], data[1], data[2]) if data else None

    @classmethod
    def find_by_parent_slug(cls, parent_slug, conn):
        cur = conn.cursor()
        cur.execute("SELECT code, name, parent_slug FROM ports WHERE parent_slug = %s", (parent_slug,))
        data = cur.fetchall()
        return [cls(row[0], row[1], row[2]) for row in data] if data else None

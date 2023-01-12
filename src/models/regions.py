class Region:
    def __init__(self, slug, name, parent_slug):
        self.slug = slug
        self.name = name
        self.parent_slug = parent_slug

    @classmethod
    def find_by_slug(cls, slug, conn):
        cur = conn.cursor()
        cur.execute("SELECT slug, name, parent_slug FROM regions WHERE slug = %s", (slug,))
        data = cur.fetchone()
        return cls(data[0], data[1], data[2]) if data else None

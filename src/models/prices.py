class Price:
    def __init__(self, orig_code, dest_code, day, price):
        self.orig_code = orig_code
        self.dest_code = dest_code
        self.day = day
        self.price = price

    @classmethod
    def find_average_prices(cls, date_from, date_to, origin, destination, conn):
        cur = conn.cursor()
        cur.execute("""
            SELECT day, AVG(price) as average_price FROM prices
            WHERE orig_code = ANY(%s) AND dest_code = ANY(%s) AND day >= %s AND day <= %s
            GROUP BY day
            HAVING COUNT(*) >= 3""", (origin, destination, date_from, date_to))
        prices = cur.fetchall()
        return prices


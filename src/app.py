from flask import Flask, jsonify, request
import psycopg2
from src.models import Port, Region, Price
from src.utils import validate_input

app = Flask(__name__)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="ratestask",
    database="postgres"
)


# Helper function to get port codes if the origin or destination is a region slug
def get_port_codes(region_slug):
    cur = conn.cursor()
    cur.execute("SELECT code FROM ports JOIN regions ON ports.parent_slug = regions.slug WHERE regions.slug = %s",
                (region_slug,))
    port_codes = [x[0] for x in cur.fetchall()]
    return port_codes


@app.route('/rates', methods=['GET'])
def get_average_prices():
    # Get the query parameters
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    origin = request.args.get('origin')
    destination = request.args.get('destination')

    # input validation
    try:
        validate_input(date_from, date_to, origin, destination)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    # create a list of origin port codes
    origin_port_codes = []
    for value in origin:
        # check if the value is a region slug
        data = Port.find_by_parent_slug(value, conn)
        if data:
            origin_port_codes.extend([row.code for row in data])
        else:
            origin_port_codes.append(value)

    # create a list of destination port codes
    destination_port_codes = []
    for value in destination:
        # check if the value is a region slug
        data = Port.find_by_parent_slug(value, conn)
        if data:
            destination_port_codes.extend([row.code for row in data])
        else:
            # if it's not a region slug, then it's a port code
            destination_port_codes.append(value)

    # get average prices
    prices = Price.find_average_prices(date_from, date_to, origin_port_codes, destination_port_codes, conn)

    # create a list of json objects to return
    result = []
    for price in prices:
        result.append({'day': price[0], 'average_price': price[1]})

    return jsonify(result)


# close the database connection when the server is down
@app.teardown_appcontext
def close_connection(exception):
    conn.close()


if __name__ == '__main__':
    app.run(debug=True)

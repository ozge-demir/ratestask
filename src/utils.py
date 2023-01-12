import re


def validate_input(date_from, date_to, origin, destination):
    # check if date_from, date_to, origin and destination are not None
    if not (date_from and date_to and origin and destination):
        raise ValueError('date_from, date_to, origin and destination are required')
    validate_date_range(date_from, date_to)


def validate_date_range(date_from, date_to):
    validate_date(date_from)
    validate_date(date_to)
    # check if date_from is not greater than date_to
    if date_from > date_to:
        raise ValueError('date_from cannot be greater than date_to')


def validate_date(date_string):
    # check if date is in YYYY-MM-DD format
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_string):
        raise ValueError('Invalid date format. Use YYYY-MM-DD')


def validate_port_code_or_region_slug(value):
    # check if value is a valid port code or region slug
    if not re.match(r'^[a-zA-Z0-9_]+$', value):
        raise ValueError('Invalid port code or region slug')

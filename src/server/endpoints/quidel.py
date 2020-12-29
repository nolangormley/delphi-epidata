from flask import jsonify, request, Blueprint

from sqlalchemy import select
from .._common import app, db
from .._config import AUTH
from .._validate import require_all, extract_strings, extract_integers
from .._query import filter_strings, execute_query, filter_integers
from .._exceptions import UnAuthenticatedException

# first argument is the endpoint name
bp = Blueprint("quidel", __name__)
alias = None


@bp.route("/", methods=("GET", "POST"))
def handle():
    require_all("auth", "locations", "epiweeks")
    if request.values["auth"] != AUTH["quidel"]:
        raise UnAuthenticatedException()

    locations = extract_strings("locations")
    epiweeks = extract_integers("epiweeks")

    # build query
    table = "`quidel` q"
    fields = "q.`location`, q.`epiweek`, q.`value`"
    order = "q.`epiweek` ASC, q.`location` ASC"

    # build the filter
    params = dict()
    # build the location filter
    condition_location = filter_strings("q.`location`", locations, "loc", params)
    condition_epiweek = filter_integers("q.`epiweek`", epiweeks, "epiweek", params)
    # the query
    query = f"SELECT {fields} FROM {table} WHERE ({condition_location}) AND ({condition_epiweek}) ORDER BY {order}"

    fields_string = [
        "location",
    ]
    fields_int = ["epiweek"]
    fields_float = ["value"]

    # send query
    return execute_query(query, params, fields_string, fields_int, fields_float)

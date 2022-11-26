import os
from dotenv import load_dotenv

load_dotenv()

# TODO: add validation
_con_str = os.getenv("DBSOUP_CONNECTION_STRING").partition("+")

DBSOUP_DIALECT = _con_str[0]
DBSOUP_CONNECTION_STRING = _con_str[2]

from requests.utils import requote_uri
from sqlalchemy import create_engine
from conn_data import conn_data

def connect():
    data = conn_data
    url = 'oracle://%s:%s@%s:%s/%s' % (data['schema'], requote_uri(data['password']), data['hostname'], data['port'], data['sid'])

    return create_engine(url, connect_args = {
        "encoding": "UTF-8",
        "nencoding": "UTF-8"
    }, convert_unicode = True)
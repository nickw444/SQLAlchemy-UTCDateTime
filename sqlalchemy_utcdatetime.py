from sqlalchemy import types
from datetime import datetime
import pytz

class UTCDateTime(types.TypeDecorator):

    impl = types.DateTime
    def process_bind_param(self, value, engine):
        if value is not None:
            return value.astimezone(pytz.UTC)
    def process_result_value(self, value, engine):
        if value is not None:
            return value.replace(tzinfo=pytz.UTC)

def now():
    return datetime.now(pytz.UTC)


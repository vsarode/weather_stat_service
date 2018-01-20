from rq import Connection, Worker
from datetime import datetime
import time
from pytz import timezone

with Connection():
    qs = ['lead_sms']
    tmzn = timezone('Asia/Kolkata')
    # TODO check why the exception handling is not working
    w = Worker(qs)
    present_time = datetime.now(tz=tmzn)
    business_hours_start = present_time.replace(hour=9, minute=0, second=0)
    business_hours_end = present_time.replace(hour=21, minute=0,
                                              second=0)
    while True:
        present_time = datetime.now(tz=tmzn)
        in_business_hours = business_hours_end > present_time \
                            and business_hours_start < present_time
        if in_business_hours:
            w.work()
        else:
            time.sleep(600)

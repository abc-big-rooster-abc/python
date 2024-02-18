import hashlib
import uuid
import random
import datetime
from django.conf import settings


def md5(data_string):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()


def gen_random_id(string):
    data = "{}-{}".format(str(uuid.uuid4()), string)
    return md5(data)


def gen_random_oid():
    rand_number = random.randint(10000000, 99999999)
    ctime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    trans_id = "{}{}".format(ctime, rand_number)
    return trans_id

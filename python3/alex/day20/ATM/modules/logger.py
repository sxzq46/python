# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/26


import logging
from conf import settings


def logger(log_type):

    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    log_file = "%s\\logs\\%s" %(settings.BASE_DIR,settings.LOG_TYPE[log_type])
    fh = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return  logger
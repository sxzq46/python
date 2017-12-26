# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/12


import logging

logger = logging.getLogger()

fh = logging.FileHandler('test.log')

sh = logging.StreamHandler()

formatter =  logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')
logger.setLevel(logging.DEBUG)

fh.setFormatter(formatter)

sh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(sh)

logging.debug('debug message1')
logging.info('info message2')
logging.warning('warn message3')
logging.error('error message4')
logging.critical('Boom message5')
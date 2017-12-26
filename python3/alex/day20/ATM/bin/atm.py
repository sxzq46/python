# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/26


import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from modules import main

main.main()
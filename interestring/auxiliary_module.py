#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:59:49 2019

@author: lemo
"""

import logging



class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('spam_applicationo.auxiliary.Auxiliary')
        self.logger.info('creating an instance of Auxiliary')
        
    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')
    

module_logger = logging.getLogger('spam_application.auxiliary')
def some_function():
    module_logger.info('recevied a call to "some_functions"')
        
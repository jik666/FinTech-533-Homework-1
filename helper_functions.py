# Contains helper functions for your apps!
import os
from os import listdir, remove

cwd = os.getcwd()
list_dir = os.listdir(cwd)
def check_for_and_del_io_files() :
    for file in list_dir:
        # If the io following files are in the current directory, remove them!
        # 1. 'currency_pair.txt'
        if file == 'currency_pair.txt' :
            remove('currency_pair.txt')
        # 2. 'currency_pair_history.csv
        if file == 'currency_pair_history.csv' :
            remove('currency_pair_history.csv')
        # 3. 'trade_order.p'
        if file == 'trade_order.p' :
            remove('trade_order.p')
    # nothing gets returned by this function, so end it with 'pass'.
    pass
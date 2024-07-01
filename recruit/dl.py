"""Module providing a function printing python version."""
import os
import sys
from contextlib import redirect_stdout
import gspread
def dl():"""gspread dl function"""
mypath = os.path.dirname(os.path.abspath(__file__))
gc = gspread.service_account()
sh = gc.open("Steamwheedle Recruitment")
worksheet = sh.worksheet("Recruitment")
guilds_list = [item for item in worksheet.col_values(1) if item]
original_stdout = sys.stdout
with open(mypath+'/guild.txt', 'w') as f:
    with redirect_stdout(f):
        for item in guilds_list:
            print(item)

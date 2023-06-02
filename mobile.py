import re
import pandas as pd

def mobile2(data):

    pattern2 = re.compile(r'@\d{12}')
    message23 = []
    message23 = re.findall(pattern2, data)
    return message23
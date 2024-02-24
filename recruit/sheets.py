import sys
import csv
import urllib.request
from io import StringIO

url = 'https://docs.google.com/spreadsheets/d/1PJ8ScTjVl0UQgWJE5S4v_pSGdlh2q6ciWYpZZX9XSUY/export?format=csv&gid=1471460927'
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
cr = csv.reader(lines)

original_stdout = sys.stdout
with open('guild.txt', 'w+') as f:
    sys.stdout = f
    for row in cr:
        print(','.join(row))
sys.stdout = original_stdout
with open("guild.txt") as f:
    content = f.read()
print(content)


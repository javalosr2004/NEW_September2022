import os.path, time
from os import walk
import os
import sys


if len(sys.argv) > 1:
    time_sleep = int(sys.argv[1])
else:
    time_sleep = 5
print(f'Running ... checks set to {time_sleep} second intervals')

#files to be checked
files = []
file_path = 'javascript'

for (dirpath, dirnames, filenames) in walk(file_path):
    for file in filenames:
        files.append(dirpath + '/' + file)
    break

changes = {}


index = 0

for f in files:
    changes[f] = os.path.getmtime(f)
    index += 1


while True:
    for f in files:
        if changes.get(f) < os.path.getmtime(f):
            html = ''
            with open('example_website.html', 'w+') as og_f:
                with open('example_html.txt', 'r') as ex_f:
                    html = ex_f.read()
                    html += f"\n<script src = './{f}'></script>\n</html>"
                og_f.write(html)
            changes[f] = os.path.getmtime(f)
    time.sleep(time_sleep)

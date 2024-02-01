import re

with open('/home/drashti/Documents/Python/TASK 3(re for build gradle)/build.gradle', 'r+') as file:
    file_content = file.read()
    file_content = re.sub(r'release\s*{\s*debuggable false', 'release {\n    debuggable true', file_content)
    file.write(file_content)

print("Changed.")


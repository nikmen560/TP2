import json
import os.path
from Customer import Customer

# Работа с файлом data.json
class File:
    def read(path, name):
        parseJson = None

        if os.path.isfile(path):
            with open(name, 'r') as f:
                parseJson = json.loads(f.read())

        return parseJson

    def write(path, name, parseJson) -> None:
        if os.path.isfile(path):
            with open(name, 'w+') as f:
                f.seek(0)
                f.close()
        
        with open(name, 'w+') as f:
            f.write(json.dumps(parseJson, ensure_ascii = False, indent = 4))

 
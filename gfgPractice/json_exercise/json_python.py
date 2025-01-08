import json
from collections import namedtuple

data = '{"name" : "sdf", "id" : 1, "location" : "adfsdf"}'
 
x = json.loads(data, object_hook =
               lambda d : namedtuple('X', d.keys())
               (*d.values()))
 
print(x.name, x.id, x.location)
from flatten_json import flatten
 
unflat_json = {'user':
               {'Rachel':
                {'UserID': 1717171717,
                 'Email': 'adasd@gmail.com',
                 'friends': ['ads', 'gjhk', 'asdasf']
                 }
                }
               }
 
flat_json = flatten(unflat_json)
 
print(flat_json)
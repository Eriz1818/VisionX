ditest = {'wave': ['Water1.jpg', 'Water2.jpg', 'Water3.jpg', 'Water5.jpg', 'Water6.jpg'], 'water': ['Water1.jpg', 'Water2.jpg', 'Water3.jpg', 'Water5.jpg', 'Water6.jpg'], 'sea': ['Water1.jpg', 'Water2.jpg', 'Water3.jpg', 'Water5.jpg', 'Water6.jpg'], 'ocean': ['Water1.jpg', 'Water2.jpg', 'Water3.jpg', 'Water5.jpg', 'Water6.jpg'], 'wind wave': ['Water1.jpg', 'Water2.jpg', 'Water3.jpg', 'Water6.jpg'], 'body of water': ['Water1.jpg', 'Water2.jpg', 'Water3.jpg', 'Water5.jpg', 'Water6.jpg'], 'sky': ['Water1.jpg', 'Water2.jpg', 'Water5.jpg', 'Water6.jpg'], 'coastal and oceanic landforms': ['Water2.jpg'], 'shore': ['Water2.jpg', 'Water3.jpg', 'Water5.jpg', 'Water6.jpg'], 'horizon': ['Water2.jpg', 'Water5.jpg', 'Water6.jpg'], 'sunset': ['Water5.jpg'], 'sunrise': ['Water5.jpg'], 'coast': ['Water6.jpg']}
# if 'sunset' not in ditest:
#          print('not present')
# print(ditest['sky'])
# # ditest['sky'].append('meow')
# # ditest['sky'] += ['meow']
# # ditest.setdefault('sky', []).append('meow')
# ditest.setdefault('test', []).append('a string')
# print(ditest)
# if 'test' in ditest:
#     ditest.setdefault('test', []).append('new string')
# # ditest.setdefault('test', []).append('a string')
# print(ditest)
#
# print(ditest['test'])

### GREAT JOB ###

for key in ditest.keys():
    for item in ditest[key]:
        print (key," ",item)
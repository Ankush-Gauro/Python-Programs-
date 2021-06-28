simple_list = [1,2,3,4]
simple_list.extend([5,6,7])
print(simple_list)

del simple_list[0]

print(simple_list)

d = {'name':'Max'}
print(d.items()) #dict_items([('name', 'Max')])

for k, v in d.items():
    print(k, v)

del d['name']
print(d)

t = (1,2,3)
print(t.index(1))
del t[0] #TypeError: 'tuple' object doesn't support item deletion

s = {'max', 'ana', 'max'}
del s['max'] #TypeError: 'set' object does not support item deletion
print(s)
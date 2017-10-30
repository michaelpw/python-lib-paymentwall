a = ''
if not a:
    print('a is empty')

b = {'captured': False}
if b['captured']:
    print('Hey!')

a = 'charge'
b = ''
c = ''
d = (a,b,c)
print(d)
for obj in d:
    if obj:
        print(obj)
        break
else:
    print("No object found")
from collections import namedtuple

Parts = namedtuple('Parts', 'id_num desc cost amount')
auto_parts = Parts(id_num='1234', desc='Ford Engine',
               cost=1200.00, amount=10)
print(auto_parts.id_num)


# regular tuple
auto_parts = ('1234', 'Ford Engine', 1200.00, 10)
print (auto_parts[2] ) 

id_num, desc, cost, amount = auto_parts
print (id_num)

# named tuple
from collections import namedtuple

Parts = {'id_num':'1234', 'desc':'Ford Engine',
     'cost':1200.00, 'amount':10}
parts = namedtuple('Parts', Parts.keys())(**Parts)
print (parts)


# same as above
from collections import namedtuple

Parts = {'id_num':'1234', 'desc':'Ford Engine',
     'cost':1200.00, 'amount':10}
parts = namedtuple('Parts', Parts.keys())
print(parts)

auto_parts = parts(**Parts)
print(auto_parts)
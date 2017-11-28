"""d1 = {1:10,2:20}
d2 = {3:30,4:40}
print d1+d2"""

# The above process results in TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
d1 = {1:10,2:20}
d2 = {3:30,4:40}
d3 = dict(d1.items()+d2.items())
print d3




#import pizza

#pizza.make_pizza(40, 'pepperoni')
#pizza.make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

#from pizza import make_pizza

#make_pizza(40, 'pepperoni')
#make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

#import pizza as p

#p.make_pizza(40, 'pepperoni')
#p.make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

from pizza import make_pizza as mp

mp(40, 'pepperoni')
mp(30, 'pieczarki', 'zielona papryka', 'podwójny ser')



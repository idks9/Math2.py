import math2
import numpy as np

data = [[1,10  ,5  ,12  ,8  ,7  ,13  ,2],
        [4,1210,180,2028,648,448,2548,18]];
x = data[0][:6];
y = data[1][:6]
p = math2.find_graphic_equation([x, y], 3);

print(x)
print(p[0]*(data[0][-1]**3)+p[1]*(data[0][-1]**2)+p[2]*(data[0][-1])+p[3])

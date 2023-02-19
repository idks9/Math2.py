import math2
import numpy as np

data = [[1,10  ,5  ,12  ,8  ,7  ,13  ,2],
        [4,1210,180,2028,648,448,2548,18]];

p = math2.find_graphic_equation(data, 3);

print(math2.r2(data, p)*100)

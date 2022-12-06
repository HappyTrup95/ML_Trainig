import pandas as pd
import math as m



E_sh_1=-(4/10)*m.log2((4/10)) - (6/10)*m.log2((6/10))
E_gav_0=(9/10)*0.99
E_gav_1=-(5/10)*0.72
E_sh_1 = E_sh_1-E_gav_0-E_gav_1
print(E_sh_1)
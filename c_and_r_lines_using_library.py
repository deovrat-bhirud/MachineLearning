import numpy as np
import pandas as pd
marks = {
'Physics' : [15, 12, 8, 8, 7, 7, 7, 6, 5, 3],
'History' : [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
}
df = pd.DataFrame(marks)
x_phy = df['Physics'].mean()
y_hist = df['History'].mean()
sd_phy = df['Physics'].std()
sd_hist = df['History'].std()
covar = df['Physics'].cov(df['History'])

# Karl-Pearson Coefficient

r = covar/(sd_phy*sd_hist)
print('Karl-Pearson Coefficient is ', r)

# value of Slope
b_1 = r*(sd_phy/sd_hist)
print('Slope is ', format(b_1, '0.3f'))

b_0 = y_hist - (b_1*x_phy)

# Calculating if mark is 10 in physics 
ans = b_1*10+b_0
print("Calculated marks is History is ", format(ans, '.1f'))

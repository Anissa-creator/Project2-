#Anissa Champiom
#Project 2 
#Pandas Library

import pandas as pd 
#Here I am importing another libraru to show Visualization
import matplotlib.pyplot as plt
data = {
  "calories": [101, 95, 97],
  "duration": [30, 25, 27]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
df.plot()
plt.show()
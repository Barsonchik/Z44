# Преобразование DataFrame в one-hot вид без использования функции get_dummies

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

# Cтолбец whoAmI преобразуется в one-hot вид
data['is_robot'] = data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)
data['is_human'] = data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)
data.head()


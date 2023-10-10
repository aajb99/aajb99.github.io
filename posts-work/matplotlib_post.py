# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# %%

iris = sns.load_dataset('iris')
titanic = sns.load_dataset('titanic')


# %%

titanic


# %%

# flights1_weather1 = pd.merge(flights1, weather1, on='date', how='inner')

# flights1_weather1 = flights1_weather1.dropna()

# flights1 = flights[(flights['month'] == 5) & (flights['day'].isin([1, 2]))]

# plt.scatter(x=flights1['air_time'], y=flights1['arr_delay'], s=1, c= flights1['distance'])

# plt.scatter(x=flights1['air_time'], y=flights1['arr_delay'], s=10, c= flights1['distance'], marker= '*')


# %%

sns.stripplot(x='petal_width', y='sepal_width', hue='species', size=6, data=iris)


# %%

sns.stripplot(x='petal_width', y='sepal_width', hue='species', data=iris, size=5,
              marker='.')

# %%

sns.regplot(x='petal_width', y='petal_length', data=iris, marker='.')


# %%

### advanced plot

sns.violinplot(x='pclass', y='age', data=titanic)


# %%

sns.violinplot(x='sex', y='age', hue='survived', data=titanic)


# %%

sns.violinplot(x='sex', y='fare', hue='survived', data=titanic)

# %%

sns.set_style('dark')

sns.violinplot(x='pclass', y='age', data=titanic)

# %%

sns.set_style('darkgrid')

sns.violinplot(x='pclass', y='age', data=titanic)

# %%

plt.title('Titanic: Age by Pclass')
plt.ylabel('Passenger Age')
plt.xlabel('Passenger Pclass') 

sns.violinplot(x='pclass', y='age', data=titanic)
# %%

sns.catplot(x='survived',
               y='age',
               hue='sex',
               data=titanic)

# %%

sns.pairplot(iris)

# %%

# Matplotlib

plot_name = sns.pairplot(iris)
plt.show(plot_name)

plot_name.savefig("plot_name.png",
            transparent=True)


# %%

import matplotlib.animation as mpla

T = np.linspace(0, 2*np.pi, 100)
line_s = np.sin(T)

line, = plt.plot(T, line_s)

def animate(i):
    line.set_ydata(np.sin(T+i/50))
anim = mpla.FuncAnimation(plt.gcf(), animate, interval=5)

plt.show


# %%

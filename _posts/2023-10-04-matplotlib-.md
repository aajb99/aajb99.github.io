---
layout: post
title:  "Exploring Powerful Visual Tools in Seaborn and other Visual Libraries"
author: Aaron Brown
description: An introduction to the Seaborn Cheatsheet and powerful visualization tools in Seaborn, as well as a brief introduction to Matplotlib
image: "/assets/images/20220722_124650.jpg"
--- 

## Setting up an environment for Python and the Seaborn library

* The first step to using Seaborn in your data analysis is to set up an Integrated Development Environment (IDE) for Python and its libraries. Such environments include Visual Studio Code, Pycharm, Jupyter Notebook, etc. Because this tutorial will cover specific tools in Seaborn (and Matplotlib) for data analysis and visualization, it will not cover the initial steps to set up an environment and get started with Python.

* To find help in setting this up, I suggest looking at [Pycharm Setup](https://www.guru99.com/how-to-install-python.html), [VS Code Setup](https://code.visualstudio.com/docs/python/python-tutorial), or other sources on setting up an environment for coding in Python.

* If you have your environment all set up and ready to go, then let's get started!



## Introduction

Data visualization is a key component of Data Science—we see it everywhere, from the beginning steps of Exploratory Analysis to the final product of our project analysis. Exploring different figures can help us Data Scientists understand more about our data and how it is structured, but they also make it easier for others to visualize and interpret our data and our findings (even if they aren't as into Data Science as you and I!). So, now that we know data visualization is a crucial part of data science and analysis, what are some good steps to get started? There are plenty of coding languages and visualization libraries we could choose from, but the Seaborn Library is a great tool to start with.

Python's Seaborn is well-known in Data Science for its quick and easy use as a data visualization tool. It contains a variety of functions used to plot your data in several different ways! But what's better—it was designed to provide you with visually-appealing figures of your data. If the bland, white background of your plot doesn't fit into your presentation well, then no worries! Seaborn makes it easy for you to switch backgrounds, plot configurations, point colors and sizes, you name it.

But rather than simply describing Seaborn's capabilities, why don't we dive right into it.


## Seaborn's Primary Plotting Functions and Customization Methods

Seaborn is a library in Python, and must therefore be imported into your Python Environment. However, because we will also be using Seaborn's companion visualization library Matplotlib in this tutorial, we should load both by inputting the following code.

```
---
import seaborn as sns
import matplotlib.pyplot as plt
---
```

(In importing these libraries, we call them by their abbreviations "sns" and "plt" for simplicity sake, and you will see instances of these later on).

Awesome! Now that we are set up with our two libraries, we can get started with our data visualization practice. First off, we need to determine which datasets we'll be using to perform visualization. In this tutorial, I will be using two datasets of differing variables and variable types in order to practice visualization with both categorical and quantitative variables. The 'iris' and 'titanic' datasets are already built-in to Python, so let's use those.

```
---
iris = sns.load_dataset('iris')
titanic = sns.load_dataset('titanic')
---
```

As you can see in the code above, Seaborn has many functions with different uses—even ones to load in a dataset! Now we will be focusing on functions from the [Seaborn Cheatsheet](https://www.markdownguide.org/extended-syntax/). You can read along as you search through the sheet, but feel free to continue using it when working on data visualization.

I want to go over some commonly-used functions in the "Categorical Plots" section. These functions are used to better understand categorical variables and relationships between variables. stripplot(), for instance, will help you determine the relationship between a categorical variable and a quantitative one—more or less, it is the substitution for a scatterplot in the presence of categorical data.

```
---
sns.stripplot(x='species', y='sepal_width', hue='species', size=6, data=iris)
---
```
<img src="{{site.url}}/{{site.baseurl}}/assets/images/strpplot1.png" alt="" style="width:500px;"/>

The only necessary parameters for stripplot() are
1. Your x variable, which is typically your categorical data if y is denoted as the response.
2. Your y variable, which is the other variable in the analysis (typically the quantitative variable).
3. Lastly, the data of focus. This dataset should carry both variables.

However, I also incorporated the parameters of "hue" and "size" to demonstrate the casual parameters you can choose to either specify or ignore (ignoring these other parameters sets them to a default condition). 

These casual parameters can prove particularly useful in certain cases. In analyzing two quantitative variables with a scatterplot, for example, you can also involve a categorical variable using the "hue" parameter. "Size" and "marker" are also helpful in determining the size and appearance of the points on the scatterplot.

```
---
sns.scatterplot(x='petal_width', y='sepal_width', hue='species', data=iris,
              marker='.')
---
```
<img src="{{site.url}}/{{site.baseurl}}/assets/images/sctrplt1.png" alt="" style="width:500px;"/>

Similarly to our previous example with stripplot() we incorporate "hue" according to the levels of species in the iris dataset. However, because x and y are both quantitative variables in the scatterplot, a categorical variable is added by color in order to compare its levels in the data. Also, "marker" is altered as a way to adjust the size of the data points.

In addition to the exploratory plots previously mentioned, Seaborn includes plotting functions designed to portray relationships between quantitative variables. Below, for example, is a linear regression plot for petal_length by petal_width from the iris dataset.

```
---
sns.regplot(x='petal_width', y='petal_length', data=iris, marker='.')
---
```

<img src="{{site.url}}/{{site.baseurl}}/assets/images/regplt1.png" alt="" style="width:500px;"/>

The examples I've showed you are merely a fraction of the plot functions offered in Seaborn. Again, I strongly suggest exploring the [Seaborn Cheatsheet](https://www.markdownguide.org/extended-syntax/) to practice additional functions. There are also plenty of other sources to look to when learning more about Seaborn and its capabilities. The [Seaborn API Reference List](https://seaborn.pydata.org/api.html) is such a source, and goes into further depth with plotting functions—with scatterplot(), for example, you can learn more about how "hue", "size", "marker", and other casual parameters can be utilized in comparing the levels of a categorical variable.

There's so much more to Seaborn than I can cover in a single tutorial, but there is certainly one last thing I feel should be discussed.


## Seaborn's Companionship with Matplotlib

While it is common to use Seaborn in Data Science to render plots and create aesthetically pleasing visualizations of one's data and stastical analysis, it is important to know where Seaborn is derived from. The Seaborn library was developed on top of Matplotlib—another data visualization tool in Python. Matplotlib also includes a variety of plotting and visualization functions, but it is not considered to be as "specialized" or effective as Seaborn in creating visually appealing and/or more complex plots. However, there are benefits to pulling functions from both libraries, and I want to introduce certain cases where both come in handy.

Now, you can import Matplotlib as a separate library from Seaborn, but as you can see above, we imported it as Matplotlib.pyplot which just allows us to apply Matplotlib functions to our Seaborn-created objects.

With that in mind, let's start out by creating a violin plot with our titanic data using Seaborn.

```
---
sns.violinplot(x='sex', y='age', hue='survived', split=True, data=titanic)
---
```

<img src="{{site.url}}/{{site.baseurl}}/assets/images/violplt1.png" alt="" style="width:500px;"/>

Here, I am using similar parameters to previous plots, except "split" is particularly useful for violin plots when you are applying a categorical variable to "hue". I would encourage you to look into other parameters and how they can strengthen you violin plot.

To this point, I've shown you a variety of plots offered in Seaborn, but without specific customizations such as labeling and layout. That is where Matplotlib comes into play. Under "Further Customizations" in the Seaborn Cheatsheet, you will see functions that are designed to help customize your plot. We will now incorporate some of these—specifically labeling functions—to our violin plot.

```
---
sns.violinplot(x='sex', y='age', hue='survived', split=True, data=titanic)

plt.title('Titanic: Age by Gender, Survival Comparison')
plt.ylabel('Passenger Age')
plt.xlabel('Passenger Gender')
---
```
<img src="{{site.url}}/{{site.baseurl}}/assets/images/violplt2.png" alt="" style="width:500px;"/>

You can also find customization options in other sections of the cheatsheet. In "Figure Aesthetics", for example, you can change the background of your plot using set_style() in Seaborn (in case you're tired of the blank white theme, or you want to add a grid, etc.). 

```
---
sns.set_style('darkgrid')

sns.violinplot(x='sex', y='age', hue='survived', split=True, data=titanic)

plt.title('Titanic: Age by Gender, Survival Comparison')
plt.ylabel('Passenger Age')
plt.xlabel('Passenger Gender') 
---
```
<img src="{{site.url}}/{{site.baseurl}}/assets/images/violpltdark.png" alt="" style="width:500px;"/>

Here, we are just using a couple of customization functions—I encourage you to look through more of them and to try them out!

Lastly, I want to introduce one last plot and show you how to save your new plot as a png file through Matplotlib.

This last plot is Seaborn's Pairplot, and is a good visualization feature for summarizing large datasets with multiple quantitative variables. All quantitative variables are compared with one another in a matrix format in order to visually describe and compare each combination's relationship. In addition to these scatterplots, histograms—as the default—are incorporated along the diagonal to depict the distribution of each variable individually.

```
---
sns.pairplot(iris)
---
```
<img src="{{site.url}}/{{site.baseurl}}/assets/images/iris_prplt.png" alt="" style="width:500px;"/>

It's as simple as that. But like I said, we're also trying to save this plot as a png file. To do so, we can use savefig() from Matplotlib.pyplot as is shown below.

```
---
sns.pairplot(iris)

plt.savefig("iris_prplt.png",
            transparent=True)
---
```
![Figure]({{site.url}}/{{site.baseurl}}/assets/images/prplt_combo.png)

Similarly to the other customization functions we performed, savefig() is run alongside the plot function—it will save the most recent plot output to the specified file name. With this example of savefig(), I included the casual parameter "transparent", which is another method for changing the theme of your plot (except this parameter offers the two different design options displayed above). If you prefer the original white display, you may ignore the "transparent" parameter altogether.


## Conclusion

Congradulations! You are one step closer to becoming a pro in data visualization. Having read this brief introduction to Seaborn and some of its core functions, you now have the know-how to read in datasets and explore their respective variables and other characteristics. You also know more about Seaborn's main purpose as a Python library along with its interaction with Matplotlib. However, there is still plenty to learn about the functions included in these libraries, and how they can help you portray more complex visuals in your analysis. I invite you to explore the additional resources previously mentioned, along with the [Matplotlib Cheatsheet](https://matplotlib.org/cheatsheets/_images/cheatsheets-1.png). Doing so will broaden your perspective of Python's visual libraries and the support they can provide you with along your Data Science journey. 

Now that you have the necessary tools to get started, go make some charts!
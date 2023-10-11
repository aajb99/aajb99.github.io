---
layout: post
title:  "Exploring Powerful Visual Tools in Seaborn and other Visual Libraries"
author: Aaron Brown
description: An introduction to the Seaborn Cheatsheet and powerful Seaborn tools for visualization, as well as a brief introduction to Matplotlib
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

Seaborn is a library in Python, and must therefore be imported into your Python Environment. However, because we will also be using Seaborn's companion visualization library Matplotlib in this tutorial, we should load both by inputting the following code:

```
---

import seaborn as sns
import matplotlib.pyplot as plt

---
```











* (look at seaborn cheatsheet https://images.datacamp.com/image/upload/v1676302629/Marketing/Blog/Seaborn_Cheat_Sheet.pdf and matplotlib cheatsheet https://matplotlib.org/cheatsheets/_images/cheatsheets-1.png) make sure to inclue in plots tools such as markers, color wheel, and animations

* basic plots: imshow and contour

* advanced plot: violin plot

* maybe even a scale to show animation

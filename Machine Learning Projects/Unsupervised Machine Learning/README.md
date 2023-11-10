# Unsupervised-Machine-Learning

In this task, we explore the differences between various Cities using
unsupervised learning methods such as Principal Component Analysis (PCA) and
various clustering techniques. The data we will be exploring contains 48 cities.
There are 4 variables for each city.

This problem can be broken down into the following steps:

  1. Exploring data
To improve the understanding of the data, I have performed a basic EDA on the dataset
by, loading the data, checking for null values, ploting the city index, displaying all 
the cities in the dataset, get statistical info, plot heatmap of the dataset and 
created other plots.

  2. Correlation analysis
I have then created a correlation plot. From the correlation plot, it is evident that 
Murder has a relatively strong positive correlation.

  3. Principal Component Analysis (PCA)
Principal Components Analysis (PCA) is a method for finding the underlying
variables (i.e. principal components) that best differentiate the observations by
determining the directions along which your data points are most spread out.
Since the determination of the principal components is based on finding the
direction that maximises the variance, variables with variance that are much
higher than the other variables tend to dominate the analysis purely due to their
scale.

  4. CLUSTER ANALYSIS
We will perform both Hierarchical Clustering and K-means to this data and
compare the results. Hierarchical clustering has the advantage that we can see the 
clusters visually in adendrogram and don’t have to specify the number of clusters 
before running the algorithm. However, we will have to decide the number of clusters
after the algorithm runs.

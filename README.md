# PythonDataAnlysisProject
Final project in the course Python for Data Analysis

The dataset is named **Facebook Comment Volume Dataset Data Set**, and is composed of 54 integeer/float attributes and the associated task is regression.

In fact, the main goal of the dataset is trying to **predict the exact number of comments in the next day under a Facebook publication**.

To do so, I have tried different models, everything is explain in the report.

For the conclusion, non of the model that I have tested can be considered as good, maybe except for the KNNRegressor one. 
Indeed, we still get a high RMSE, which is probably caused by the too few samples where the output is different from 0.
The KNNRegressor model will tend to surestimate the number of comments under a post.

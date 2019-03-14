### Case 3: Optimal Portfolio through Factor Models
---

#### Case Materials
1. You are provided with a simple dev kit for testing purposes. It contains a basic demo for data loading.
2. Training data can be downloaded at this [link](https://drive.google.com/open?id=1wwsc2wrK9BHVdc0GoIeDd0G8SAls9t36).
3. A simple guideline to factor models is available in this repo.

#### Case Background
1. You may assume that stock price returns are log normal.
2. You may assume that the market obeys Barra factor models (not Fama-French). There is a good reason why Fama-French is rarely used directly for factor investing, and we will go through the details during the case presentation on the day of the competition.
3. The training data covers 756 days over a 3-year period with a basket of 680 assets. The features for each stock are updated every 21 days. Due to the particular design of the dimensions, you should be mindful when you are either directly or implictly inverting a matrix. Check out its condition number for stability.
4. All the features are style-based. There are no macroeconomic factors.

#### Code Submission and Dependency Management
1. see [here](https://github.com/uchimwtc/MWTC19Submit)

#### Update
- 3/13/2019: We uploaded a new version of the training data that makes the periodicity of the features more pronounced. Please use the new data.
- 3/13/2019: We have taken down the PDF guide for modification. It will be updated soon.
- 3/13/2019: A new guide is available.
